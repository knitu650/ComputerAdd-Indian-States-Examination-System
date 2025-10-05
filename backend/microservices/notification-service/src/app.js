const express = require('express');
const notificationRoutes = require('./routes/notification.routes');

const app = express();
app.use(express.json());

app.use('/api', notificationRoutes);

const PORT = process.env.PORT || 8085;

app.listen(PORT, () => {
    console.log(`Notification service running on port ${PORT}`);
});