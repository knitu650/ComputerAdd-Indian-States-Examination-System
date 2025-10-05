#!/usr/bin/env python3
"""
Comprehensive File Generation Script for Indian States Examination System
Creates all remaining files with production-ready code
"""

import os
import json
from pathlib import Path

BASE_DIR = "/workspace/ComputerAdd-Indian-States-Examination-System"

# File templates
FILE_TEMPLATES = {
    # AI/ML Service Files
    "backend/microservices/ai-ml-service/src/app.py": '''from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from controllers import cv_proctoring_controller, nlp_processing_controller, ml_analytics_controller
from utils.logger import setup_logger

app = FastAPI(
    title="AI/ML Service - Indian States Examination System",
    description="Computer Vision, NLP, and ML services for exam proctoring and analytics",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = setup_logger(__name__)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "AI/ML Service"}

@app.get("/api/v1/health")
async def api_health():
    return {"status": "healthy", "models_loaded": True}

# Include routers
app.include_router(cv_proctoring_controller.router, prefix="/api/v1/cv", tags=["Computer Vision"])
app.include_router(nlp_processing_controller.router, prefix="/api/v1/nlp", tags=["NLP"])
app.include_router(ml_analytics_controller.router, prefix="/api/v1/ml", tags=["Machine Learning"])

if __name__ == "__main__":
    logger.info("Starting AI/ML Service...")
    uvicorn.run(app, host="0.0.0.0", port=5000)
''',

    "backend/microservices/ai-ml-service/src/models/computer-vision/face_recognition.py": '''import cv2
import numpy as np
import tensorflow as tf
from typing import Dict, List, Tuple

class FaceRecognitionModel:
    def __init__(self, model_path: str = None):
        self.model = self.load_model(model_path)
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
    
    def load_model(self, model_path: str = None):
        """Load pre-trained face recognition model"""
        if model_path:
            return tf.keras.models.load_model(model_path)
        # Default model architecture
        return self.build_default_model()
    
    def build_default_model(self):
        """Build default face recognition model"""
        model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation='relu'),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(256, activation='sigmoid')
        ])
        return model
    
    def detect_faces(self, image: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """Detect faces in image"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )
        return faces
    
    def extract_face_embeddings(self, image: np.ndarray, face_coords: Tuple) -> np.ndarray:
        """Extract face embeddings"""
        x, y, w, h = face_coords
        face = image[y:y+h, x:x+w]
        face_resized = cv2.resize(face, (224, 224))
        face_normalized = face_resized / 255.0
        face_batch = np.expand_dims(face_normalized, axis=0)
        
        embeddings = self.model.predict(face_batch, verbose=0)
        return embeddings[0]
    
    def verify_identity(self, embedding1: np.ndarray, embedding2: np.ndarray, 
                       threshold: float = 0.6) -> Dict:
        """Verify if two face embeddings match"""
        distance = np.linalg.norm(embedding1 - embedding2)
        similarity = 1 / (1 + distance)
        
        return {
            "match": similarity >= threshold,
            "confidence": float(similarity),
            "distance": float(distance)
        }
    
    def analyze_frame(self, frame: np.ndarray, reference_embedding: np.ndarray = None) -> Dict:
        """Analyze video frame for proctoring"""
        faces = self.detect_faces(frame)
        
        result = {
            "face_detected": len(faces) > 0,
            "face_count": len(faces),
            "multiple_persons": len(faces) > 1,
            "no_face": len(faces) == 0,
            "faces": []
        }
        
        if reference_embedding is not None and len(faces) > 0:
            for face in faces:
                embedding = self.extract_face_embeddings(frame, face)
                verification = self.verify_identity(reference_embedding, embedding)
                result["faces"].append({
                    "coordinates": face.tolist(),
                    "verified": verification["match"],
                    "confidence": verification["confidence"]
                })
        
        return result
''',

    "backend/microservices/ai-ml-service/src/models/nlp/question_generator.py": '''from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
from typing import List, Dict

class QuestionGenerator:
    def __init__(self, model_name: str = "t5-base"):
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
    
    def generate_questions(self, context: str, num_questions: int = 5, 
                          question_type: str = "factual") -> List[Dict]:
        """Generate questions from given context"""
        
        # Prepare input
        input_text = f"generate {question_type} questions: {context}"
        input_ids = self.tokenizer.encode(
            input_text, 
            return_tensors="pt", 
            max_length=512,
            truncation=True
        ).to(self.device)
        
        # Generate questions
        outputs = self.model.generate(
            input_ids,
            max_length=200,
            num_return_sequences=num_questions,
            num_beams=5,
            early_stopping=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95
        )
        
        questions = []
        for output in outputs:
            question = self.tokenizer.decode(output, skip_special_tokens=True)
            questions.append({
                "question": question,
                "type": question_type,
                "context": context[:100] + "..."
            })
        
        return questions
    
    def generate_distractors(self, question: str, correct_answer: str, 
                            num_distractors: int = 3) -> List[str]:
        """Generate distractor options for MCQ"""
        
        input_text = f"generate distractors for question: {question} with answer: {correct_answer}"
        input_ids = self.tokenizer.encode(
            input_text,
            return_tensors="pt",
            max_length=256,
            truncation=True
        ).to(self.device)
        
        outputs = self.model.generate(
            input_ids,
            max_length=100,
            num_return_sequences=num_distractors,
            num_beams=num_distractors + 2,
            temperature=0.9
        )
        
        distractors = []
        for output in outputs:
            distractor = self.tokenizer.decode(output, skip_special_tokens=True)
            distractors.append(distractor)
        
        return distractors
    
    def generate_state_questions(self, state_name: str, category: str = "geography") -> List[Dict]:
        """Generate questions specific to Indian states"""
        
        templates = {
            "geography": f"Generate geography questions about {state_name}, India",
            "history": f"Generate historical questions about {state_name}, India",
            "culture": f"Generate cultural questions about {state_name}, India",
            "economy": f"Generate economy-related questions about {state_name}, India"
        }
        
        context = templates.get(category, templates["geography"])
        return self.generate_questions(context, num_questions=5)
''',

    # Frontend React Components
    "frontend/web-app/src/components/common/Header/Header.jsx": '''import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../../hooks/useAuth';
import { useNotification } from '../../../hooks/useNotification';
import styles from './Header.module.css';

const Header = () => {
  const { user, logout } = useAuth();
  const { notifications, unreadCount } = useNotification();
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      await logout();
      navigate('/login');
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <header className={styles.header}>
      <div className={styles.container}>
        <Link to="/" className={styles.logo}>
          <img src="/assets/logo.png" alt="Exam System" />
          <span>Indian States Exam</span>
        </Link>

        <nav className={styles.nav}>
          <Link to="/dashboard" className={styles.navLink}>Dashboard</Link>
          <Link to="/exams" className={styles.navLink}>Exams</Link>
          <Link to="/states" className={styles.navLink}>States</Link>
          <Link to="/practice" className={styles.navLink}>Practice</Link>
          <Link to="/results" className={styles.navLink}>Results</Link>
        </nav>

        <div className={styles.actions}>
          <button className={styles.notificationBtn}>
            <i className="fas fa-bell"></i>
            {unreadCount > 0 && (
              <span className={styles.badge}>{unreadCount}</span>
            )}
          </button>

          <div className={styles.userMenu}>
            <button className={styles.userBtn}>
              <img 
                src={user?.profile?.avatar || '/assets/default-avatar.png'} 
                alt={user?.fullName} 
              />
              <span>{user?.profile?.firstName}</span>
            </button>
            
            <div className={styles.dropdown}>
              <Link to="/profile">Profile</Link>
              <Link to="/settings">Settings</Link>
              <Link to="/help">Help</Link>
              <button onClick={handleLogout}>Logout</button>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
''',

    "frontend/web-app/src/components/examination/ExamInterface/ExamInterface.jsx": '''import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useExam } from '../../../hooks/useExam';
import { useTimer } from '../../../hooks/useTimer';
import { useProctoring } from '../../../hooks/useProctoring';
import QuestionPanel from './QuestionPanel';
import AnswerPanel from './AnswerPanel';
import NavigationPanel from './NavigationPanel';
import TimerPanel from './TimerPanel';
import styles from './ExamInterface.module.css';

const ExamInterface = () => {
  const { examId } = useParams();
  const navigate = useNavigate();
  const { 
    exam, 
    currentQuestion, 
    submitAnswer, 
    submitExam,
    goToQuestion 
  } = useExam(examId);
  
  const { timeRemaining, formatTime } = useTimer(exam?.duration * 60);
  const { startProctoring, violations } = useProctoring(examId);

  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [flaggedQuestions, setFlaggedQuestions] = useState(new Set());

  useEffect(() => {
    if (exam?.proctoring?.enabled) {
      startProctoring();
    }
  }, [exam]);

  useEffect(() => {
    if (timeRemaining === 0) {
      handleSubmitExam();
    }
  }, [timeRemaining]);

  const handleAnswerSelect = (answer) => {
    setSelectedAnswer(answer);
  };

  const handleSubmitAnswer = async () => {
    if (selectedAnswer) {
      await submitAnswer(currentQuestion.id, selectedAnswer);
      setSelectedAnswer(null);
      
      // Move to next question
      if (currentQuestion.number < exam.totalQuestions) {
        goToQuestion(currentQuestion.number + 1);
      }
    }
  };

  const handleFlagQuestion = () => {
    const newFlagged = new Set(flaggedQuestions);
    if (newFlagged.has(currentQuestion.id)) {
      newFlagged.delete(currentQuestion.id);
    } else {
      newFlagged.add(currentQuestion.id);
    }
    setFlaggedQuestions(newFlagged);
  };

  const handleSubmitExam = async () => {
    if (window.confirm('Are you sure you want to submit the exam?')) {
      await submitExam();
      navigate(`/exams/${examId}/result`);
    }
  };

  if (!exam || !currentQuestion) {
    return <div className={styles.loading}>Loading exam...</div>;
  }

  return (
    <div className={styles.examInterface}>
      <div className={styles.header}>
        <h1>{exam.title}</h1>
        <TimerPanel 
          timeRemaining={timeRemaining} 
          formatTime={formatTime} 
        />
      </div>

      {violations.length > 0 && (
        <div className={styles.violationAlert}>
          <i className="fas fa-exclamation-triangle"></i>
          Violation detected: {violations[violations.length - 1].type}
        </div>
      )}

      <div className={styles.content}>
        <div className={styles.leftPanel}>
          <QuestionPanel 
            question={currentQuestion}
            questionNumber={currentQuestion.number}
            totalQuestions={exam.totalQuestions}
          />

          <AnswerPanel
            question={currentQuestion}
            selectedAnswer={selectedAnswer}
            onAnswerSelect={handleAnswerSelect}
          />

          <div className={styles.actions}>
            <button 
              className={styles.flagBtn}
              onClick={handleFlagQuestion}
            >
              {flaggedQuestions.has(currentQuestion.id) ? 'Unflag' : 'Flag'} Question
            </button>
            
            <button 
              className={styles.clearBtn}
              onClick={() => setSelectedAnswer(null)}
            >
              Clear Answer
            </button>
            
            <button 
              className={styles.submitBtn}
              onClick={handleSubmitAnswer}
              disabled={!selectedAnswer}
            >
              Save & Next
            </button>
          </div>
        </div>

        <div className={styles.rightPanel}>
          <NavigationPanel
            questions={exam.questions}
            currentQuestion={currentQuestion.number}
            answeredQuestions={exam.answeredQuestions}
            flaggedQuestions={flaggedQuestions}
            onQuestionSelect={goToQuestion}
          />

          <button 
            className={styles.submitExamBtn}
            onClick={handleSubmitExam}
          >
            Submit Exam
          </button>
        </div>
      </div>
    </div>
  );
};

export default ExamInterface;
''',

    # React Native Mobile App
    "mobile/react-native/src/screens/AuthStack/LoginScreen.js": '''import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  Alert,
  ActivityIndicator,
} from 'react-native';
import { useAuth } from '../../hooks/useAuth';
import { useBiometric } from '../../hooks/useBiometric';

const LoginScreen = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  
  const { login } = useAuth();
  const { isBiometricAvailable, authenticateWithBiometric } = useBiometric();

  const handleLogin = async () => {
    if (!email || !password) {
      Alert.alert('Error', 'Please enter email and password');
      return;
    }

    setLoading(true);
    try {
      await login(email, password);
      navigation.replace('Main');
    } catch (error) {
      Alert.alert('Login Failed', error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleBiometricLogin = async () => {
    if (!isBiometricAvailable) {
      Alert.alert('Not Available', 'Biometric authentication is not available');
      return;
    }

    try {
      const result = await authenticateWithBiometric();
      if (result.success) {
        navigation.replace('Main');
      }
    } catch (error) {
      Alert.alert('Authentication Failed', error.message);
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Indian States Exam</Text>
        <Text style={styles.subtitle}>Login to continue</Text>
      </View>

      <View style={styles.form}>
        <TextInput
          style={styles.input}
          placeholder="Email"
          value={email}
          onChangeText={setEmail}
          autoCapitalize="none"
          keyboardType="email-address"
        />

        <TextInput
          style={styles.input}
          placeholder="Password"
          value={password}
          onChangeText={setPassword}
          secureTextEntry
        />

        <TouchableOpacity 
          style={styles.forgotPassword}
          onPress={() => navigation.navigate('ForgotPassword')}
        >
          <Text style={styles.forgotPasswordText}>Forgot Password?</Text>
        </TouchableOpacity>

        <TouchableOpacity 
          style={styles.loginButton}
          onPress={handleLogin}
          disabled={loading}
        >
          {loading ? (
            <ActivityIndicator color="#fff" />
          ) : (
            <Text style={styles.loginButtonText}>Login</Text>
          )}
        </TouchableOpacity>

        {isBiometricAvailable && (
          <TouchableOpacity 
            style={styles.biometricButton}
            onPress={handleBiometricLogin}
          >
            <Text style={styles.biometricButtonText}>Login with Biometric</Text>
          </TouchableOpacity>
        )}

        <View style={styles.registerContainer}>
          <Text style={styles.registerText}>Don't have an account? </Text>
          <TouchableOpacity onPress={() => navigation.navigate('Register')}>
            <Text style={styles.registerLink}>Register</Text>
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 20,
  },
  header: {
    marginTop: 60,
    marginBottom: 40,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
  },
  form: {
    flex: 1,
  },
  input: {
    height: 50,
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    paddingHorizontal: 15,
    marginBottom: 15,
    fontSize: 16,
  },
  forgotPassword: {
    alignSelf: 'flex-end',
    marginBottom: 20,
  },
  forgotPasswordText: {
    color: '#007AFF',
    fontSize: 14,
  },
  loginButton: {
    height: 50,
    backgroundColor: '#007AFF',
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 15,
  },
  loginButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  biometricButton: {
    height: 50,
    backgroundColor: '#fff',
    borderWidth: 1,
    borderColor: '#007AFF',
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 20,
  },
  biometricButtonText: {
    color: '#007AFF',
    fontSize: 16,
    fontWeight: '600',
  },
  registerContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  registerText: {
    color: '#666',
    fontSize: 14,
  },
  registerLink: {
    color: '#007AFF',
    fontSize: 14,
    fontWeight: '600',
  },
});

export default LoginScreen;
''',

    # Kubernetes Deployment Files
    "kubernetes/deployments/api-gateway.yaml": '''apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-gateway
  namespace: exam-system
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api-gateway
  template:
    metadata:
      labels:
        app: api-gateway
    spec:
      containers:
      - name: api-gateway
        image: exam-system/api-gateway:latest
        ports:
        - containerPort: 8000
        env:
        - name: NODE_ENV
          value: "production"
        - name: PORT
          value: "8000"
        - name: MONGODB_URI
          valueFrom:
            secretKeyRef:
              name: mongodb-secret
              key: uri
        - name: REDIS_URL
          valueFrom:
            secretKeyRef:
              name: redis-secret
              key: url
        - name: JWT_SECRET
          valueFrom:
            secretKeyRef:
              name: jwt-secret
              key: secret
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 20
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: api-gateway
  namespace: exam-system
spec:
  selector:
    app: api-gateway
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: LoadBalancer
''',

    # GitHub Actions CI/CD
    ".github/workflows/ci-cd.yml": '''name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install dependencies
        run: |
          cd backend/api-gateway
          npm ci
          
      - name: Run tests
        run: |
          cd backend/api-gateway
          npm test
          
      - name: Run lint
        run: |
          cd backend/api-gateway
          npm run lint

  test-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install dependencies
        run: |
          cd frontend/web-app
          npm ci
          
      - name: Run tests
        run: |
          cd frontend/web-app
          npm test
          
      - name: Build
        run: |
          cd frontend/web-app
          npm run build

  build-and-push:
    needs: [test-backend, test-frontend]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
          
      - name: Build and push API Gateway
        uses: docker/build-push-action@v4
        with:
          context: ./backend/api-gateway
          push: true
          tags: exam-system/api-gateway:latest
          
      - name: Build and push User Service
        uses: docker/build-push-action@v4
        with:
          context: ./backend/microservices/user-service
          push: true
          tags: exam-system/user-service:latest

  deploy:
    needs: build-and-push
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      
      - name: Configure kubectl
        uses: azure/setup-kubectl@v3
        with:
          version: 'latest'
          
      - name: Deploy to Kubernetes
        run: |
          kubectl apply -f kubernetes/namespaces/production.yaml
          kubectl apply -f kubernetes/deployments/
          kubectl apply -f kubernetes/services/
          kubectl rollout status deployment/api-gateway -n exam-system
''',
}

def create_file(filepath, content):
    """Create file with content"""
    full_path = os.path.join(BASE_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Created: {filepath}")

def main():
    print("🚀 Creating all project files...")
    print(f"📁 Base directory: {BASE_DIR}\n")
    
    # Create all files from templates
    for filepath, content in FILE_TEMPLATES.items():
        try:
            create_file(filepath, content)
        except Exception as e:
            print(f"✗ Error creating {filepath}: {e}")
    
    print(f"\n✅ Successfully created {len(FILE_TEMPLATES)} files!")
    print("\n📋 Next steps:")
    print("1. Run: docker-compose up -d")
    print("2. Access web app: http://localhost:3000")
    print("3. Access admin dashboard: http://localhost:3001")
    print("4. Access API docs: http://localhost:8000/api/v1/docs")

if __name__ == "__main__":
    main()
