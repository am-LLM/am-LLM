# DeepLearning.AI Deep Learning & Backpropagation Calculus Notes
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: Vectorized Neural Network Implementations from scratch, Backpropagation derivatives, and Adam Optimization.

---

## 1. Vectorized Matrix Calculus for L-Layer DNN

* **Forward Propagation**:
  $$Z^{[l]} = W^{[l]} A^{[l-1]} + b^{[l]}$$
  $$A^{[l]} = g^{[l]}(Z^{[l]})$$
* **Backward Propagation**:
  $$dZ^{[l]} = dA^{[l]} * {g^{[l]}}'(Z^{[l]})$$
  $$dW^{[l]} = rac{1}{m} dZ^{[l]} (A^{[l-1]})^T$$
  $$db^{[l]} = rac{1}{m} \sum dZ^{[l]}$$
