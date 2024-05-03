from keras import utils, layers, Sequential
from os import path

IMAGE_SIZE=(224,224)

def __get_dataset(directory, subdir, augment=False):
    return utils.image_dataset_from_directory(path.join(directory, subdir), image_size=IMAGE_SIZE) 

def get_datasets(base_dir):
    return __get_dataset(base_dir, "train"), __get_dataset(base_dir, "test"), __get_dataset(base_dir, "valid")