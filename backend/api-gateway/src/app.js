const express = require('express');
const morgan = require('morgan');
const cors = require('cors');
const helmet = require('helmet');
const proxy = require('express-http-proxy');
const rateLimit = require('express-rate-limit');

const app = express();

// Middleware
app.use(morgan('dev'));
app.use(cors());
app.use(helmet());
app.use(express.json());

// Rate Limiter
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // limit each IP to 100 requests per windowMs
    standardHeaders: true,
    legacyHeaders: false,
});
app.use(limiter);

// Service Routes
app.use('/auth', proxy('http://user-service:8081'));
app.use('/users', proxy('http://user-service:8081'));
app.use('/exams', proxy('http://examination-service:8082'));
app.use('/proctoring', proxy('http://proctoring-service:8083'));
app.use('/analytics', proxy('http://analytics-service:8084'));

// AI/ML Service Route
app.use('/ai', proxy('http://ai-ml-service:5000'));

const PORT = process.env.PORT || 8080;

app.listen(PORT, () => {
    console.log(`API Gateway listening on port ${PORT}`);
});