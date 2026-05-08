"""
2026_05_08

Train file: trains the model on the train dataset and saves it in a .pth file.

Convolutional Neural Network (CNN) exercise for the
Programmazione avanzata ed intelligenza artificiale [146179]
class at the University of Trento.

Objective: Application of a CNN in a toy example
"""
from pathlib import Path
from time import time

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from ex4_lenet_model import LeNet5  # model is defined here
from ex4_mnist_dataset import MnistDataloader, preprocess_data # dataset is defined here

### step 1 - load MNIST dataset

# get paths
base_path = Path(__file__).resolve().parent # project folder path
data_folder_path = base_path / "data" / "mnist"
training_images_filepath = data_folder_path / 'train-images-idx3-ubyte/train-images-idx3-ubyte'
training_labels_filepath = data_folder_path / 'train-labels-idx1-ubyte/train-labels-idx1-ubyte'
test_images_filepath = data_folder_path / 't10k-images-idx3-ubyte/t10k-images-idx3-ubyte'
test_labels_filepath = data_folder_path / 't10k-labels-idx1-ubyte/t10k-labels-idx1-ubyte'

#  load data
mnist_dataloader = MnistDataloader(training_images_filepath, training_labels_filepath, test_images_filepath, test_labels_filepath)
(x_train, y_train), (x_test, y_test) = mnist_dataloader.load_data()

# Prepare DataLoaders
train_dataset = preprocess_data(x_train, y_train)
test_dataset = preprocess_data(x_test, y_test)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

### step 2 - train model

# define training config
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = LeNet5().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 5
print(f"Training on {device}...")

# count training time:
training_start_time = time()

### training loop
for epoch in range(epochs):
    epoch_start_time = time()
    model.train()
    epoch_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        
        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward pass and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        epoch_loss += loss.item()
    
    epoch_end_time = time()
    epoch_time = epoch_end_time - epoch_start_time
    print(f"Epoch [{epoch+1}/{epochs}],\tLoss: {epoch_loss/len(train_loader):.4f} \t elapsed time: {epoch_time:.4f} seconds")

training_end_time = time()
training_time = training_end_time - training_start_time
print(f"Training completed in {training_time:.4f} seconds")

### step 3 - Save the Weights (State Dict)
model_filepath = base_path / "lenet5_mnist.pth"
torch.save(model.state_dict(), model_filepath)
print(f"Model saved to {model_filepath}")
