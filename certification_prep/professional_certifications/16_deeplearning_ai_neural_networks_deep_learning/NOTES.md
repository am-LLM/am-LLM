# DeepLearning.AI: Neural Networks and Deep Learning Specialization

## 1. Vectorized Multi-Layer Neural Network Mathematics

```
                FORWARD & BACKWARD PROPAGATION COMPUTATIONAL GRAPH
 Layer [l-1]                   Layer [l]                    Loss L
 ┌──────────┐   W[l], b[l]   ┌──────────┐      Activation  ┌──────────┐
 │  A[l-1]  │ ─────────────> │ Z[l]     │ ───────────────> │ A[l]     │ ──> L(A[L], Y)
 └──────────┘                └──────────┘                  └──────────┘
      ▲                           │                             │
      │ dW[l], db[l]              │ dZ[l]                       │ dA[l]
      └───────────────────────────┴─────────────────────────────┘
```

### Forward Propagation Equations (Batch of $m$ Examples):
$$Z^{[l]} = W^{[l]} A^{[l-1]} + b^{[l]}$$
$$A^{[l]} = g^{[l]}(Z^{[l]})$$

### Binary Cross-Entropy Cost Function:
$$\mathcal{J}(W, b) = -\frac{1}{m} \sum_{i=1}^m \Big[ y^{(i)} \log(a^{[L](i)}) + (1 - y^{(i)}) \log(1 - a^{[L](i)}) \Big]$$

### Backward Propagation Equations:
$$dZ^{[l]} = dA^{[l]} * {g^{[l]}}'(Z^{[l]})$$
$$dW^{[l]} = \frac{1}{m} dZ^{[l]} (A^{[l-1]})^T$$
$$db^{[l]} = \frac{1}{m} \sum_{i=1}^m dZ^{[l](i)}$$
$$dA^{[l-1]} = (W^{[l]})^T dZ^{[l]}$$

### Parameter Initialization Best Practices:
* **Xavier / Glorot Initialization** (for $\tanh$ / Sigmoid activations):
  $$W^{[l]} \sim \mathcal{N}\left(0, \sqrt{\frac{2}{n^{[l-1]} + n^{[l]}}}\right)$$
* **He Initialization** (for ReLU / LeakyReLU activations):
  $$W^{[l]} \sim \mathcal{N}\left(0, \sqrt{\frac{2}{n^{[l-1]}}}\right)$$
