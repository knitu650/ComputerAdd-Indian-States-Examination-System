#!/bin/bash
echo "🚀 Setting up Indian States Examination System..."

# Install backend dependencies
echo "📦 Installing backend dependencies..."
cd backend/api-gateway && npm install
cd ../microservices/user-service && npm install
cd ../examination-service && npm install

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd ../../frontend/web-app && npm install
cd ../admin-dashboard && npm install

# Setup AI/ML
echo "🤖 Setting up AI/ML service..."
cd ../../backend/microservices/ai-ml-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "✅ Setup complete!"
