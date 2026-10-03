#!/usr/bin/env python3
"""
DeepLearning.AI Module: Pure Vectorized 2-Layer Neural Network from Scratch in NumPy
"""

import numpy as np

class TwoLayerNN:
    def __init__(self, n_x: int, n_h: int, n_y: int):
        np.random.seed(42)
        self.W1 = np.random.randn(n_h, n_x) * 0.01
        self.b1 = np.zeros((n_h, 1))
        self.W2 = np.random.randn(n_y, n_h) * 0.01
        self.b2 = np.zeros((n_y, 1))

    def forward(self, X):
        Z1 = np.dot(self.W1, X) + self.b1
        A1 = np.maximum(0, Z1)  # ReLU
        Z2 = np.dot(self.W2, A1) + self.b2
        A2 = 1 / (1 + np.exp(-Z2))  # Sigmoid
        return A2

if __name__ == "__main__":
    nn = TwoLayerNN(n_x=4, n_h=8, n_y=1)
    sample_input = np.random.randn(4, 3)
    output = nn.forward(sample_input)
    print("[*] Vectorized Forward Propagation Output:")
    print(f"  Shape: {output.shape} | Predictions: {output.ravel().round(4)}")
