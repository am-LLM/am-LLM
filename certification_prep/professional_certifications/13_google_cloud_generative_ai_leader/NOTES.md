# Google Cloud Generative AI Enterprise Architecture Notes
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: Google Cloud Vertex AI, Gemini Foundation Models, Retrieval-Augmented Generation (RAG), and Enterprise AI Governance.

---

## 1. Vertex AI RAG Pipeline Architecture

```
[ User Query ] ──▶ [ Embedding Model (text-embedding-004) ] ──▶ [ Vertex AI Vector Search ]
                                                                             │
                                                                 Top-K Context Chunks
                                                                             ▼
[ Grounded Response ] ◀── [ Gemini 1.5 Pro / Flash ] ◀── [ Augmented Prompt + Context ]
```
