const cors = require('cors');
const { logger } = require('../utils/logger');

/**
 * CORS Configuration
 * Handles Cross-Origin Resource Sharing
 */

// Parse allowed origins from environment
const getAllowedOrigins = () => {
  const origins = process.env.ALLOWED_ORIGINS || 'http://localhost:3000';
  return origins.split(',').map(origin => origin.trim());
};

/**
 * Dynamic CORS Options
 * Validates origin and configures CORS dynamically
 */
const corsOptions = {
  origin: (origin, callback) => {
    const allowedOrigins = getAllowedOrigins();
    
    // Allow requests with no origin (mobile apps, Postman, etc.)
    if (!origin) {
      return callback(null, true);
    }

    // Check if origin is allowed
    if (allowedOrigins.includes(origin) || allowedOrigins.includes('*')) {
      callback(null, true);
    } else {
      logger.warn('CORS blocked request from unauthorized origin', {
        origin,
        allowedOrigins
      });
      
      callback(new Error('Not allowed by CORS'));
    }
  },
  
  // Allowed HTTP methods
  methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
  
  // Allowed headers
  allowedHeaders: [
    'Content-Type',
    'Authorization',
    'X-Requested-With',
    'X-API-Key',
    'X-Session-ID',
    'X-Exam-ID',
    'X-Device-ID',
    'X-App-Version'
  ],
  
  // Exposed headers (accessible to client)
  exposedHeaders: [
    'X-Total-Count',
    'X-Page-Count',
    'X-Current-Page',
    'X-Rate-Limit-Remaining',
    'X-Rate-Limit-Reset',
    'X-Session-Timeout'
  ],
  
  // Allow credentials (cookies, authorization headers)
  credentials: true,
  
  // Preflight cache duration (seconds)
  maxAge: 86400, // 24 hours
  
  // Success status for OPTIONS requests
  optionsSuccessStatus: 204
};

/**
 * Standard CORS Middleware
 */
const corsMiddleware = cors(corsOptions);

/**
 * Strict CORS for Exam Endpoints
 * Only allows specific origins during exams
 */
const examCorsList = process.env.EXAM_ALLOWED_ORIGINS?.split(',') || [];

const strictExamCors = cors({
  ...corsOptions,
  origin: (origin, callback) => {
    if (!origin) {
      return callback(new Error('Origin required for exam endpoints'));
    }

    if (examCorsList.includes(origin) || examCorsList.includes('*')) {
      callback(null, true);
    } else {
      logger.warn('Strict CORS blocked exam request', {
        origin,
        allowedOrigins: examCorsList
      });
      
      callback(new Error('Not allowed by exam CORS policy'));
    }
  }
});

/**
 * Public CORS for Open Endpoints
 * Allows all origins for public data
 */
const publicCors = cors({
  origin: '*',
  methods: ['GET', 'OPTIONS'],
  allowedHeaders: ['Content-Type'],
  credentials: false,
  maxAge: 86400
});

/**
 * Custom CORS Error Handler
 */
const corsErrorHandler = (err, req, res, next) => {
  if (err.message && err.message.includes('CORS')) {
    logger.error('CORS error', {
      origin: req.headers.origin,
      method: req.method,
      path: req.path,
      error: err.message
    });

    return res.status(403).json({
      success: false,
      message: 'CORS policy violation',
      error: 'CORS_ERROR',
      details: process.env.NODE_ENV === 'development' ? err.message : undefined
    });
  }

  next(err);
};

/**
 * Preflight Handler
 * Optimized handling for OPTIONS requests
 */
const handlePreflight = (req, res, next) => {
  if (req.method === 'OPTIONS') {
    logger.debug('Preflight request', {
      origin: req.headers.origin,
      method: req.headers['access-control-request-method'],
      headers: req.headers['access-control-request-headers']
    });
    
    // CORS middleware will handle the response
    return next();
  }
  
  next();
};

/**
 * Security Headers Middleware
 * Adds additional security headers
 */
const securityHeaders = (req, res, next) => {
  // Prevent clickjacking
  res.setHeader('X-Frame-Options', 'DENY');
  
  // Prevent MIME type sniffing
  res.setHeader('X-Content-Type-Options', 'nosniff');
  
  // Enable XSS protection
  res.setHeader('X-XSS-Protection', '1; mode=block');
  
  // Strict Transport Security
  if (process.env.NODE_ENV === 'production') {
    res.setHeader(
      'Strict-Transport-Security',
      'max-age=31536000; includeSubDomains; preload'
    );
  }
  
  // Content Security Policy
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; " +
    "script-src 'self' 'unsafe-inline' 'unsafe-eval'; " +
    "style-src 'self' 'unsafe-inline'; " +
    "img-src 'self' data: https:; " +
    "font-src 'self' data:; " +
    "connect-src 'self' wss: ws:; " +
    "media-src 'self' blob:; " +
    "frame-ancestors 'none';"
  );
  
  // Referrer Policy
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  
  // Permissions Policy
  res.setHeader(
    'Permissions-Policy',
    'camera=(self), microphone=(self), geolocation=(), payment=()'
  );

  next();
};

/**
 * Origin Validator Middleware
 * Additional validation for sensitive endpoints
 */
const validateOrigin = (req, res, next) => {
  const origin = req.headers.origin || req.headers.referer;
  
  if (!origin && req.method !== 'GET') {
    logger.warn('Request without origin header', {
      method: req.method,
      path: req.path,
      ip: req.ip
    });
    
    return res.status(403).json({
      success: false,
      message: 'Origin header required',
      error: 'ORIGIN_REQUIRED'
    });
  }

  next();
};

module.exports = {
  corsMiddleware,
  strictExamCors,
  publicCors,
  corsErrorHandler,
  handlePreflight,
  securityHeaders,
  validateOrigin
};
