# Deployment Guide

## Prerequisites
- Docker & Docker Compose
- Kubernetes cluster
- Domain name

## Steps

1. **Clone Repository**
```bash
git clone <repo-url>
cd ComputerAdd-Indian-States-Examination-System
```

2. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your values
```

3. **Deploy with Docker Compose**
```bash
docker-compose up -d
```

4. **Deploy to Kubernetes**
```bash
kubectl apply -f kubernetes/
```

## Monitoring
- Grafana: http://your-domain:3002
- Prometheus: http://your-domain:9090
