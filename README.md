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

---

## 🧠 Core ML Pipeline – `networksecurity/`

```
networksecurity/
├── cloud/
│   └── s3_syncer.py           # Sync local folders with S3
│
├── components/
│   ├── data_ingestion.py      # Pull from MongoDB, split train/test
│   ├── data_validation.py     # Schema checks, nulls, drift detection
│   ├── data_transformation.py # Preprocessing, imputation
│   └── model_trainer.py       # Train model, log via MLflow
│
├── constant/
│   └── training_pipeline/__init__.py
│       # Configs: TARGET_COLUMN, PIPELINE_NAME, ARTIFACT_DIR, FILE_NAME
│
├── entity/
│   ├── config_entity.py       # Config objects
│   └── artifact_entity.py     # Pipeline artifact objects
│
├── exception/
│   └── exception.py           # Custom exception handling
│
├── logging/
│   └── logger.py              # Logging utility
│
├── pipeline/
│   ├── training_pipeline.py   # Orchestrates all steps
│   └── batch_prediction.py    # Batch prediction runner
│
└── utils/
    ├── main_utils/utils.py    # Save/load objects, metrics, YAML utils
    └── ml_utils/
        ├── metric/classification_metric.py
        └── model/estimator.py # Preprocessor + model wrapper
```