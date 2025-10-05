const cors = require('cors');

const corsOptions = {
  origin: ['http://localhost:3000', 'http://localhost:3001'], // Whitelist frontend origins
  methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
  credentials: true,
  optionsSuccessStatus: 204,
};

module.exports = cors(corsOptions);