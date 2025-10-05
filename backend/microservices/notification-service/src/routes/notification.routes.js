const express = require('express');
const router = express.Router();
const nodemailer = require('nodemailer');

// This is a placeholder for a more robust email service
const transporter = nodemailer.createTransport({
    host: 'smtp.ethereal.email',
    port: 587,
    auth: {
        user: 'your-test-user@ethereal.email', // Replace with a test account
        pass: 'your-test-password'
    }
});

// @desc    Send an email notification
// @route   POST /api/send-email
// @access  Internal
router.post('/send-email', async (req, res) => {
    const { to, subject, text, html } = req.body;

    if (!to || !subject || (!text && !html)) {
        return res.status(400).json({ message: 'Missing required fields for email' });
    }

    try {
        // In a real app, use a template engine and proper credentials
        await transporter.sendMail({ from: '"Exam System" <noreply@examsystem.com>', to, subject, text, html });
        res.status(200).json({ message: 'Email sent successfully' });
    } catch (error) {
        console.error("Error sending email:", error);
        res.status(500).json({ message: 'Failed to send email' });
    }
});

module.exports = router;