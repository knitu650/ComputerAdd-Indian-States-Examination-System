#!/bin/bash

# Generate All Project Files Script
# This script creates the complete file structure with functional code

set -e

BASE_DIR="/workspace/ComputerAdd-Indian-States-Examination-System"
cd "$BASE_DIR"

echo "🚀 Generating Indian States Examination System Files..."

# Create all directories
echo "📁 Creating directory structure..."

mkdir -p backend/api-gateway/src/{controllers,middleware,routes,utils,config}
mkdir -p backend/microservices/user-service/src/{controllers,models,services,middleware,routes,utils,config}
mkdir -p backend/microservices/examination-service/src/{controllers,models,services,middleware,routes,utils}
mkdir -p backend/microservices/ai-ml-service/src/{controllers,models/{computer-vision,nlp,ml,deep-learning},services,utils,data/{datasets,trained_models,preprocessing}}
mkdir -p backend/microservices/proctoring-service/src/{controllers,services,middleware,routes,utils}
mkdir -p backend/microservices/analytics-service/src/{controllers,services,models,utils}
mkdir -p backend/microservices/notification-service/src/{controllers,services,templates/{email,sms,push},utils}
mkdir -p backend/microservices/payment-service/src/{controllers,services,models,utils}
mkdir -p backend/microservices/blockchain-service/src/{controllers,contracts,services,utils}
mkdir -p backend/shared/{config,utils,middleware,types}
mkdir -p backend/databases/{mongodb/{schemas,migrations,seeds},postgresql/{schemas,migrations,seeds},redis/config}

mkdir -p frontend/web-app/{public,src}/{components,pages,hooks,context,services,store,utils,styles,locales,workers}
mkdir -p frontend/admin-dashboard/{public,src}/{components,pages,services,store,utils,styles,hooks}

mkdir -p mobile/react-native/src/{components,screens,navigation,services,store,utils,assets,styles,hooks,locales}
mkdir -p mobile/android/app/src/main/{java/com/computeradd/indianstates,res}
mkdir -p mobile/ios/ComputerAddExam

mkdir -p ai-ml/{computer-vision,natural-language-processing,machine-learning,deep-learning,data,pipelines,configs,experiments,utils,tests}

mkdir -p devops/{terraform/{modules,environments/{dev,staging,production},global},kubernetes/{namespaces,deployments,services,configmaps,secrets,ingress,monitoring},docker,ansible/{playbooks,roles,inventory},monitoring/{prometheus,grafana,elk},ci-cd,security,backup}

mkdir -p docs
mkdir -p scripts/{deployment,maintenance,monitoring,utilities}
mkdir -p testing/{unit-tests,integration-tests,e2e-tests,load-tests}
mkdir -p kubernetes/{deployments,services,configmaps}
mkdir -p .github/workflows

echo "✅ Directory structure created!"

# Generate package.json files for all Node.js services
echo "📦 Generating package.json files..."

# User Service package.json
cat > backend/microservices/user-service/package.json << 'EOF'
{
  "name": "user-service",
  "version": "1.0.0",
  "description": "User authentication and management service",
  "main": "src/app.js",
  "scripts": {
    "start": "node src/app.js",
    "dev": "nodemon src/app.js",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^7.5.0",
    "bcryptjs": "^2.4.3",
    "jsonwebtoken": "^9.0.2",
    "dotenv": "^16.3.1",
    "joi": "^17.9.2",
    "nodemailer": "^6.9.4",
    "redis": "^4.6.7",
    "amqplib": "^0.10.3",
    "winston": "^3.10.0"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "jest": "^29.6.4"
  }
}
EOF

# Examination Service package.json
cat > backend/microservices/examination-service/package.json << 'EOF'
{
  "name": "examination-service",
  "version": "1.0.0",
  "description": "Examination management and delivery service",
  "main": "src/app.js",
  "scripts": {
    "start": "node src/app.js",
    "dev": "nodemon src/app.js",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^7.5.0",
    "redis": "^4.6.7",
    "socket.io": "^4.7.2",
    "axios": "^1.5.0",
    "dotenv": "^16.3.1",
    "winston": "^3.10.0"
  }
}
EOF

# AI/ML Service requirements.txt
cat > backend/microservices/ai-ml-service/requirements.txt << 'EOF'
fastapi==0.103.0
uvicorn[standard]==0.23.2
tensorflow==2.13.0
torch==2.0.1
torchvision==0.15.2
opencv-python==4.8.0.76
transformers==4.33.0
spacy==3.6.1
scikit-learn==1.3.0
pandas==2.1.0
numpy==1.25.2
Pillow==10.0.0
python-multipart==0.0.6
pydantic==2.3.0
pymongo==4.5.0
redis==5.0.0
celery==5.3.1
