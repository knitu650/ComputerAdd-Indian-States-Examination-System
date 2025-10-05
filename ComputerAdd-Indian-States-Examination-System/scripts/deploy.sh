#!/bin/bash
echo "🚀 Deploying services..."

# Build Docker images
docker-compose build

# Deploy to Kubernetes
kubectl apply -f kubernetes/

echo "✅ Deployment complete!"
