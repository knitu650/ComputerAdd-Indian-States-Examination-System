const express = require('express');
const router = express.Router();
const { createProxyMiddleware } = require('http-proxy-middleware');

// Health check
router.get('/health', (req, res) => {
  res.json({ 
    success: true, 
    message: 'API Gateway is healthy',
    timestamp: new Date()
  });
});

// User service routes
router.use('/auth', createProxyMiddleware({
  target: 'http://user-service:3001',
  pathRewrite: { '^/api/v1/auth': '/api/v1/auth' },
  changeOrigin: true
}));

router.use('/profile', createProxyMiddleware({
  target: 'http://user-service:3001',
  pathRewrite: { '^/api/v1/profile': '/api/v1/profile' },
  changeOrigin: true
}));

// Examination service routes
router.use('/exams', createProxyMiddleware({
  target: 'http://examination-service:3002',
  pathRewrite: { '^/api/v1/exams': '/api/v1/exams' },
  changeOrigin: true
}));

// AI/ML service routes
router.use('/ai', createProxyMiddleware({
  target: 'http://ai-ml-service:5000',
  pathRewrite: { '^/api/v1/ai': '/api/v1' },
  changeOrigin: true
}));

// Proctoring service routes
router.use('/proctoring', createProxyMiddleware({
  target: 'http://proctoring-service:3003',
  pathRewrite: { '^/api/v1/proctoring': '/api/v1/monitoring' },
  changeOrigin: true
}));

// Analytics service routes
router.use('/analytics', createProxyMiddleware({
  target: 'http://analytics-service:3004',
  pathRewrite: { '^/api/v1/analytics': '/api/v1/analytics' },
  changeOrigin: true
}));

// Notification service routes
router.use('/notifications', createProxyMiddleware({
  target: 'http://notification-service:3005',
  pathRewrite: { '^/api/v1/notifications': '/api/v1/notifications' },
  changeOrigin: true
}));

// Payment service routes
router.use('/payments', createProxyMiddleware({
  target: 'http://payment-service:3006',
  pathRewrite: { '^/api/v1/payments': '/api/v1/payments' },
  changeOrigin: true
}));

module.exports = router;
