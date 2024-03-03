import os
from PIL import Image

def create_dataset(file_name):
    # Read the file
    with open(file_name, 'r') as f:
        lines = f.readlines()

    # Create a dictionary to store the data
    data = {}
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 4:
            print(f"Unexpected format: {line}")
            continue
        n_value, _, label, superlabel = parts
        data[n_value] = {'label': label, 'superlabel': superlabel}

    # Create a dataset
    dataset = []
    for n_value, info in data.items():
        # Get the list of image files in the folder
        folder_path = f'../../data/miniImageNetTest/{n_value}'
        image_files = os.listdir(folder_path)

        # Read each image file
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            image = Image.open(image_path)
            dataset.append({
                'image': image,
                'label': info['label'],
                'superlabel': info['superlabel']
            })

    return dataset