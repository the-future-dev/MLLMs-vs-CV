from dotenv import load_dotenv
import requests
import base64
from PIL import Image
import io
from os import path

load_dotenv()
API_KEY = os.getenv('API_TOKEN')

api_url = "https://api-inference.huggingface.co/models/llava-hf/llava-1.5-7b-hf"
headers = {"Authorization": f"Bearer {API_KEY}"}

dir = path.dirname(path.realpath(__file__))

def test_inference():
    with open(path.join(dir, '../../../../paper_code/data/test.jpeg'), 'rb') as f:
        image = f.read()
    img_str = base64.b64encode(image).decode()

    # Specify the text_prompt
    text_prompt = "USER: <image>\nPerform zero-shot classification on this image: what label whould you give it?\nASSISTANT:"

    # Prepare the payload
    payload = {
        "inputs": {
            "image": img_str,
            "text_prompt": text_prompt
        }
    }

    # Request to Hugging Face API
    response = requests.post(api_url, headers=headers, json=payload)

    print(response.json())

if __name__ == '__main__':
    test_inference()