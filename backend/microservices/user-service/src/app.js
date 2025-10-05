const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const authRoutes = require('./routes/auth.routes');
const profileRoutes = require('./routes/profile.routes');

dotenv.config();

const app = express();
app.use(express.json());

// Database Connection
mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected to User-Service'))
.catch(err => console.error(err));

// Routes
app.use('/auth', authRoutes);
app.use('/profile', profileRoutes);


const PORT = process.env.PORT || 8081;

app.listen(PORT, () => {
    console.log(`User service running on port ${PORT}`);
});