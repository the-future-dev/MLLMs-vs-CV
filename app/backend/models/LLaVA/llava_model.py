from transformers import pipeline
from PIL import Image
from os import path

model_id = "llava-hf/llava-1.5-7b-hf"
# model_id = "liuhaotian/llava-v1.6-mistral-7b"
pipe = pipeline("image-to-text", model=model_id)
dir = path.dirname(path.realpath(__file__))

def test_inference():
    image = Image.open(path.join(dir, '../../../../paper_code/data/test.jpeg'))

    prompt = "USER: <image>\nPerform zero-shot classification on this image: what label whould you give it?\nASSISTANT:"

    outputs = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 10})
    print(outputs)

def single_image_classification(image):
    # image
    prompt = "USER: <image>\nPerform zero-shot classification on this image: what label whould you give it?\nASSISTANT:"

    outputs = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 2})

    print("Label: ", outputs)
    return outputs

if __name__ == '__main__':
    test_inference()
