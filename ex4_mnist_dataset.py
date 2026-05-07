"""
2026_05_08

Auxiliary file: MnistDataloader class and visualization methods.

Convolutional Neural Network (CNN) exercise for the
Programmazione avanzata ed intelligenza artificiale [146179]
class at the University of Trento.
"""

import random
import struct
from array import array
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import torch
from torch.utils.data import TensorDataset


class MnistDataloader(object):
    def __init__(self, training_images_filepath: str,training_labels_filepath: str,
                 test_images_filepath: str, test_labels_filepath: str):
        self.training_images_filepath = training_images_filepath
        self.training_labels_filepath = training_labels_filepath
        self.test_images_filepath = test_images_filepath
        self.test_labels_filepath = test_labels_filepath
    
    def read_images_labels(self, images_filepath: str, labels_filepath: str) -> Tuple[list, array]:
        labels = []
        with open(labels_filepath, 'rb') as file:
            magic, size = struct.unpack(">II", file.read(8))
            if magic != 2049:
                raise ValueError('Magic number mismatch, expected 2049, got {}'.format(magic))
            labels = array("B", file.read())        
        
        with open(images_filepath, 'rb') as file:
            magic, size, rows, cols = struct.unpack(">IIII", file.read(16))
            if magic != 2051:
                raise ValueError('Magic number mismatch, expected 2051, got {}'.format(magic))
            image_data = array("B", file.read())        
        images = []
        for i in range(size):
            images.append([0] * rows * cols)
        for i in range(size):
            img = np.array(image_data[i * rows * cols:(i + 1) * rows * cols])
            img = img.reshape(28, 28)
            images[i][:] = img            
        
        return images, labels
            
    def load_data(self) -> Tuple[Tuple[list, array], Tuple[list, array]]:
        x_train, y_train = self.read_images_labels(self.training_images_filepath, self.training_labels_filepath)
        x_test, y_test = self.read_images_labels(self.test_images_filepath, self.test_labels_filepath)
        return (x_train, y_train),(x_test, y_test)

#
# Helper function to show a list of images with their relating titles
#
def show_images(images: list, title_texts: list):
    cols = 5
    rows = int(len(images)/cols) + 1
    
    # We maintain a large figure size so the images don't get squashed
    plt.figure(figsize=(30,20))
    index = 1    
    for x in zip(images, title_texts):        
        image = x[0]        
        title_text = x[1]
        plt.subplot(rows, cols, index)        
        
        # Turn off the pixel axes (optional, but looks much cleaner for presentation)
        # plt.axis('off') 

        plt.imshow(image, cmap=plt.cm.gray)
        
        if (title_text != ''):
            # Increase fontsize for large screen visibility
            plt.title(title_text, fontsize = 15, fontweight='bold');        
        index += 1
    
    # adjust subplot to give everything breathing room
    plt.tight_layout(pad=5.0)

def show_mnist(x_train: list, x_test: list, y_train: array, y_test: array):
    images_2_show = []
    titles_2_show = []
    for i in range(0, 10):
        r = random.randint(1, 60000)
        images_2_show.append(x_train[r])
        titles_2_show.append('training image [' + str(r) + '] = ' + str(y_train[r]))    

    for i in range(0, 5):
        r = random.randint(1, 10000)
        images_2_show.append(x_test[r])        
        titles_2_show.append('test image [' + str(r) + '] = ' + str(y_test[r]))    

    show_images(images_2_show, titles_2_show)
    plt.show()


def preprocess_data(x, y):
    # Convert to numpy, normalize to [0, 1], and add channel dimension (Batch, Channel, H, W)
    x_tensor = torch.tensor(np.array(x), dtype=torch.float32).unsqueeze(1) / 255.0
    y_tensor = torch.tensor(np.array(y), dtype=torch.long)
    return TensorDataset(x_tensor, y_tensor)

if __name__ == "__main__":
    ### step 1 - load and show MNIST dataset
    # get paths
    data_folder_path = '/home/pfpimenta/python_exercises_unitn/data/mnist/'
    training_images_filepath = data_folder_path + 'train-images-idx3-ubyte/train-images-idx3-ubyte'
    training_labels_filepath = data_folder_path + 'train-labels-idx1-ubyte/train-labels-idx1-ubyte'
    test_images_filepath = data_folder_path + 't10k-images-idx3-ubyte/t10k-images-idx3-ubyte'
    test_labels_filepath = data_folder_path + 't10k-labels-idx1-ubyte/t10k-labels-idx1-ubyte'

    #  load data
    mnist_dataloader = MnistDataloader(training_images_filepath, training_labels_filepath, test_images_filepath, test_labels_filepath)
    (x_train, y_train), (x_test, y_test) = mnist_dataloader.load_data()

    # Show some random training and test images 
    show_mnist(x_train, x_test, y_train, y_test)