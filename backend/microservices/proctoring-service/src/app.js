const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const proctoringRoutes = require('./routes/proctoring.routes');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

app.use(express.json());
app.use('/api', proctoringRoutes);

io.on('connection', (socket) => {
    console.log('A user connected to proctoring service');

    socket.on('join_exam_room', (examId) => {
        socket.join(examId);
        console.log(`User joined exam room: ${examId}`);
    });

    socket.on('proctoring_event', (data) => {
        // Broadcast event to admins/proctors in the same exam room
        io.to(data.examId).emit('new_proctoring_event', data.event);
    });

    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

const PORT = process.env.PORT || 8083;

server.listen(PORT, () => {
    console.log(`Proctoring service running on port ${PORT}`);
});