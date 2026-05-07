"""
2026_05_08

Auxiliary file: LeNet5 model.

Convolutional Neural Network (CNN) exercise for the
Programmazione avanzata ed intelligenza artificiale [146179]
class at the University of Trento.
"""
import torch.nn as nn
import torch.nn.functional as F


class LeNet5(nn.Module):
    def __init__(self):
        super(LeNet5, self).__init__()
        
        # Layer C1: Convolutional Layer
        # Input: 1 channel (Grayscale), Output: 6 channels, Kernel: 5x5
        # We add padding=2 so the 28x28 MNIST image becomes 32x32 (LeNet original size)
        self.c1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, padding=2)
        
        # Layer S2: Subsampling (Pooling) Layer
        self.s2 = nn.AvgPool2d(kernel_size=2, stride=2)
        
        # Layer C3: Convolutional Layer
        self.c3 = nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5)
        
        # Layer S4: Subsampling (Pooling) Layer
        self.s4 = nn.AvgPool2d(kernel_size=2, stride=2)
        
        # Fully Connected Layers
        # Flattening 16 channels of 5x5 images = 400 features
        self.f5 = nn.Linear(in_features=16 * 5 * 5, out_features=120)
        self.f6 = nn.Linear(in_features=120, out_features=84)
        self.output = nn.Linear(in_features=84, out_features=10)

    def forward(self, x):
        # Convolution -> Activation -> Pooling
        x = self.s2(F.relu(self.c1(x)))
        x = self.s4(F.relu(self.c3(x)))
        
        # Flatten the data for the dense layers
        x = x.view(-1, 16 * 5 * 5)
        
        # Fully connected layers with ReLU
        x = F.relu(self.f5(x))
        x = F.relu(self.f6(x))
        
        # The final output (Logits)
        x = self.output(x)
        return x


if __name__ == "__main__":
    model = LeNet5()
    print(model)