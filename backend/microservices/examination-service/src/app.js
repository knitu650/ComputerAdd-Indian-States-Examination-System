const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const examRoutes = require('./routes/exam.routes');
const questionRoutes = require('./routes/question.routes');

dotenv.config();

const app = express();
app.use(express.json());

// Database Connection
mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected to Examination-Service'))
.catch(err => console.error(err));

// Routes
app.use('/exams', examRoutes);
app.use('/questions', questionRoutes);

const PORT = process.env.PORT || 8082;

app.listen(PORT, () => {
    console.log(`Examination service running on port ${PORT}`);
});