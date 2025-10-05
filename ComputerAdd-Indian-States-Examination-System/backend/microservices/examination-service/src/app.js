const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3002;

app.use(express.json());

mongoose.connect(process.env.MONGODB_URI)
  .then(() => console.log('✅ Examination Service: MongoDB connected'))
  .catch(err => console.error('❌ MongoDB error:', err));

app.get('/health', (req, res) => {
  res.json({ success: true, service: 'Examination Service' });
});

app.listen(PORT, () => {
  console.log(`🚀 Examination Service on port ${PORT}`);
});
