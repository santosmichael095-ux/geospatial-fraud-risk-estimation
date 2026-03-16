# Geospatial Fraud Risk Estimation

## Overview

This project implements a **geospatial fraud risk estimation pipeline** designed to prioritize inspections using spatial patterns of historical fraud occurrences.

By aggregating inspection outcomes across **hierarchical geospatial cells (geohashes)**, the system estimates the **probability of fraud at each service location**. This allows organizations to allocate inspection resources more efficiently and focus on high-risk areas.

The pipeline processes inspection datasets, computes spatial fraud frequencies, and produces **fraud risk scores** for each service point.

---

## Key Concepts

The methodology is based on three main ideas:

1. **Historical inspection analysis**  
Fraud probability is inferred from historical inspection results.

2. **Spatial aggregation**  
Fraud signals are aggregated using **geohash grids** to capture geographic patterns.

3. **Risk scoring**  
Each service point receives a **fraud risk score** derived from spatial fraud frequency.

---

## Features

- Geospatial fraud detection pipeline
- Hierarchical spatial aggregation using geohash
- Fraud probability estimation
- Scalable data processing with parquet
- Modular Python pipeline
- Reproducible geospatial analytics workflow

---

## Technology Stack

| Category | Tools |
|--------|--------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Geospatial Encoding | Geohash |
| Data Format | Parquet |
| Pipeline Utilities | TQDM |

---

## Project Architecture

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

## Project Structure

```
geospatial-fraud-risk-estimation/

README.md
requirements.txt
.gitignore

src/
    fraud_risk_pipeline.py

data/
    raw/
    processed/

outputs/
    fraud_risk_scores.parquet
```

---

## Pipeline Steps

### 1. Load Inspection Data

Inspection records are loaded from parquet datasets containing historical inspection outcomes.

Example fields:

- service_point_id
- inspection_date
- inspection_result
- latitude
- longitude

---

### 2. Target Variable Creation

A binary fraud variable is created:

```
fraud = 1 if inspection_result == "fraud"
fraud = 0 otherwise
```

---

### 3. Geospatial Encoding

Each service point is encoded using **Geohash**, which converts geographic coordinates into spatial grid identifiers.

Example:

```
Latitude:  -23.12
Longitude: -47.21
Geohash:   6gyf4
```

This allows efficient spatial grouping.

---

### 4. Spatial Aggregation

Fraud frequency is calculated for each geohash cell.

```
fraud_frequency = total_frauds / total_inspections
```

This value represents the **local fraud probability**.

---

### 5. Fraud Risk Estimation

Each service point receives a **fraud risk score** derived from the fraud frequency of its geohash region.

Higher values indicate higher fraud probability.

---

### 6. Export Results

The final output dataset contains:

| Field | Description |
|------|-------------|
| SERVICE_POINT_ID | Unique location identifier |
| FRAUD_RISK_SCORE | Estimated fraud probability |

Example output:

```
SERVICE_POINT_ID | FRAUD_RISK_SCORE
102345           | 0.42
102346           | 0.42
102347           | 0.17
```

The results are exported as:

```
outputs/fraud_risk_scores.parquet
```

---

## Running the Pipeline

### Clone the repository

```
git clone https://github.com/yourusername/geospatial-fraud-risk-estimation.git
```

---

### Install dependencies

```
pip install -r requirements.txt
```

---

### Run the pipeline

```
python src/fraud_risk_pipeline.py
```

---

## Data Confidentiality

The original datasets used in this project **cannot be shared** due to confidentiality restrictions.

To reproduce the pipeline, synthetic datasets with the following fields can be used:

- service_point_id
- latitude
- longitude
- inspection_result

---

## Potential Applications

This methodology can be applied in several domains:

- Utility fraud detection
- Inspection prioritization
- Infrastructure risk monitoring
- Geospatial anomaly detection
- Field operation optimization

---

## Future Improvements

Possible extensions include:

- Machine learning fraud prediction models
- Spatial clustering algorithms
- Real-time fraud risk dashboards
- Integration with GIS platforms
- Interactive geospatial visualization

---

## Author

Geospatial Data Engineering Project  
Fraud Risk Estimation Pipeline

---

## License

This repository is provided for **educational and portfolio purposes**.
