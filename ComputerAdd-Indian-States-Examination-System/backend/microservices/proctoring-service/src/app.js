const express = require('express');
const http = require('http');
const socketIO = require('socket.io');
const videoMonitoringController = require('./controllers/video-monitoring.controller');

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

app.use(express.json());

// Routes
app.post('/api/v1/monitoring/start', videoMonitoringController.startMonitoring);
app.post('/api/v1/monitoring/frame', videoMonitoringController.processFrame);
app.get('/api/v1/monitoring/:examId/:userId/violations', videoMonitoringController.getViolations);

// WebSocket for real-time monitoring
io.on('connection', (socket) => {
  console.log('Client connected:', socket.id);
  
  socket.on('start-proctoring', (data) => {
    socket.join(`exam-${data.examId}-${data.userId}`);
  });
  
  socket.on('video-frame', async (data) => {
    // Process frame
    // Emit violations to admin
  });
  
  socket.on('disconnect', () => {
    console.log('Client disconnected:', socket.id);
  });
});

const PORT = process.env.PORT || 3003;
server.listen(PORT, () => {
  console.log(`Proctoring service listening on port ${PORT}`);
});
