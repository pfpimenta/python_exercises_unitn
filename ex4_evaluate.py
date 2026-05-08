"""
2026_05_08

Evaluation file: loads the model and evaluates it on the test dataset.

Convolutional Neural Network (CNN) exercise for the
Programmazione avanzata ed intelligenza artificiale [146179]
class at the University of Trento.

Objective: Application of a CNN in a toy example
"""
from pathlib import Path

import torch
from torch.utils.data import DataLoader
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

from ex4_lenet_model import LeNet5
from ex4_mnist_dataset import MnistDataloader, preprocess_data # dataset is defined here


### 1. Load Test Data
# get paths
base_path = Path(__file__).resolve().parent # project folder path
data_folder_path = base_path / "data" / "mnist"
training_images_filepath = data_folder_path / 'train-images-idx3-ubyte/train-images-idx3-ubyte'
training_labels_filepath = data_folder_path / 'train-labels-idx1-ubyte/train-labels-idx1-ubyte'
test_images_filepath = data_folder_path / 't10k-images-idx3-ubyte/t10k-images-idx3-ubyte'
test_labels_filepath = data_folder_path / 't10k-labels-idx1-ubyte/t10k-labels-idx1-ubyte'

#  load data
mnist_dataloader = MnistDataloader(training_images_filepath, training_labels_filepath, test_images_filepath, test_labels_filepath)
_, (x_test, y_test) = mnist_dataloader.load_data()

# 2. Preprocess
test_dataset = preprocess_data(x_test, y_test)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# 3. Initialize Model and Load Saved Weights
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = LeNet5().to(device)
model_filepath = base_path / "lenet5_mnist.pth"
model.load_state_dict(torch.load(model_filepath, map_location=device))
model.eval()

# 4. Evaluation Loop
correct = 0
total = 0
all_preds = []
all_labels = []
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

        # collecting for confusion matrix
        all_preds.extend(predicted.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())

print(f'Accuracy on 10,000 test images: {100 * correct / total:.2f}%')

### Extra: confusion matrix
# Compute confusion matrix
cm = confusion_matrix(all_labels, all_preds)

# Plot confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=list(range(10)))
disp.plot(cmap=plt.cm.Blues, values_format='d')
plt.title(f'Confusion Matrix: LeNet-5 on MNIST\nAccuracy: {100 * correct / total:.2f}%')
plt.show()
