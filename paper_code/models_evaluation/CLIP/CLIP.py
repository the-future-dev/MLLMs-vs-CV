import torch
import numpy as np

device = "cpu"

def classify(model, text, dataloader, dataset=""):
    true_labels = []
    predicted_labels = []
    checkpoint_interval = 100

    with torch.no_grad():
        for i, (images, labels) in enumerate(dataloader):
            images = images.to(device)
            labels = labels.to(device)

            image_features = model.encode_image(images)
            text_features = model.encode_text(text)

            # Compute the similarity between the image and text features
            similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
            predictions = similarity.argmax(dim=-1)

            true_labels.extend(labels.cpu().numpy())
            predicted_labels.extend(predictions.cpu().numpy())

            if i % checkpoint_interval == 0:
                np.save(f'results/true_labels-{dataset}.npy', true_labels)
                np.save(f'results/pred_labels-{dataset}.npy', predicted_labels)

    return true_labels, predicted_labels