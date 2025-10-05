const rateLimit = require('express-rate-limit');
const RedisStore = require('rate-limit-redis');
const redis = require('../config/redis.config');
const { logger } = require('../utils/logger');

/**
 * General API Rate Limiter
 * Limits requests per IP address
 */
const generalLimiter = rateLimit({
  windowMs: parseInt(process.env.RATE_LIMIT_WINDOW_MS) || 15 * 60 * 1000, // 15 minutes
  max: parseInt(process.env.RATE_LIMIT_MAX_REQUESTS) || 100,
  message: {
    success: false,
    message: 'Too many requests from this IP, please try again later',
    error: 'RATE_LIMIT_EXCEEDED'
  },
  standardHeaders: true,
  legacyHeaders: false,
  store: new RedisStore({
    client: redis,
    prefix: 'rl:general:'
  }),
  handler: (req, res) => {
    logger.warn('Rate limit exceeded', {
      ip: req.ip,
      path: req.path,
      method: req.method
    });

    res.status(429).json({
      success: false,
      message: 'Too many requests, please try again later',
      error: 'RATE_LIMIT_EXCEEDED',
      retryAfter: req.rateLimit.resetTime
    });
  }
});

/**
 * Strict Rate Limiter for Authentication Endpoints
 * Prevents brute force attacks
 */
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts
  skipSuccessfulRequests: true,
  message: {
    success: false,
    message: 'Too many login attempts, please try again after 15 minutes',
    error: 'AUTH_RATE_LIMIT_EXCEEDED'
  },
  store: new RedisStore({
    client: redis,
    prefix: 'rl:auth:'
  }),
  handler: (req, res) => {
    logger.warn('Authentication rate limit exceeded', {
      ip: req.ip,
      path: req.path,
      email: req.body.email
    });

    res.status(429).json({
      success: false,
      message: 'Too many login attempts, account temporarily locked',
      error: 'AUTH_RATE_LIMIT_EXCEEDED',
      lockoutDuration: '15 minutes'
    });
  }
});

/**
 * Exam Submission Rate Limiter
 * Prevents rapid answer submissions
 */
const examSubmissionLimiter = rateLimit({
  windowMs: 1000, // 1 second
  max: 1, // 1 submission per second
  skipSuccessfulRequests: false,
  message: {
    success: false,
    message: 'Please wait before submitting another answer',
    error: 'SUBMISSION_RATE_LIMIT'
  },
  store: new RedisStore({
    client: redis,
    prefix: 'rl:exam:'
  }),
  keyGenerator: (req) => {
    // Rate limit per user
    return `${req.user?.id || req.ip}`;
  }
});

/**
 * API Key Rate Limiter
 * Limits requests per API key (for service-to-service)
 */
const apiKeyLimiter = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 1000, // 1000 requests per minute
  skipSuccessfulRequests: false,
  store: new RedisStore({
    client: redis,
    prefix: 'rl:apikey:'
  }),
  keyGenerator: (req) => {
    return req.headers['x-api-key'] || req.ip;
  },
  handler: (req, res) => {
    logger.warn('API key rate limit exceeded', {
      apiKey: req.headers['x-api-key']?.substring(0, 8) + '...',
      path: req.path
    });

    res.status(429).json({
      success: false,
      message: 'API rate limit exceeded',
      error: 'API_RATE_LIMIT_EXCEEDED'
    });
  }
});

/**
 * File Upload Rate Limiter
 * Limits file upload requests
 */
const uploadLimiter = rateLimit({
  windowMs: 60 * 60 * 1000, // 1 hour
  max: 10, // 10 uploads per hour
  skipSuccessfulRequests: false,
  message: {
    success: false,
    message: 'Upload limit exceeded, please try again later',
    error: 'UPLOAD_RATE_LIMIT'
  },
  store: new RedisStore({
    client: redis,
    prefix: 'rl:upload:'
  }),
  keyGenerator: (req) => {
    return req.user?.id || req.ip;
  }
});

/**
 * Password Reset Rate Limiter
 * Prevents password reset abuse
 */
const passwordResetLimiter = rateLimit({
  windowMs: 60 * 60 * 1000, // 1 hour
  max: 3, // 3 attempts per hour
  skipSuccessfulRequests: false,
  message: {
    success: false,
    message: 'Too many password reset attempts',
    error: 'PASSWORD_RESET_LIMIT'
  },
  store: new RedisStore({
    client: redis,
    prefix: 'rl:password:'
  }),
  keyGenerator: (req) => {
    return req.body.email || req.ip;
  }
});

/**
 * Dynamic Rate Limiter
 * Adjusts limits based on user role
 */
const createDynamicLimiter = (options = {}) => {
  return (req, res, next) => {
    const userRole = req.user?.role || 'guest';
    
    const limits = {
      admin: 1000,
      examiner: 500,
      student: 100,
      guest: 50,
      ...options.customLimits
    };

    const limiter = rateLimit({
      windowMs: options.windowMs || 15 * 60 * 1000,
      max: limits[userRole] || limits.guest,
      store: new RedisStore({
        client: redis,
        prefix: `rl:dynamic:${userRole}:`
      }),
      keyGenerator: (req) => {
        return req.user?.id || req.ip;
      },
      handler: (req, res) => {
        logger.warn('Dynamic rate limit exceeded', {
          userId: req.user?.id,
          role: userRole,
          path: req.path
        });

        res.status(429).json({
          success: false,
          message: 'Rate limit exceeded for your account type',
          error: 'DYNAMIC_RATE_LIMIT_EXCEEDED'
        });
      }
    });

    limiter(req, res, next);
  };
};

/**
 * Proctoring Endpoint Rate Limiter
 * High frequency for real-time monitoring
 */
const proctoringLimiter = rateLimit({
  windowMs: 1000, // 1 second
  max: 10, // 10 requests per second for video frames
  skipSuccessfulRequests: false,
  store: new RedisStore({
    client: redis,
    prefix: 'rl:proctoring:'
  }),
  keyGenerator: (req) => {
    return `${req.user?.id}:${req.params.examId || 'default'}`;
  }
});

module.exports = {
  generalLimiter,
  authLimiter,
  examSubmissionLimiter,
  apiKeyLimiter,
  uploadLimiter,
  passwordResetLimiter,
  createDynamicLimiter,
  proctoringLimiter
};
