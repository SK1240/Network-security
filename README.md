# 🛡️Network Security - Phishing URL Detection Pipeline (End-to-End ML & MLOps)
This project demonstrates a complete **Machine Learning + MLOps workflow** for detecting phishing URLs. It covers **data ingestion → validation → transformation → model training → evaluation → deployment**, with **MLflow tracking**, **Docker containerization**, **CI/CD** via GitHub Actions, and deployment on **AWS (EC2 + ECR + S3)**.

---

## ✅ Key Features

- Structured, production-style **pipeline** with **logging**, **exceptions**, and **artifacts**

- **ETL Pipeline**: Extract data from **MongoDB**, transform it **(imputation, preprocessing, feature engineering)**, and load it into the pipeline for model training

- **FastAPI** service for training and prediction (/train, /predict)

- **MLflow** integration for experiments (parameters, metrics, and artifacts)

- **Containerized with Docker** for easy deployment

- **AWS deployment** workflow: **EC2**, **ECR**, and **S3 storage**

- GitHub Actions workflows for **CI/CD** included

- Utilities to sync artifacts to/from **S3**

---

## 📦 Project Structure

```
Network-Security/    
│── app.py                  # FastAPI app: /train and /predict    
│── main.py                 # Local CLI training entry (stage-by-stage)    
│── push_data.py            # Ingest source data into MongoDB    
│── setup.py                # Package setup (editable install)    
│── requirements.txt        # Dependencies    
│── Dockerfile              # Containerization    
│── test_mongodb.py         # Connectivity test for MongoDB    
│── .github/workflows/      # CI/CD workflows (GitHub Actions)    
│    
├── Artifacts/              # Auto-generated run artifacts (timestamped)    
│   ├── data_ingestion/     # feature_store/, ingested/{train.csv,test.csv}    
│   ├── data_validation/    # drift_report/report.yaml    
│   ├── data_transformation/# transformed/{train.npy,test.npy}, preprocessing.pkl    
│   ├── model_trainer/      # trained_model/model.pkl    
│   ├── model_evaluation/   # evaluation.yaml    
│   └── model_pusher/       # final packaging for serving    
│    
├── data_schema/            # (Optional) schema files for validation    
├── final_model/            # final model + preprocessor for API serving    
├── prediction_output/      # batch prediction outputs (if used)    
├── templates/              # Web templates (if UI routes are added)    
├── valid_data/             # curated/validated CSVs for quick tests    
└── networksecurity/        # Core ML pipeline (see below) 
```
