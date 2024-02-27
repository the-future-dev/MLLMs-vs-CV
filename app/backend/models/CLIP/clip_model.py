import torch
import clip
from PIL import Image
import json
from os import path

device = "cpu"
# device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def load_labels(path):
    with open(path, 'r') as file:
        labels = json.load(file)
    return labels

dir = path.dirname(path.realpath(__file__))
labels = load_labels(path.join(dir, '../../../../data/labels_ImageNet.json'))

print("OK")

text = clip.tokenize(labels).to(device)


def test_inference():
    image = preprocess(Image.open(path.join(dir, '../../../../data/test.jpeg'))).unsqueeze(0).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        logits_per_image, logits_per_text = model(image, text)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()

    print("Label: ", labels[probs.argmax()])

def single_image_classification(image):
    image = preprocess(image).unsqueeze(0).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        logits_per_image, logits_per_text = model(image, text)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()

    # Get the label with the highest probability
    label = labels[probs.argmax()]

    print("Label: ", label)

    return f'{label}'

if __name__ == '__main__':
    test_inference()
