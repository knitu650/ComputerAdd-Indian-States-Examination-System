# API Documentation

This document provides a detailed overview of the APIs for the Indian States Examination System.

## 1. Authentication API

### Endpoints

- `POST /api/auth/register`: Register a new user.
- `POST /api/auth/login`: Authenticate a user and receive a JWT.
- `POST /api/auth/refresh-token`: Refresh an expired JWT.

## 2. Examination API

### Endpoints

- `GET /api/exams`: Get a list of available exams.
- `GET /api/exams/:id`: Get details for a specific exam.
- `POST /api/exams/:id/start`: Start an exam session.
- `POST /api/exams/:id/submit`: Submit answers for an exam.
- `GET /api/exams/results/:id`: Get the results for a completed exam.

## 3. User Profile API

### Endpoints

- `GET /api/profile`: Get the profile of the currently authenticated user.
- `PUT /api/profile`: Update the profile of the currently authenticated user.

## 4. AI/ML API

### Endpoints

- `POST /api/proctoring/analyze`: Analyze a video frame for proctoring violations.
- `GET /api/analytics/performance`: Get performance analytics for a user.