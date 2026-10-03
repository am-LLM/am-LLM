# Google Cloud Certified: Generative AI Leader & Cloud Architect Reference

## 1. Vertex AI Generative AI Architecture

```
                   VERTEX AI END-TO-END RAG PIPELINE
 ┌────────────────┐     ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
 │ Enterprise Doc │ ──> │ Text-Embedding │ ──> │ Vertex Vector  │ ──> │ Gemini 1.5 Pro │
 │ Repository     │     │ Gecko / 004    │     │ Search (ScaNN) │     │ (Grounded Gen) │
 └────────────────┘     └────────────────┘     └────────────────┘     └────────────────┘
                                                       │                       ▲
                                                       ▼                       │
                                               Grounding Metadata /            │
                                               Citation Attributions ──────────┘
```

---

## 2. Core Generative AI Patterns on GCP

### Model Garden & Foundation Model Selection
* **Gemini 1.5 Pro / Flash**: Multimodal native (Video, Audio, Code, Text), up to 2M token context window. Best for massive codebases, longitudinal document synthesis.
* **Context Caching**: Reduce latency and input token costs by up to 75% for repeated prompt prefixes on large context corpora.
* **Model Tuning Types**:
  1. **Prompt Engineering / Few-Shot In-Context Learning**: Zero model weights updated.
  2. **Parameter-Efficient Fine-Tuning (PEFT / LoRA / QLoRA)**: Freezes base weights, trains low-rank adapter matrices.
  3. **Full Fine-Tuning**: Updates all model weights on domain-specific corpora.
  4. **Distillation**: Compresses knowledge from large teacher (Gemini Pro) to small student (Gemini Flash).

### Enterprise Guardrails & Grounding
* **Vertex AI Search Grounding**: Connects Gemini responses directly to Google Search or proprietary enterprise Datastores, returning verbatim snippets and verifiable citation indices.
* **Safety Filters**: Dynamic threshold blocking for Hate Speech, Harassment, Sexual Content, Dangerous Content.
