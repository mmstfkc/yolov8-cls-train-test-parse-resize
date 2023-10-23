import os
import shutil
import random
from PIL import Image


def resize_image(image_path, size=(1280, 1280)):
    image = Image.open(image_path)
    image = image.resize(size)
    image.save(image_path)


def split_dataset(dataset_path, train_percentage, destination_path, image_size=(1280, 1280)):
    if train_percentage < 0 or train_percentage > 100:
        raise ValueError("Train percentage should be between 0 and 100.")

    # Create destination path
    new_dataset_train_path = os.path.join(destination_path, "train")
    new_dataset_test_path = os.path.join(destination_path, "test")
    os.makedirs(new_dataset_train_path, exist_ok=True)
    os.makedirs(new_dataset_test_path, exist_ok=True)

    for class_name in os.listdir(dataset_path):
        class_path = os.path.join(dataset_path, class_name)
        if os.path.isdir(class_path):
            train_class_path = os.path.join(new_dataset_train_path, class_name)
            test_class_path = os.path.join(new_dataset_test_path, class_name)
            os.makedirs(train_class_path, exist_ok=True)
            os.makedirs(test_class_path, exist_ok=True)

            for file_name in os.listdir(class_path):
                if random.randint(1, 100) <= train_percentage:
                    destination = os.path.join(train_class_path, file_name)
                else:
                    destination = os.path.join(test_class_path, file_name)

                source_file = os.path.join(class_path, file_name)
                shutil.copy(source_file, destination)

                if image_size:
                    resize_image(destination, image_size)


if __name__ == "__main__":
    dataset_path = "dataset_path"
    train_percentage = 80  # Example %80 train, %20 test
    destination_path = "destination_path"
    image_size = (1280, 1280)

    split_dataset(dataset_path, train_percentage, destination_path, image_size)