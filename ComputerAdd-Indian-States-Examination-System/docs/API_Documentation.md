# API Documentation - Indian States Examination System

## Base URL
```
Production: https://api.exam-system.com/api/v1
Development: http://localhost:8000/api/v1
```

## Authentication

All authenticated endpoints require a Bearer token in the Authorization header:
```
Authorization: Bearer <your_jwt_token>
```

## Authentication Endpoints

### Register User
```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "profile": {
    "firstName": "John",
    "lastName": "Doe",
    "dateOfBirth": "1995-01-15",
    "gender": "male",
    "phoneNumber": "9876543210",
    "address": {
      "city": "Mumbai",
      "state": "Maharashtra",
      "pincode": "400001"
    }
  }
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "User registered successfully",
  "data": {
    "userId": "60d5ec49f1b2c8b1f8e4c1a1",
    "email": "user@example.com",
    "verificationEmailSent": true
  },
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Login
```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "user": {
      "id": "60d5ec49f1b2c8b1f8e4c1a1",
      "email": "user@example.com",
      "fullName": "John Doe",
      "role": "student"
    },
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

## Examination Endpoints

### Get All Exams
```http
GET /exams?status=active&category=indian-states&page=1&limit=10
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "exams": [
      {
        "id": "60d5ec49f1b2c8b1f8e4c1a2",
        "title": "Indian States Geography Quiz",
        "code": "ISG001",
        "type": "practice",
        "category": "geography",
        "difficulty": "intermediate",
        "duration": 60,
        "totalQuestions": 50,
        "totalMarks": 100,
        "schedule": {
          "startDate": "2025-10-01T00:00:00Z",
          "endDate": "2025-10-31T23:59:59Z"
        },
        "isActive": true
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 45,
      "pages": 5
    }
  }
}
```

### Start Exam
```http
POST /exams/:examId/start
Authorization: Bearer <token>
Content-Type: application/json

{
  "language": "en",
  "deviceInfo": {
    "deviceType": "web",
    "browser": "Chrome",
    "os": "Windows"
  }
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Exam started successfully",
  "data": {
    "examSessionId": "60d5ec49f1b2c8b1f8e4c1a3",
    "exam": {
      "id": "60d5ec49f1b2c8b1f8e4c1a2",
      "title": "Indian States Geography Quiz",
      "duration": 60,
      "totalQuestions": 50
    },
    "startTime": "2025-10-05T10:00:00Z",
    "endTime": "2025-10-05T11:00:00Z",
    "currentQuestion": 1
  }
}
```

### Submit Answer
```http
POST /exams/:examId/questions/:questionId/answer
Authorization: Bearer <token>
Content-Type: application/json

{
  "answer": "Karnataka",
  "timeTaken": 45,
  "flagged": false
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Answer submitted successfully",
  "data": {
    "questionId": "60d5ec49f1b2c8b1f8e4c1a4",
    "answerSaved": true,
    "nextQuestion": 2
  }
}
```

### Submit Exam
```http
POST /exams/:examId/submit
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Exam submitted successfully",
  "data": {
    "resultId": "60d5ec49f1b2c8b1f8e4c1a5",
    "score": 85,
    "totalMarks": 100,
    "percentage": 85,
    "passed": true,
    "rank": 42,
    "timeTaken": 3540
  }
}
```

## Question Endpoints

### Get Question
```http
GET /questions/:questionId
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": "60d5ec49f1b2c8b1f8e4c1a6",
    "questionText": "What is the capital of Karnataka?",
    "questionType": "mcq",
    "options": [
      { "text": "Bengaluru", "order": 1 },
      { "text": "Mysuru", "order": 2 },
      { "text": "Hubballi", "order": 3 },
      { "text": "Mangaluru", "order": 4 }
    ],
    "marks": 2,
    "difficulty": "easy",
    "stateInfo": {
      "relatedState": "Karnataka",
      "category": "geography"
    },
    "media": {
      "imageUrl": "https://cdn.exam-system.com/maps/karnataka.png"
    }
  }
}
```

## Results Endpoints

### Get Result
```http
GET /results/:resultId
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": "60d5ec49f1b2c8b1f8e4c1a5",
    "examId": "60d5ec49f1b2c8b1f8e4c1a2",
    "userId": "60d5ec49f1b2c8b1f8e4c1a1",
    "score": 85,
    "totalMarks": 100,
    "percentage": 85,
    "passed": true,
    "rank": 42,
    "totalParticipants": 500,
    "timeTaken": 3540,
    "answers": [
      {
        "questionId": "60d5ec49f1b2c8b1f8e4c1a6",
        "userAnswer": "Bengaluru",
        "correctAnswer": "Bengaluru",
        "isCorrect": true,
        "marksAwarded": 2,
        "timeTaken": 45
      }
    ],
    "stateWisePerformance": [
      {
        "state": "Karnataka",
        "questionsAttempted": 5,
        "correctAnswers": 4,
        "accuracy": 80
      }
    ],
    "certificateUrl": "https://cdn.exam-system.com/certificates/abc123.pdf",
    "completedAt": "2025-10-05T11:00:00Z"
  }
}
```

## Proctoring Endpoints

### Upload Proctoring Frame
```http
POST /proctoring/exams/:examId/frames
Authorization: Bearer <token>
Content-Type: multipart/form-data

{
  "frame": <image_file>,
  "timestamp": "2025-10-05T10:30:00Z",
  "metadata": {
    "deviceId": "device123",
    "sessionId": "session456"
  }
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "frameId": "60d5ec49f1b2c8b1f8e4c1a7",
    "analysis": {
      "faceDetected": true,
      "multipleFaces": false,
      "phoneDetected": false,
      "violations": []
    },
    "processed": true
  }
}
```

## Analytics Endpoints

### Get Dashboard Analytics
```http
GET /analytics/dashboard
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "totalExams": 15,
    "totalExamsTaken": 120,
    "averageScore": 78.5,
    "totalStudyTime": 3600,
    "recentActivity": [
      {
        "type": "exam_completed",
        "examTitle": "Indian States Geography Quiz",
        "score": 85,
        "date": "2025-10-05T11:00:00Z"
      }
    ],
    "upcomingExams": [
      {
        "examId": "60d5ec49f1b2c8b1f8e4c1a8",
        "title": "History of Indian States",
        "startDate": "2025-10-10T10:00:00Z"
      }
    ],
    "stateWiseProgress": [
      {
        "state": "Karnataka",
        "accuracy": 85,
        "questionsAttempted": 50
      }
    ]
  }
}
```

## Indian States Content Endpoints

### Get All States
```http
GET /states
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "states": [
      {
        "name": "Karnataka",
        "capital": "Bengaluru",
        "population": 61095297,
        "area": 191791,
        "language": "Kannada",
        "established": "1956-11-01",
        "geography": {
          "coastline": 320,
          "highestPoint": "Mullayanagiri (1930m)"
        },
        "imageUrl": "https://cdn.exam-system.com/states/karnataka.jpg"
      }
    ]
  }
}
```

## Payment Endpoints

### Create Payment Order
```http
POST /payments/create-order
Authorization: Bearer <token>
Content-Type: application/json

{
  "amount": 499,
  "currency": "INR",
  "examId": "60d5ec49f1b2c8b1f8e4c1a2",
  "description": "Exam Registration Fee"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "orderId": "order_123456789",
    "amount": 499,
    "currency": "INR",
    "razorpayOrderId": "order_KJH7sdfSDFHsdf"
  }
}
```

## Error Responses

### 400 Bad Request
```json
{
  "success": false,
  "message": "Validation error",
  "error": "VALIDATION_ERROR",
  "details": [
    {
      "field": "email",
      "message": "Email is required"
    }
  ]
}
```

### 401 Unauthorized
```json
{
  "success": false,
  "message": "Authentication required",
  "error": "UNAUTHORIZED"
}
```

### 403 Forbidden
```json
{
  "success": false,
  "message": "Insufficient permissions",
  "error": "FORBIDDEN"
}
```

### 404 Not Found
```json
{
  "success": false,
  "message": "Resource not found",
  "error": "NOT_FOUND"
}
```

### 429 Too Many Requests
```json
{
  "success": false,
  "message": "Rate limit exceeded",
  "error": "RATE_LIMIT_EXCEEDED",
  "retryAfter": "2025-10-05T10:35:00Z"
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "message": "Internal server error",
  "error": "INTERNAL_ERROR"
}
```

## Rate Limits

| Endpoint Type | Rate Limit |
|--------------|------------|
| Authentication | 5 requests per 15 minutes |
| Exam APIs | 100 requests per 15 minutes |
| Proctoring | 10 frames per second |
| General APIs | 100 requests per 15 minutes |

## WebSocket Events

### Connect to Proctoring Socket
```javascript
const socket = io('wss://api.exam-system.com/proctoring', {
  auth: {
    token: 'Bearer <jwt_token>'
  }
});

// Join exam room
socket.emit('join-exam', {
  examId: '60d5ec49f1b2c8b1f8e4c1a2',
  sessionId: '60d5ec49f1b2c8b1f8e4c1a3'
});

// Receive violation alerts
socket.on('violation-detected', (data) => {
  console.log('Violation:', data);
});

// Receive exam updates
socket.on('exam-update', (data) => {
  console.log('Update:', data);
});
```

## SDKs and Libraries

### JavaScript/TypeScript
```bash
npm install @exam-system/sdk
```

### Python
```bash
pip install exam-system-sdk
```

### Mobile (React Native)
```bash
npm install @exam-system/react-native-sdk
```

## Support

For API support, contact:
- Email: api-support@exam-system.com
- Documentation: https://docs.exam-system.com
- Status Page: https://status.exam-system.com
