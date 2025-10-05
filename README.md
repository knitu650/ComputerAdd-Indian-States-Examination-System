# ComputerAdd-Indian-States-Examination-System

An online examination system focused on Indian states, designed with a microservices architecture. This project includes features like AI-based proctoring, adaptive testing, and detailed analytics.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This system is designed to provide a comprehensive platform for conducting examinations related to Indian states. It includes a student-facing web and mobile app for taking exams, and an admin dashboard for managing content, users, and monitoring examinations. The architecture is built using microservices to ensure scalability and maintainability.

## Features

- **User Authentication**: Secure login and registration for students and administrators.
- **Examination Module**: Create, manage, and conduct exams with various question types.
- **AI/ML Proctoring**: Computer vision-based monitoring to prevent cheating.
- **Adaptive Testing**: Adjusts question difficulty based on student performance.
- **Detailed Analytics**: In-depth analysis of student performance and state-wise trends.
- **Multi-language Support**: Content available in multiple Indian languages.
- **Blockchain-based Certificates**: Secure and verifiable certificates issued on a blockchain.

## Architecture

The system is based on a microservices architecture, with services for:
- **API Gateway**: The single entry point for all client requests.
- **User Service**: Manages user data and authentication.
- **Examination Service**: Handles all logic related to exams, questions, and results.
- **AI/ML Service**: Provides AI-powered features like proctoring and adaptive testing.
- **Proctoring Service**: Manages real-time proctoring sessions.
- **Analytics Service**: Aggregates and analyzes data for reporting.
- **Notification Service**: Sends emails, SMS, and push notifications.
- **Payment Service**: Manages subscriptions and payments.
- **Blockchain Service**: Issues and verifies certificates.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Node.js
- Python

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ComputerAdd-Indian-States-Examination-System.git
   cd ComputerAdd-Indian-States-Examination-System
   ```

2. **Run the setup script:**
   ```bash
   ./scripts/setup.sh
   ```

3. **Start the application:**
   ```bash
   docker-compose up -d
   ```

## Technology Stack

- **Backend**: Node.js, Python, Express, Flask
- **Frontend**: React, Redux
- **Mobile**: React Native
- **Databases**: MongoDB, PostgreSQL, Redis
- **AI/ML**: TensorFlow, PyTorch, OpenCV
- **DevOps**: Docker, Kubernetes, Terraform, Jenkins, Prometheus, Grafana
- **Blockchain**: Solidity, Web3.js

## Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.