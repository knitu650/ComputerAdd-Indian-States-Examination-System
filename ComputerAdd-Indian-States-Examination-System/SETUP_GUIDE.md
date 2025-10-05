# Setup Guide - Indian States Examination System

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

### Required Software
- **Node.js**: v18.x or higher ([Download](https://nodejs.org/))
- **Python**: 3.9 or higher ([Download](https://www.python.org/))
- **Docker**: 20.10.x or higher ([Download](https://www.docker.com/))
- **Docker Compose**: v2.x or higher
- **Git**: Latest version

### Optional (for local development)
- **MongoDB**: 5.0+
- **PostgreSQL**: 14.x+
- **Redis**: 6.2+
- **CUDA Toolkit**: 11.x+ (for GPU acceleration in AI/ML service)

## 🚀 Quick Start (Docker - Recommended)

###  Step 1: Clone the Repository
```bash
git clone https://github.com/computeradd/indian-states-exam-system.git
cd indian-states-exam-system
```

### Step 2: Configure Environment Variables
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your configuration
nano .env
```

### Step 3: Start All Services
```bash
# Start all services with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Check service status
docker-compose ps
```

### Step 4: Initialize Database
```bash
# Run database migrations
docker-compose exec api-gateway npm run migrate

# Seed initial data
docker-compose exec api-gateway npm run seed
```

### Step 5: Access the Application
- **Web Application**: http://localhost:3000
- **Admin Dashboard**: http://localhost:3001
- **API Gateway**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/v1/docs
- **Grafana (Monitoring)**: http://localhost:3002 (admin/admin)
- **Kibana (Logs)**: http://localhost:5601

## 🔧 Manual Setup (Development)

### Backend Services Setup

#### 1. API Gateway
```bash
cd backend/api-gateway
npm install
cp .env.example .env
# Edit .env with your configuration
npm run dev
```

#### 2. User Service
```bash
cd backend/microservices/user-service
npm install
cp .env.example .env
npm run dev
```

#### 3. Examination Service
```bash
cd backend/microservices/examination-service
npm install
cp .env.example .env
npm run dev
```

#### 4. AI/ML Service
```bash
cd backend/microservices/ai-ml-service
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/app.py
```

#### 5. Proctoring Service
```bash
cd backend/microservices/proctoring-service
npm install
npm run dev
```

#### 6. Analytics Service
```bash
cd backend/microservices/analytics-service
npm install
npm run dev
```

#### 7. Notification Service
```bash
cd backend/microservices/notification-service
npm install
npm run dev
```

#### 8. Payment Service
```bash
cd backend/microservices/payment-service
npm install
npm run dev
```

#### 9. Blockchain Service
```bash
cd backend/microservices/blockchain-service
npm install
npm run dev
```

### Frontend Setup

#### Web Application
```bash
cd frontend/web-app
npm install
cp .env.example .env
# Edit .env
npm start
```

#### Admin Dashboard
```bash
cd frontend/admin-dashboard
npm install
cp .env.example .env
npm start
```

### Mobile App Setup

#### React Native
```bash
cd mobile/react-native
npm install

# For Android
npx react-native run-android

# For iOS (macOS only)
cd ios && pod install && cd ..
npx react-native run-ios
```

#### Android (Native)
```bash
cd mobile/android
./gradlew assembleDebug
```

#### iOS (Native)
```bash
cd mobile/ios
pod install
open ComputerAddExam.xcworkspace
```

## 🗄️ Database Setup

### MongoDB
```bash
# Connect to MongoDB
mongosh "mongodb://localhost:27017/exam_system"

# Create indexes
use exam_system
db.users.createIndex({ email: 1 })
db.exams.createIndex({ code: 1 })
db.questions.createIndex({ "stateInfo.relatedState": 1 })
```

### PostgreSQL
```bash
# Connect to PostgreSQL
psql -U examuser -d exam_analytics

# Run migrations
\i backend/databases/postgresql/migrations/001_create_tables.sql
```

### Redis
```bash
# Test Redis connection
redis-cli ping
```

## 🔐 Security Configuration

### 1. Generate JWT Secret
```bash
# Generate a secure random secret
node -e "console.log(require('crypto').randomBytes(64).toString('hex'))"
```

### 2. Configure SSL/TLS (Production)
```bash
# Generate self-signed certificate (for development)
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

### 3. Set Up Firewall Rules
```bash
# Example: Allow only necessary ports
sudo ufw allow 22    # SSH
sudo ufw allow 80    # HTTP
sudo ufw allow 443   # HTTPS
sudo ufw enable
```

## 🧪 Testing

### Run All Tests
```bash
# Backend tests
cd backend/api-gateway
npm test

# Frontend tests
cd frontend/web-app
npm test

# E2E tests
cd testing/e2e-tests
npm run test:e2e
```

### Load Testing
```bash
cd testing/load-tests
npm install
npm run load-test
```

## 📊 Monitoring Setup

### Prometheus
```bash
# Start Prometheus
docker-compose up -d prometheus

# Access Prometheus UI
open http://localhost:9090
```

### Grafana
```bash
# Start Grafana
docker-compose up -d grafana

# Import dashboards
# Navigate to http://localhost:3002
# Login: admin/admin
# Import dashboards from devops/monitoring/grafana/dashboards/
```

### ELK Stack
```bash
# Start ELK
docker-compose up -d elasticsearch logstash kibana

# Configure Kibana
open http://localhost:5601
```

## 🚢 Kubernetes Deployment

### Prerequisites
- Kubernetes cluster (v1.25+)
- kubectl configured
- Helm 3.x

### Deploy to Kubernetes
```bash
# Create namespace
kubectl create namespace exam-system

# Apply configurations
kubectl apply -f kubernetes/namespaces/production.yaml
kubectl apply -f kubernetes/configmaps/
kubectl apply -f kubernetes/secrets/
kubectl apply -f kubernetes/deployments/
kubectl apply -f kubernetes/services/
kubectl apply -f kubernetes/ingress/

# Check deployment status
kubectl get pods -n exam-system
kubectl get services -n exam-system
```

### Using Helm
```bash
# Install with Helm
helm install exam-system ./helm-charts/exam-system \
  --namespace exam-system \
  --values helm-charts/exam-system/values.yaml
```

## 🌐 Domain Configuration

### 1. Update DNS Records
```
# Add A records for your domain
A     api.yourdomain.com      → YOUR_SERVER_IP
A     app.yourdomain.com      → YOUR_SERVER_IP
A     admin.yourdomain.com    → YOUR_SERVER_IP
```

### 2. Configure SSL Certificate
```bash
# Using Let's Encrypt
sudo certbot --nginx -d api.yourdomain.com -d app.yourdomain.com
```

## 🔄 CI/CD Setup

### GitHub Actions
```bash
# Secrets to configure in GitHub:
# - DOCKER_USERNAME
# - DOCKER_PASSWORD
# - KUBE_CONFIG
# - AWS_ACCESS_KEY_ID (if using AWS)
# - AWS_SECRET_ACCESS_KEY
```

### Jenkins
```bash
# Install Jenkins plugins:
# - Docker Pipeline
# - Kubernetes Continuous Deploy
# - GitHub Integration
```

## 📱 Mobile App Distribution

### Android
```bash
# Generate release APK
cd mobile/android
./gradlew assembleRelease

# Sign APK
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 \
  -keystore my-release-key.keystore \
  app/build/outputs/apk/release/app-release-unsigned.apk \
  alias_name
```

### iOS
```bash
# Archive app
xcodebuild -workspace ComputerAddExam.xcworkspace \
  -scheme ComputerAddExam \
  -archivePath build/ComputerAddExam.xcarchive \
  archive
```

## 🐛 Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Find process using port
lsof -i :8000
# Kill process
kill -9 <PID>
```

#### Docker Compose Issues
```bash
# Remove all containers and volumes
docker-compose down -v
# Rebuild images
docker-compose build --no-cache
# Start fresh
docker-compose up -d
```

#### Database Connection Failed
```bash
# Check if database is running
docker-compose ps mongodb postgresql redis

# Check logs
docker-compose logs mongodb
```

#### AI/ML Service GPU Issues
```bash
# Check CUDA availability
python -c "import torch; print(torch.cuda.is_available())"

# Check NVIDIA drivers
nvidia-smi
```

## 📚 Additional Resources

- [API Documentation](docs/API_Documentation.md)
- [Architecture Guide](docs/Architecture_Guide.md)
- [Deployment Guide](docs/Deployment_Guide.md)
- [User Manual](docs/User_Manual.md)

## 💡 Tips

1. **Use Docker for development** - It's the easiest way to get started
2. **Monitor logs** - Use `docker-compose logs -f service-name`
3. **Backup databases** - Run `./scripts/backup.sh` regularly
4. **Update regularly** - Keep dependencies updated
5. **Test before deploying** - Always test in staging environment

## 🆘 Support

- **Email**: support@computeradd.com
- **Documentation**: https://docs.computeradd.com
- **GitHub Issues**: https://github.com/computeradd/indian-states-exam-system/issues
- **Community Forum**: https://community.computeradd.com

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
