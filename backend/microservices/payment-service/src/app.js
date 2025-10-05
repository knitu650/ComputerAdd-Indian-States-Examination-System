const express = require('express');
const paymentRoutes = require('./routes/payment.routes');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

const app = express();

// Use express.raw({type: 'application/json'}) for webhook signature verification
app.use((req, res, next) => {
    if (req.originalUrl === '/api/webhook') {
        next();
    } else {
        express.json()(req, res, next);
    }
});

app.use('/api', paymentRoutes);

const PORT = process.env.PORT || 8086;

app.listen(PORT, () => {
    console.log(`Payment service running on port ${PORT}`);
});