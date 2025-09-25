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

---

## 🔑 Environment & Secrets(.env / GitHub Secrets)

Local `.env` file (create in repo root):    

MONGO_DB_URL="YOUR_MONGODB_URI"    
MONGODB_URL_KEY="YOUR_MONGODB_URI"   # used in app.py    
    
MLFLOW_TRACKING_URI="https://dagshub.com/<username>/<repo>.mlflow"    
MLFLOW_TRACKING_USERNAME="<your_username>"    
MLFLOW_TRACKING_PASSWORD="<your_token>"    
    
AWS_ACCESS_KEY_ID="<your_aws_access_key>"    
AWS_SECRET_ACCESS_KEY="<your_aws_secret_key>"    
AWS_DEFAULT_REGION="us-east-1"    
    
GitHub → Settings → Secrets → Actions:    
    
AWS_ACCESS_KEY_ID    
AWS_SECRET_ACCESS_KEY    
AWS_REGION = us-east-1        
AWS_ECR_LOGIN_URI = 788614365622.dkr.ecr.us-east-1.amazonaws.com/networkssecurity    
ECR_REPOSITORY_NAME = networkssecurity    
MLFLOW_TRACKING_URI    
MLFLOW_TRACKING_USERNAME    
MLFLOW_TRACKING_PASSWORD    
MONGO_DB_URL   # or MONGODB_URL_KEY 

---

## 🧭 Config Changes Before Run    

Open `networksecurity/constant/training_pipeline/__init__.py` and review:    

- TARGET_COLUMN = "Result"    
- FILE_NAME = "phisingData.csv"    
- ARTIFACT_DIR = "Artifacts"    
- MODEL_TRAINER_EXPECTED_SCORE = 0.60    
- TRAINING_BUCKET_NAME = "your-s3-bucket-name"    
    
---   
     
## ⚡ Quick Start (Local Setup)

📂 Clone Repository
```
git clone https://github.com/SK1240/Network-security.git    
cd Network-Security 
```   
    
### 🛠️ Create Virtual Environment  
```
python -m venv .venv    
.venv\Scripts\activate     # Windows    
source .venv/bin/activate  # Linux/Mac   
``` 
    
### 📦 Install Dependencies  
```
pip install -r requirements.txt    
```

### 🔑 Add Secrets   
```
nano .env    
```

---    
   
## 🗄️ MongoDB – Load Data
### ✅ Test Connection
```
python test_mongodb.py
```

### 📤 Push Data to MongoDB
```
python push_data.py
```

## 🤖 Run Training Pipeline
### ▶️ Execute End-to-End Pipeline
```
python main.py
```

---

## 📂 Artifacts will be created inside Artifacts/<timestamp>/:
* 📥 data_ingestion/

* 🧐 data_validation/

* 🔄 data_transformation/

* 🏋️ model_trainer/

* 📊 model_evaluation/

* 📦 model_pusher/

---

## 🚀 Run API (FastAPI)
### ▶️ Start API Server
```
uvicorn app:app --host 0.0.0.0 --port 5000 --reload
```

### 🏗️ Train via API
```
curl -X GET http://127.0.0.1:5000/train
```

### 🔍 Predict via API (Upload CSV)
curl -X POST "http://127.0.0.1:5000/predict" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@valid_data/sample.csv"

---

## 📊 MLflow Experiments
### 🖥️ Run MLflow Locally
```
mlflow ui --host 0.0.0.0 --port 5001
```
➡️ Open http://127.0.0.1:5001 in your browser

For DagsHub MLflow → set `MLFLOW_TRACKING_URI`, `USERNAME`, `PASSWORD` in `.env`

---

## ☁️ AWS Deployment (EC2 + Docker + ECR)
### 🔑 1. Connect to EC2 Instance
Replace <EC2-IP> with your **EC2 public IPv4 address**, and `your-key.pem` with your private key file:
```
chmod 400 your-key.pem   # set proper permissions first
ssh -i "your-key.pem" ubuntu@<EC2-IP>
```

### 🐳 2. Install Docker on EC2
```
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
docker --version
``` 

### 🔧 3. Configure AWS CLI
```
aws configure
```
👉 Enter your **AWS Access Key**, **Secret Key**, **Region** when prompted.


### 🏷️ 4. Login to Amazon ECR
AWS_REGION=us-east-1
AWS_ECR_LOGIN_URI=788614365622.dkr.ecr.$AWS_REGION.amazonaws.com
ECR_REPOSITORY_NAME=networkssecurity

aws ecr get-login-password --region $AWS_REGION \
| docker login --username AWS --password-stdin $AWS_ECR_LOGIN_URI


### 📦 5. Build & Push Docker Image
```
docker build -t $ECR_REPOSITORY_NAME:latest .
docker tag $ECR_REPOSITORY_NAME:latest $AWS_ECR_LOGIN_URI/$ECR_REPOSITORY_NAME:latest
docker push $AWS_ECR_LOGIN_URI/$ECR_REPOSITORY_NAME:latest
```