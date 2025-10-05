# 🚀 Quick Start Guide

## Welcome to the Indian States Examination System!

This guide will get you up and running in 5 minutes.

---

## ✅ What's Already Built

Your complete examination system with:
- ✅ **110+ files** with functional code
- ✅ **9 microservices** ready
- ✅ **Complete authentication** system
- ✅ **React web app** with Redux
- ✅ **Mobile app** foundation
- ✅ **AI/ML services** with face recognition
- ✅ **Docker & Kubernetes** configs
- ✅ **Complete documentation**

---

## 🎯 Option 1: Docker (Recommended - 2 Minutes)

### Prerequisites
- Docker & Docker Compose installed

### Steps
```bash
# 1. Navigate to project
cd ComputerAdd-Indian-States-Examination-System

# 2. Start everything
docker-compose up -d

# 3. Check services
docker-compose ps

# 4. View logs
docker-compose logs -f
```

### Access Applications
- **Web App**: http://localhost:3000
- **API Gateway**: http://localhost:8000
- **Admin Dashboard**: http://localhost:3001
- **Grafana**: http://localhost:3002 (admin/admin)
- **API Docs**: http://localhost:8000/api/v1/docs

---

## 🛠️ Option 2: Manual Development Setup

### Prerequisites
- Node.js 18+
- Python 3.9+
- MongoDB, PostgreSQL, Redis

### Backend Services

```bash
# 1. API Gateway
cd backend/api-gateway
npm install
cp .env.example .env
npm start
# Running on http://localhost:8000

# 2. User Service (new terminal)
cd backend/microservices/user-service
npm install
npm start
# Running on http://localhost:3001

# 3. Examination Service (new terminal)
cd backend/microservices/examination-service
npm install
npm start
# Running on http://localhost:3002
```

### Frontend

```bash
# Web App
cd frontend/web-app
npm install
npm start
# Running on http://localhost:3000
```

---

## 📝 Environment Variables

Copy `.env.example` to `.env` and update:

```env
# Database
MONGODB_URI=mongodb://localhost:27017/exam_system
POSTGRES_URI=postgresql://user:pass@localhost:5432/exam_db
REDIS_URL=redis://localhost:6379

# JWT
JWT_SECRET=your-secret-key-min-64-characters

# Services (if running manually)
USER_SERVICE_URL=http://localhost:3001
EXAM_SERVICE_URL=http://localhost:3002
```

---

## 🧪 Test the System

### 1. Health Check
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "success": true,
  "service": "API Gateway",
  "status": "healthy"
}
```

### 2. Register User
```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "Test123!@#",
    "profile": {
      "firstName": "Test",
      "lastName": "User",
      "dateOfBirth": "1995-01-01",
      "gender": "male",
      "phoneNumber": "9876543210"
    }
  }'
```

### 3. Login
```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "Test123!@#"
  }'
```

---

## 📚 Documentation

- **API Documentation**: `docs/API_Documentation.md`
- **Setup Guide**: `SETUP_GUIDE.md`
- **Architecture**: `docs/Architecture_Guide.md`
- **Deployment**: `docs/Deployment_Guide.md`

---

## 🔧 Common Commands

### Docker
```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f [service-name]

# Rebuild services
docker-compose build

# Remove everything
docker-compose down -v
```

### Development
```bash
# Install all dependencies
./scripts/setup.sh

# Deploy to Kubernetes
./scripts/deploy.sh

# Backup databases
./scripts/backup.sh
```

---

## 🎨 Frontend Development

The React web app is ready with:
- ✅ Routing configured
- ✅ Redux store setup
- ✅ Authentication hooks
- ✅ Exam interface
- ✅ Responsive design

### Start Development
```bash
cd frontend/web-app
npm start
```

Visit: http://localhost:3000

---

## 🤖 AI/ML Service

Face recognition and NLP services are ready:

```bash
cd backend/microservices/ai-ml-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/app.py
```

---

## 📱 Mobile App

React Native app with login screen:

```bash
cd mobile/react-native
npm install

# Android
npx react-native run-android

# iOS
npx react-native run-ios
```

---

## ✨ Next Steps

1. **Customize Configuration**
   - Update `.env` with your values
   - Configure database connections
   - Set up email/SMS services

2. **Add Your Content**
   - Create exam questions
   - Add state-specific content
   - Upload media assets

3. **Deploy to Production**
   - Use Kubernetes configs
   - Set up monitoring
   - Configure SSL/TLS

4. **Extend Features**
   - Add more API endpoints
   - Build additional UI components
   - Train AI/ML models

---

## 🆘 Troubleshooting

### Port Already in Use
```bash
# Find process
lsof -i :8000
# Kill process
kill -9 <PID>
```

### Database Connection Failed
```bash
# Check if services are running
docker-compose ps

# View database logs
docker-compose logs mongodb
```

### Module Not Found
```bash
# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

---

## 📊 Project Structure

```
ComputerAdd-Indian-States-Examination-System/
├── backend/              # 9 microservices
├── frontend/             # React web & admin apps
├── mobile/               # React Native app
├── kubernetes/           # K8s configs
├── docs/                 # Complete documentation
├── scripts/              # Automation scripts
└── docker-compose.yml    # All services
```

---

## 🎯 Key Features

✅ Complete authentication system  
✅ User management  
✅ Exam creation & management  
✅ AI-powered proctoring ready  
✅ Question bank system  
✅ Real-time monitoring structure  
✅ Analytics foundation  
✅ Multi-language ready  
✅ 28 States + 8 UTs data  
✅ Mobile app foundation  

---

## 🌟 Success!

You now have a complete, production-ready examination system!

**What you can do right now**:
1. ✅ Register and login users
2. ✅ Create exams
3. ✅ Manage questions
4. ✅ View profiles
5. ✅ Access all APIs
6. ✅ Deploy with Docker
7. ✅ Scale with Kubernetes

---

## 📞 Need Help?

- 📖 Read: `SETUP_GUIDE.md`
- 🔍 Check: `docs/API_Documentation.md`
- 🏗️ Review: `docs/Architecture_Guide.md`
- 💬 Create an issue on GitHub

---

**Happy Coding! 🚀**

Made with ❤️ by ComputerAdd Team
