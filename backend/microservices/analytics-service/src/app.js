const express = require('express');
const mongoose = require('mongoose');
const analyticsRoutes = require('./routes/analytics.routes');

const app = express();
app.use(express.json());

// Connect to a database if needed for storing aggregated analytics
// mongoose.connect(process.env.MONGO_URI, ...)

app.use('/api', analyticsRoutes);

const PORT = process.env.PORT || 8084;

app.listen(PORT, () => {
    console.log(`Analytics service running on port ${PORT}`);
});