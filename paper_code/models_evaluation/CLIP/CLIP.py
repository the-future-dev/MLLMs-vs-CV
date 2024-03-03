import torch
import numpy as np

device = "cpu"

def classify(model, text, dataloader, dataset=""):
    true_labels = []
    predicted_labels = []
    checkpoint_interval = 100

    with torch.no_grad():
        text_features = model.encode_text(text)

        for i, (images, labels) in enumerate(dataloader):
            images = images.to(device)
            labels = labels.to(device)

            image_features = model.encode_image(images)

            # Compute the similarity between the image and text features
            similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
            predictions = similarity.argmax(dim=-1)

            true_labels.extend(labels.cpu().numpy())
            predicted_labels.extend(predictions.cpu().numpy())

            print(f'True: {true_labels[-1]} | Predicted: {predicted_labels[-1]}')

            if i % checkpoint_interval == 0:
                np.save(f'results/true_labels-{dataset}.npy', true_labels)
                np.save(f'results/pred_labels-{dataset}.npy', predicted_labels)

    return true_labels, predicted_labels

def cifar100_classes():
    return [
        'apple',
        'aquarium fish',
        'baby',
        'bear',
        'beaver',
        'bed',
        'bee',
        'beetle',
        'bicycle',
        'bottle',
        'bowl',
        'boy',
        'bridge',
        'bus',
        'butterfly',
        'camel',
        'can',
        'castle',
        'caterpillar',
        'cattle',
        'chair',
        'chimpanzee',
        'clock',
        'cloud',
        'cockroach',
        'couch',
        'crab',
        'crocodile',
        'cup',
        'dinosaur',
        'dolphin',
        'elephant',
        'flatfish',
        'forest',
        'fox',
        'girl',
        'hamster',
        'house',
        'kangaroo',
        'keyboard',
        'lamp',
        'lawn mower',
        'leopard',
        'lion',
        'lizard',
        'lobster',
        'man',
        'maple tree',
        'motorcycle',
        'mountain',
        'mouse',
        'mushroom',
        'oak tree',
        'orange',
        'orchid',
        'otter',
        'palm tree',
        'pear',
        'pickup truck',
        'pine tree',
        'plain',
        'plate',
        'poppy',
        'porcupine',
        'possum',
        'rabbit',
        'raccoon',
        'ray',
        'road',
        'rocket',
        'rose',
        'sea',
        'seal',
        'shark',
        'shrew',
        'skunk',
        'skyscraper',
        'snail',
        'snake',
        'spider',
        'squirrel',
        'streetcar',
        'sunflower',
        'sweet pepper',
        'table',
        'tank',
        'telephone',
        'television',
        'tiger',
        'tractor',
        'train',
        'trout',
        'tulip',
        'turtle',
        'wardrobe',
        'whale',
        'willow tree',
        'wolf',
        'woman',
        'worm',
    ]

def templates():
    return [
        'a photo with subject a {}',
        'an image of a {}.',
        'a photo of a {}.',
        'a blurry photo of a {}.',
        'a black and white photo of a {}.',
        'a low contrast photo of a {}.',
        'a high contrast photo of a {}.',
        'a bad photo of a {}.',
        'a good photo of a {}.',
        'a photo of a small {}.',
        'a photo of a big {}.',
        'a photo of the {}.',
        'a blurry photo of the {}.',
        'a black and white photo of the {}.',
        'a low contrast photo of the {}.',
        'a high contrast photo of the {}.',
        'a bad photo of the {}.',
        'a good photo of the {}.',
        'a photo of the small {}.',
        'a photo of the big {}.',
    ]