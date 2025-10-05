const winston = require('winston');
const path = require('path');

/**
 * Custom Winston Logger Configuration
 * Provides structured logging with multiple transports
 */

// Define log levels
const levels = {
  error: 0,
  warn: 1,
  info: 2,
  http: 3,
  debug: 4
};

// Define colors for each level
const colors = {
  error: 'red',
  warn: 'yellow',
  info: 'green',
  http: 'magenta',
  debug: 'blue'
};

// Tell winston about our colors
winston.addColors(colors);

// Define log format
const format = winston.format.combine(
  winston.format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
  winston.format.errors({ stack: true }),
  winston.format.splat(),
  winston.format.json()
);

// Define console format (pretty printing for development)
const consoleFormat = winston.format.combine(
  winston.format.colorize({ all: true }),
  winston.format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
  winston.format.printf((info) => {
    const { timestamp, level, message, ...meta } = info;
    const metaString = Object.keys(meta).length ? `\n${JSON.stringify(meta, null, 2)}` : '';
    return `[${timestamp}] ${level}: ${message}${metaString}`;
  })
);

// Define transports
const transports = [
  // Console transport
  new winston.transports.Console({
    format: consoleFormat,
    level: process.env.LOG_LEVEL || 'debug'
  }),

  // File transport for errors
  new winston.transports.File({
    filename: path.join('logs', 'error.log'),
    level: 'error',
    format,
    maxsize: 10485760, // 10MB
    maxFiles: 5
  }),

  // File transport for all logs
  new winston.transports.File({
    filename: path.join('logs', 'combined.log'),
    format,
    maxsize: 10485760, // 10MB
    maxFiles: 5
  })
];

// Create logger instance
const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  levels,
  format,
  transports,
  exitOnError: false
});

// Create stream for Morgan
const morganStream = {
  write: (message) => {
    logger.http(message.trim());
  }
};

// Helper functions
logger.logRequest = (req, message = 'Request received') => {
  logger.info(message, {
    method: req.method,
    path: req.path,
    ip: req.ip,
    userAgent: req.get('user-agent'),
    userId: req.user?.id
  });
};

logger.logResponse = (req, res, message = 'Response sent') => {
  logger.info(message, {
    method: req.method,
    path: req.path,
    statusCode: res.statusCode,
    userId: req.user?.id,
    duration: res.get('X-Response-Time')
  });
};

logger.logError = (error, req = null) => {
  const errorLog = {
    message: error.message,
    stack: error.stack,
    name: error.name
  };

  if (req) {
    errorLog.request = {
      method: req.method,
      path: req.path,
      body: req.body,
      userId: req.user?.id
    };
  }

  logger.error('Error occurred', errorLog);
};

logger.logPerformance = (req, startTime, message = 'Performance metric') => {
  const duration = Date.now() - startTime;
  
  logger.info(message, {
    method: req.method,
    path: req.path,
    duration: `${duration}ms`,
    userId: req.user?.id
  });

  // Log warning if request takes too long
  if (duration > 3000) {
    logger.warn('Slow request detected', {
      method: req.method,
      path: req.path,
      duration: `${duration}ms`
    });
  }
};

logger.logAuth = (action, userId, success, details = {}) => {
  logger.info(`Authentication ${action}`, {
    userId,
    success,
    action,
    ...details
  });
};

logger.logExam = (action, examId, userId, details = {}) => {
  logger.info(`Exam ${action}`, {
    examId,
    userId,
    action,
    ...details
  });
};

logger.logSecurity = (event, severity = 'medium', details = {}) => {
  const logMethod = severity === 'high' ? 'error' : severity === 'medium' ? 'warn' : 'info';
  
  logger[logMethod](`Security event: ${event}`, {
    event,
    severity,
    timestamp: new Date().toISOString(),
    ...details
  });
};

module.exports = {
  logger,
  morganStream
};
