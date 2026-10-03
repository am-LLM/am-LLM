#!/usr/bin/env python3
"""
Google Cloud Generative AI: Vector Similarity & Grounded Context Synthesizer
Demonstrates cosine similarity ranking for Vertex AI Vector Search pipelines.
"""

import numpy as np

def cosine_similarity(vec_a, vec_b):
    return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b) + 1e-9)

class VectorSearchSimulator:
    def __init__(self):
        self.corpus = []

    def index(self, text: str, embedding: np.ndarray):
        self.corpus.append({"text": text, "vec": embedding})

    def search(self, query_vec: np.ndarray, top_k: int = 2):
        scores = [(item["text"], cosine_similarity(query_vec, item["vec"])) for item in self.corpus]
        return sorted(scores, key=lambda x: x[1], reverse=True)[:top_k]

if __name__ == "__main__":
    db = VectorSearchSimulator()
    np.random.seed(42)
    db.index("ISO 22301 Business Continuity Guide", np.random.randn(128))
    db.index("NIST ML-KEM Cryptographic Standard", np.random.randn(128))
    
    query = np.random.randn(128)
    results = db.search(query)
    print("[*] Vertex AI Vector Search Top Matches:")
    for text, score in results:
        print(f"  Score: {score:.4f} | Document: {text}")
