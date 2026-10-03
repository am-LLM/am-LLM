# Microsoft DP-800 Azure Data & AI Architecture Notes
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: Microsoft Fabric, Azure Synapse Analytics, Delta Lake Lakehouse, and Azure OpenAI Service Integration.

---

## 1. Delta Lake Medallion Architecture

* **Bronze (Raw Ingestion)**: Append-only raw streaming ingestion from Event Hubs / IoT Hub.
* **Silver (Cleaned & Enriched)**: Schema enforcement, deduping, and typed transformations.
* **Gold (Business Aggregates)**: Dimensional star-schema models for Power BI and ML models.
