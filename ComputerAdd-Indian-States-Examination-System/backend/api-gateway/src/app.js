const express = require('express');
const helmet = require('helmet');
const compression = require('compression');
const cookieParser = require('cookie-parser');
const morgan = require('morgan');
const { createProxyMiddleware } = require('http-proxy-middleware');
require('dotenv').config();

const { corsMiddleware, securityHeaders, corsErrorHandler } = require('./middleware/cors.middleware');
const { generalLimiter } = require('./middleware/rate-limiter.middleware');
const { logger, morganStream } = require('./utils/logger');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 8000;

// ==================== Basic Middleware ====================

// Security headers
app.use(helmet());
app.use(securityHeaders);

// CORS
app.use(corsMiddleware);

// Body parsing
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));
app.use(cookieParser());

// Compression
app.use(compression());

// Logging
app.use(morgan('combined', { stream: morganStream }));

// Rate limiting
app.use(generalLimiter);

// Request ID
app.use((req, res, next) => {
  req.id = require('uuid').v4();
  res.setHeader('X-Request-ID', req.id);
  next();
});

// ==================== Health Check ====================

app.get('/health', (req, res) => {
  res.status(200).json({
    success: true,
    message: 'API Gateway is healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    environment: process.env.NODE_ENV
  });
});

app.get('/api/v1/health', (req, res) => {
  res.status(200).json({
    success: true,
    services: {
      apiGateway: 'healthy',
      timestamp: new Date().toISOString()
    }
  });
});

// ==================== Service Proxies ====================

// User Service
app.use('/api/v1/users', createProxyMiddleware({
  target: process.env.USER_SERVICE_URL || 'http://localhost:3001',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/users': '/api/v1/users'
  },
  onError: (err, req, res) => {
    logger.error('User service proxy error:', err);
    res.status(503).json({
      success: false,
      message: 'User service unavailable',
      error: 'SERVICE_UNAVAILABLE'
    });
  }
}));

app.use('/api/v1/auth', createProxyMiddleware({
  target: process.env.USER_SERVICE_URL || 'http://localhost:3001',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/auth': '/api/v1/auth'
  }
}));

// Examination Service
app.use('/api/v1/exams', createProxyMiddleware({
  target: process.env.EXAM_SERVICE_URL || 'http://localhost:3002',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/exams': '/api/v1/exams'
  },
  onError: (err, req, res) => {
    logger.error('Exam service proxy error:', err);
    res.status(503).json({
      success: false,
      message: 'Examination service unavailable',
      error: 'SERVICE_UNAVAILABLE'
    });
  }
}));

app.use('/api/v1/questions', createProxyMiddleware({
  target: process.env.EXAM_SERVICE_URL || 'http://localhost:3002',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/questions': '/api/v1/questions'
  }
}));

app.use('/api/v1/results', createProxyMiddleware({
  target: process.env.EXAM_SERVICE_URL || 'http://localhost:3002',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/results': '/api/v1/results'
  }
}));

// AI/ML Service
app.use('/api/v1/ai', createProxyMiddleware({
  target: process.env.AI_ML_SERVICE_URL || 'http://localhost:5000',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/ai': '/api/v1'
  },
  onError: (err, req, res) => {
    logger.error('AI/ML service proxy error:', err);
    res.status(503).json({
      success: false,
      message: 'AI/ML service unavailable',
      error: 'SERVICE_UNAVAILABLE'
    });
  }
}));

// Proctoring Service
app.use('/api/v1/proctoring', createProxyMiddleware({
  target: process.env.PROCTORING_SERVICE_URL || 'http://localhost:3003',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/proctoring': '/api/v1/proctoring'
  },
  ws: true, // Enable WebSocket proxying
  onError: (err, req, res) => {
    logger.error('Proctoring service proxy error:', err);
    res.status(503).json({
      success: false,
      message: 'Proctoring service unavailable',
      error: 'SERVICE_UNAVAILABLE'
    });
  }
}));

// Analytics Service
app.use('/api/v1/analytics', createProxyMiddleware({
  target: process.env.ANALYTICS_SERVICE_URL || 'http://localhost:3004',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/analytics': '/api/v1/analytics'
  },
  onError: (err, req, res) => {
    logger.error('Analytics service proxy error:', err);
    res.status(503).json({
      success: false,
      message: 'Analytics service unavailable',
      error: 'SERVICE_UNAVAILABLE'
    });
  }
}));

// Notification Service
app.use('/api/v1/notifications', createProxyMiddleware({
  target: process.env.NOTIFICATION_SERVICE_URL || 'http://localhost:3005',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/notifications': '/api/v1/notifications'
  },
  onError: (err, req, res) => {
    logger.error('Notification service proxy error:', err);
    res.status(503).json({
      success: false,
      message: 'Notification service unavailable',
      error: 'SERVICE_UNAVAILABLE'
    });
  }
}));

// Payment Service
app.use('/api/v1/payments', createProxyMiddleware({
  target: process.env.PAYMENT_SERVICE_URL || 'http://localhost:3006',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/payments': '/api/v1/payments'
  },
  onError: (err, req, res) => {
    logger.error('Payment service proxy error:', err);
    res.status(503).json({
      success: false,
      message: 'Payment service unavailable',
      error: 'SERVICE_UNAVAILABLE'
    });
  }
}));

// Blockchain Service
app.use('/api/v1/blockchain', createProxyMiddleware({
  target: process.env.BLOCKCHAIN_SERVICE_URL || 'http://localhost:3007',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/blockchain': '/api/v1/blockchain'
  },
  onError: (err, req, res) => {
    logger.error('Blockchain service proxy error:', err);
    res.status(503).json({
      success: false,
      message: 'Blockchain service unavailable',
      error: 'SERVICE_UNAVAILABLE'
    });
  }
}));

// Indian States Content Service
app.use('/api/v1/states', createProxyMiddleware({
  target: process.env.EXAM_SERVICE_URL || 'http://localhost:3002',
  changeOrigin: true,
  pathRewrite: {
    '^/api/v1/states': '/api/v1/states'
  }
}));

// ==================== API Documentation ====================

app.get('/api/v1/docs', (req, res) => {
  res.json({
    success: true,
    name: 'Indian States Examination System API',
    version: '1.0.0',
    endpoints: {
      auth: '/api/v1/auth',
      users: '/api/v1/users',
      exams: '/api/v1/exams',
      questions: '/api/v1/questions',
      results: '/api/v1/results',
      proctoring: '/api/v1/proctoring',
      analytics: '/api/v1/analytics',
      notifications: '/api/v1/notifications',
      payments: '/api/v1/payments',
      blockchain: '/api/v1/blockchain',
      states: '/api/v1/states',
      ai: '/api/v1/ai'
    },
    documentation: '/api/v1/docs/swagger'
  });
});

// ==================== Error Handling ====================

// CORS error handler
app.use(corsErrorHandler);

// 404 handler
app.use((req, res) => {
  logger.warn('404 Not Found', {
    method: req.method,
    path: req.path,
    ip: req.ip
  });

  res.status(404).json({
    success: false,
    message: 'Endpoint not found',
    error: 'NOT_FOUND',
    path: req.path
  });
});

// Global error handler
app.use((err, req, res, next) => {
  logger.error('Unhandled error:', {
    error: err.message,
    stack: err.stack,
    path: req.path,
    method: req.method
  });

  res.status(err.status || 500).json({
    success: false,
    message: err.message || 'Internal server error',
    error: err.name || 'INTERNAL_ERROR',
    ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
  });
});

// ==================== Server Startup ====================

const server = app.listen(PORT, () => {
  logger.info(`🚀 API Gateway started on port ${PORT}`);
  logger.info(`📝 Environment: ${process.env.NODE_ENV}`);
  logger.info(`🌐 Health check: http://localhost:${PORT}/health`);
  logger.info(`📖 API Docs: http://localhost:${PORT}/api/v1/docs`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  logger.info('SIGTERM received, closing server gracefully');
  
  server.close(() => {
    logger.info('Server closed');
    process.exit(0);
  });

  // Force close after 30 seconds
  setTimeout(() => {
    logger.error('Forced shutdown after timeout');
    process.exit(1);
  }, 30000);
});

process.on('SIGINT', () => {
  logger.info('SIGINT received, closing server gracefully');
  server.close(() => {
    logger.info('Server closed');
    process.exit(0);
  });
});

// Handle uncaught exceptions
process.on('uncaughtException', (err) => {
  logger.error('Uncaught Exception:', err);
  process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
  logger.error('Unhandled Rejection:', {
    reason,
    promise
  });
});

module.exports = app;
