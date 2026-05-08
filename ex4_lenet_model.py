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
        
        # C1: Convolutional Layer (6 filters, 5x5)
        # Input 1x28x28 -> Padding 2 -> 1x32x32 -> Output 6x28x28
        self.c1 = nn.Conv2d(1, 6, kernel_size=5, padding=2)
        
        # S1: Subsampling (2x2 Avg Pool)
        # Output 6x14x14
        self.s1 = nn.AvgPool2d(kernel_size=2, stride=2)
        
        # C2: Convolutional Layer (16 filters, 5x5)
        # Output 16x10x10
        self.c2 = nn.Conv2d(6, 16, kernel_size=5)
        
        # S2: Subsampling (2x2 Avg Pool)
        # Output 16x5x5
        self.s2 = nn.AvgPool2d(kernel_size=2, stride=2)
        
        # C3: Convolutional Layer (120 filters, 5x5)
        # This layer "flattens" the 5x5 space because the kernel matches the input size
        # Output 120x1x1
        self.c3 = nn.Conv2d(16, 120, kernel_size=5)
        
        # F1: Fully Connected Layer
        self.f1 = nn.Linear(120, 84)
        
        # F2: Output Layer
        self.f2 = nn.Linear(84, 10)

    def forward(self, x):
        # Convolution blocks
        x = F.tanh(self.c1(x))
        x = self.s1(x)
        
        x = F.tanh(self.c2(x))
        x = self.s2(x)
        
        x = F.tanh(self.c3(x))
        
        # Flatten: from (Batch, 120, 1, 1) to (Batch, 120)
        x = x.view(-1, 120)
        
        # Fully connected layers
        x = F.tanh(self.f1(x))
        x = self.f2(x) # Output logits
        
        return x


if __name__ == "__main__":
    model = LeNet5()
    print(model)