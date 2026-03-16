// Geospatial Fraud Risk Estimation

// Overview

This project implements a **geospatial fraud risk estimation pipeline** designed to prioritize inspections using spatial patterns of historical fraud occurrences.

By aggregating inspection outcomes across **hierarchical geospatial cells (geohashes)**, the system estimates the **probability of fraud at each service location**. This allows organizations to allocate inspection resources more efficiently and focus on high-risk areas.

The pipeline processes inspection datasets, computes spatial fraud frequencies, and produces **fraud risk scores** for each service point.

---

// Key Concepts

The methodology is based on three main ideas:

1. **Historical inspection analysis**  
   Fraud probability is inferred from historical inspection results.

2. **Spatial aggregation**  
   Fraud signals are aggregated using **geohash grids** to capture geographic patterns.

3. **Risk scoring**  
   Each service point receives a **fraud risk score** derived from spatial fraud frequency.

---

// Features

- Geospatial fraud detection pipeline
- Hierarchical spatial aggregation using geohash
- Fraud probability estimation
- Scalable data processing with parquet
- Modular Python pipeline
- Reproducible geospatial analytics workflow

---

// Technology Stack

| Category | Tools |
|--------|--------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Geospatial Encoding | Geohash |
| Data Format | Parquet |
| Pipeline Utilities | TQDM |

---

// Project Architecture

The pipeline follows the workflow below:

Raw Inspection Data  
↓  
Target Variable Creation  
↓  
Geospatial Encoding (Geohash)  
↓  
Spatial Aggregation  
↓  
Fraud Frequency Estimation  
↓  
Fraud Probability Calculation  
↓  
Fraud Risk Score Output  

This architecture allows fraud patterns to be captured across **multiple spatial resolutions**.

---

// Project Structure
