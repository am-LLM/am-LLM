# Microsoft DP-800: Azure AI & Enterprise Data Engineering Solutions

## 1. Microsoft Fabric & Delta Lake Medallion Architecture

```
                 MEDALLION DATA LAKEHOUSE PATTERN (FABRIC ONELAKE)
 ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
 │ Bronze (Raw)    │ ───> │ Silver (Clean)  │ ───> │ Gold (Curated)  │
 │ Append-only raw │      │ Deduplicated &  │      │ Aggregated star │
 │ ingestion lake  │      │ Schema-enforced │      │ schema business │
 └─────────────────┘      └─────────────────┘      └─────────────────┘
```

---

## 2. Core Azure Data Engineering Components
* **Microsoft Fabric OneLake**: Single unified logical SaaS data lake over Azure Blob/ADLS Gen2 eliminating data siloing.
* **Delta Lake ACID Guarantees**: Parquet file storage backed by `_delta_log` JSON transaction logs ensuring Serializable / WriteSerializable isolation.
* **Azure Cosmos DB Vector Search**: Integrated DiskANN and HNSW vector indexing for real-time semantic retrieval alongside operational transactional workloads.
* **Azure Synapse Serverless SQL**: Query data directly in OneLake parquet format using standard T-SQL with zero dedicated compute clusters.
