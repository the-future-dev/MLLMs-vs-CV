import requests
import torch
from PIL import Image
from transformers import AlignProcessor, AlignModel
from os import path
import json

processor = AlignProcessor.from_pretrained("kakaobrain/align-base")
model = AlignModel.from_pretrained("kakaobrain/align-base")

def load_labels(path):
    with open(path, 'r') as file:
        labels = json.load(file)
    return labels

dir = path.dirname(path.realpath(__file__))
imagenet_labels = load_labels(path.join(dir, '../../../../paper_code/data/labels_ImageNet.json'))

def test_inference():
    image = Image.open(path.join(dir, '../../../../paper_code/data/test.jpeg'))

    candidate_labels = ["an image of a lake", "an image of a forest", "an image of a mountain", "an image of a beach", "an image of a river", "an image of a sea"]
    inputs = processor(text=candidate_labels, images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    # this is the image-text similarity score
    logits_per_image = outputs.logits_per_image

    # we can take the softmax to get the label probabilities
    probs = logits_per_image.softmax(dim=1)

    label = candidate_labels[probs.argmax()]
    print("Label: ", label)

def single_image_classification(image):
    candidate_labels = imagenet_labels
    inputs = processor(text=candidate_labels, images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
    
    logits_per_image = outputs.logits_per_image

    probs = logits_per_image.softmax(dim=1)
    label = candidate_labels[probs.argmax()]
    print("Label: ", label)

    return f'{label}'

if __name__ == '__main__':
    test_inference()

