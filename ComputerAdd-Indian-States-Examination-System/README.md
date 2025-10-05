# ComputerAdd Indian States Examination System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)

## 🇮🇳 Overview

A comprehensive, AI-powered online examination system focused on Indian States knowledge assessment. This platform provides secure, proctored examinations with advanced features including computer vision-based monitoring, adaptive testing, and multi-language support for all 22 scheduled languages of India.

## 🚀 Key Features

### Examination Features
- **Adaptive Testing**: AI-powered question selection based on candidate performance
- **Multi-format Questions**: MCQ, True/False, Image-based, Audio, Drag-drop, Interactive maps
- **Real-time Proctoring**: Computer vision-based monitoring with face recognition
- **Secure Browser Lock**: Prevents cheating and unauthorized access
- **Offline Mode**: Continue exams during network disruptions

### Content Coverage
- All 28 States and 8 Union Territories
- Geography, History, Culture, Government, Economy
- 10,000+ curated questions
- Multi-language support (22 Indian languages)
- Interactive maps and multimedia content

### AI/ML Capabilities
- **Computer Vision**: Face recognition, object detection, behavior analysis
- **NLP**: Question generation, answer evaluation, multilingual processing
- **Machine Learning**: Performance prediction, recommendation engine, anomaly detection
- **Deep Learning**: Transformers (BERT, GPT, T5), CNN, RNN models

### Security & Compliance
- End-to-end encryption
- Blockchain-based certificates
- GDPR & IT Act 2000 compliant
- Multi-factor authentication
- Biometric verification

## 🏗️ Architecture

```
┌─────────────────┐
│   Load Balancer  │
└────────┬─────────┘
         │
    ┌────┴────┐
    │ API GW   │
    └────┬────┘
         │
    ┌────┴────────────────────────────┐
    │                                  │
┌───┴───┐  ┌──────┐  ┌────────┐  ┌────────┐
│ User  │  │ Exam │  │ AI/ML  │  │Proctor │
│Service│  │Service│  │Service │  │Service │
└───┬───┘  └──┬───┘  └────┬───┘  └────┬───┘
    │         │           │            │
    └─────────┴───────────┴────────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
    ┌───┴────┐      ┌───────┴────┐
    │MongoDB │      │PostgreSQL  │
    └────────┘      └────────────┘
```

## 📋 Prerequisites

- **Node.js**: v18.x or higher
- **Python**: 3.9 or higher
- **Docker**: 20.10.x or higher
- **Kubernetes**: v1.25 or higher
- **MongoDB**: 5.0 or higher
- **PostgreSQL**: 14.x or higher
- **Redis**: 6.2 or higher
- **CUDA**: 11.x (for GPU acceleration)

## 🛠️ Tech Stack

### Backend
- **API Gateway**: Node.js, Express.js, Kong
- **Microservices**: Node.js, Python (FastAPI)
- **Databases**: MongoDB, PostgreSQL, Redis
- **Message Queue**: RabbitMQ, Apache Kafka
- **Blockchain**: Ethereum, Web3.js, IPFS

### Frontend
- **Web**: React 18, Redux Toolkit, Material-UI
- **Admin**: React, TypeScript, Ant Design
- **Mobile**: React Native, Swift (iOS), Kotlin (Android)

### AI/ML
- **Computer Vision**: OpenCV, TensorFlow, PyTorch
- **NLP**: Transformers, BERT, GPT, spaCy
- **ML**: Scikit-learn, XGBoost, LightGBM
- **Deep Learning**: TensorFlow, PyTorch, Keras

### DevOps
- **Containerization**: Docker, Docker Compose
- **Orchestration**: Kubernetes, Helm
- **CI/CD**: GitHub Actions, Jenkins
- **Monitoring**: Prometheus, Grafana, ELK Stack
- **IaC**: Terraform, Ansible

## 🚀 Quick Start

### Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/computeradd/indian-states-exam-system.git
cd indian-states-exam-system

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Start all services
docker-compose up -d

# Access the application
# Web App: http://localhost:3000
# Admin Dashboard: http://localhost:3001
# API Gateway: http://localhost:8000
```

### Manual Setup

#### 1. Backend Services

```bash
# API Gateway
cd backend/api-gateway
npm install
npm run dev

# User Service
cd backend/microservices/user-service
npm install
npm run dev

# Examination Service
cd backend/microservices/examination-service
npm install
npm run dev

# AI/ML Service
cd backend/microservices/ai-ml-service
pip install -r requirements.txt
python src/app.py
```

#### 2. Frontend

```bash
# Web App
cd frontend/web-app
npm install
npm start

# Admin Dashboard
cd frontend/admin-dashboard
npm install
npm start
```

#### 3. Mobile

```bash
# React Native
cd mobile/react-native
npm install
npx react-native run-android  # For Android
npx react-native run-ios       # For iOS
```

## 📦 Installation

### Development Environment

```bash
# Install dependencies for all services
./scripts/setup.sh

# Start development environment
docker-compose -f docker-compose.dev.yml up
```

### Production Deployment

```bash
# Deploy to Kubernetes
kubectl apply -f kubernetes/namespaces/production.yaml
kubectl apply -f kubernetes/deployments/
kubectl apply -f kubernetes/services/

# Or use Helm
helm install exam-system ./helm-charts/exam-system
```

## 🔧 Configuration

### Environment Variables

```env
# Application
NODE_ENV=production
PORT=8000
API_VERSION=v1

# Database
MONGODB_URI=mongodb://localhost:27017/exam_system
POSTGRES_URI=postgresql://user:pass@localhost:5432/exam_db
REDIS_URL=redis://localhost:6379

# JWT
JWT_SECRET=your-secret-key
JWT_EXPIRY=7d

# AI/ML
TENSORFLOW_MODEL_PATH=/models
GPU_ENABLED=true

# AWS (Optional)
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
S3_BUCKET=exam-system-assets

# Payment
RAZORPAY_KEY_ID=your-key
RAZORPAY_KEY_SECRET=your-secret
```

## 🧪 Testing

```bash
# Run all tests
npm run test

# Unit tests
npm run test:unit

# Integration tests
npm run test:integration

# E2E tests
npm run test:e2e

# Load tests
npm run test:load
```

## 📊 Monitoring

Access monitoring dashboards:

- **Grafana**: http://localhost:3002
- **Prometheus**: http://localhost:9090
- **Kibana**: http://localhost:5601

## 🔒 Security

- All data encrypted at rest and in transit
- SOC 2 Type II compliant
- Regular security audits
- Vulnerability scanning with Trivy and Snyk
- WAF protection with ModSecurity

## 📱 Mobile Apps

### Android
- Minimum SDK: 24 (Android 7.0)
- Target SDK: 33 (Android 13)
- Download: [Google Play Store](#)

### iOS
- Minimum iOS: 13.0
- Target iOS: 16.0
- Download: [App Store](#)

## 🌍 Supported Languages

Hindi, English, Tamil, Telugu, Kannada, Malayalam, Gujarati, Marathi, Bengali, Punjabi, Assamese, Odia, Urdu, Sanskrit, and 8 more regional languages.

## 📖 Documentation

- [API Documentation](docs/API_Documentation.md)
- [Architecture Guide](docs/Architecture_Guide.md)
- [Deployment Guide](docs/Deployment_Guide.md)
- [User Manual](docs/User_Manual.md)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **ComputerAdd** - Development Team
- **Contributors** - See [CONTRIBUTORS.md](CONTRIBUTORS.md)

## 📞 Support

- **Email**: support@computeradd.com
- **Documentation**: https://docs.computeradd.com
- **Issues**: https://github.com/computeradd/indian-states-exam-system/issues

## 🗺️ Roadmap

- [x] Core examination system
- [x] AI-powered proctoring
- [x] Multi-language support
- [ ] Virtual Reality exam rooms
- [ ] Voice-based examinations
- [ ] Advanced analytics dashboard
- [ ] Mobile app enhancements

## ⭐ Acknowledgments

- Government of India for official state data
- Open source community
- All contributors and testers

---

Made with ❤️ by ComputerAdd Team | © 2025 All Rights Reserved
