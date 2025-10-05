const jwt = require('jsonwebtoken');
const redis = require('../config/redis.config');
const { logger } = require('../utils/logger');

/**
 * Authentication Middleware
 * Verifies JWT tokens and validates user sessions
 */
const authMiddleware = async (req, res, next) => {
  try {
    // Extract token from header
    const authHeader = req.headers.authorization;
    
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return res.status(401).json({
        success: false,
        message: 'No authentication token provided',
        error: 'UNAUTHORIZED'
      });
    }

    const token = authHeader.substring(7);

    // Check if token is blacklisted
    const isBlacklisted = await redis.get(`blacklist:${token}`);
    if (isBlacklisted) {
      return res.status(401).json({
        success: false,
        message: 'Token has been revoked',
        error: 'TOKEN_REVOKED'
      });
    }

    // Verify token
    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    // Check if user session exists in Redis
    const sessionKey = `session:${decoded.userId}`;
    const session = await redis.get(sessionKey);

    if (!session) {
      return res.status(401).json({
        success: false,
        message: 'Session expired or invalid',
        error: 'SESSION_EXPIRED'
      });
    }

    // Attach user info to request
    req.user = {
      id: decoded.userId,
      email: decoded.email,
      role: decoded.role,
      sessionId: decoded.sessionId
    };

    // Log authentication
    logger.info(`User ${req.user.id} authenticated successfully`, {
      userId: req.user.id,
      path: req.path,
      method: req.method
    });

    next();
  } catch (error) {
    if (error.name === 'TokenExpiredError') {
      return res.status(401).json({
        success: false,
        message: 'Token has expired',
        error: 'TOKEN_EXPIRED'
      });
    }

    if (error.name === 'JsonWebTokenError') {
      return res.status(401).json({
        success: false,
        message: 'Invalid token',
        error: 'INVALID_TOKEN'
      });
    }

    logger.error('Authentication error:', error);
    return res.status(500).json({
      success: false,
      message: 'Authentication failed',
      error: 'AUTH_ERROR'
    });
  }
};

/**
 * Role-based Authorization Middleware
 * Checks if user has required role
 */
const authorize = (...allowedRoles) => {
  return (req, res, next) => {
    if (!req.user) {
      return res.status(401).json({
        success: false,
        message: 'Authentication required',
        error: 'UNAUTHORIZED'
      });
    }

    if (!allowedRoles.includes(req.user.role)) {
      logger.warn(`User ${req.user.id} attempted unauthorized access`, {
        userId: req.user.id,
        role: req.user.role,
        requiredRoles: allowedRoles,
        path: req.path
      });

      return res.status(403).json({
        success: false,
        message: 'Insufficient permissions',
        error: 'FORBIDDEN'
      });
    }

    next();
  };
};

/**
 * Optional Authentication Middleware
 * Validates token if present but doesn't require it
 */
const optionalAuth = async (req, res, next) => {
  try {
    const authHeader = req.headers.authorization;
    
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return next();
    }

    const token = authHeader.substring(7);
    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    req.user = {
      id: decoded.userId,
      email: decoded.email,
      role: decoded.role
    };
  } catch (error) {
    // Silently fail for optional auth
    logger.debug('Optional auth failed:', error.message);
  }

  next();
};

/**
 * Exam Session Validator
 * Ensures user has active exam session
 */
const validateExamSession = async (req, res, next) => {
  try {
    const { examId } = req.params;
    const userId = req.user.id;

    // Check active exam session in Redis
    const sessionKey = `exam:session:${userId}:${examId}`;
    const examSession = await redis.get(sessionKey);

    if (!examSession) {
      return res.status(403).json({
        success: false,
        message: 'No active exam session found',
        error: 'NO_ACTIVE_SESSION'
      });
    }

    const session = JSON.parse(examSession);

    // Check if exam time has expired
    if (new Date() > new Date(session.endTime)) {
      return res.status(403).json({
        success: false,
        message: 'Exam time has expired',
        error: 'EXAM_EXPIRED'
      });
    }

    req.examSession = session;
    next();
  } catch (error) {
    logger.error('Exam session validation error:', error);
    return res.status(500).json({
      success: false,
      message: 'Failed to validate exam session',
      error: 'VALIDATION_ERROR'
    });
  }
};

/**
 * API Key Middleware
 * Validates API keys for service-to-service communication
 */
const validateApiKey = (req, res, next) => {
  const apiKey = req.headers['x-api-key'];

  if (!apiKey) {
    return res.status(401).json({
      success: false,
      message: 'API key required',
      error: 'API_KEY_MISSING'
    });
  }

  // Validate API key (in production, check against database/vault)
  const validApiKeys = process.env.VALID_API_KEYS?.split(',') || [];

  if (!validApiKeys.includes(apiKey)) {
    logger.warn('Invalid API key attempted', {
      apiKey: apiKey.substring(0, 8) + '...',
      ip: req.ip
    });

    return res.status(401).json({
      success: false,
      message: 'Invalid API key',
      error: 'INVALID_API_KEY'
    });
  }

  next();
};

module.exports = {
  authMiddleware,
  authorize,
  optionalAuth,
  validateExamSession,
  validateApiKey
};
