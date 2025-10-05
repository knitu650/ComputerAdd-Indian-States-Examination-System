const nodemailer = require('nodemailer');
const fs = require('fs').promises;
const path = require('path');

class EmailService {
  
  constructor() {
    this.transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST || 'smtp.gmail.com',
      port: process.env.SMTP_PORT || 587,
      secure: false,
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS
      }
    });
  }
  
  async sendEmail(to, subject, html, attachments = []) {
    try {
      const mailOptions = {
        from: process.env.SMTP_FROM || 'noreply@indianstatesexam.com',
        to,
        subject,
        html,
        attachments
      };
      
      const info = await this.transporter.sendMail(mailOptions);
      
      console.log('Email sent:', info.messageId);
      return info;
      
    } catch (error) {
      console.error('Email send error:', error);
      throw error;
    }
  }
  
  async renderTemplate(templateName, data) {
    try {
      const templatePath = path.join(__dirname, '../templates/email', `${templateName}.html`);
      let template = await fs.readFile(templatePath, 'utf-8');
      
      // Simple template rendering (replace {{variable}})
      Object.keys(data).forEach(key => {
        const regex = new RegExp(`{{${key}}}`, 'g');
        template = template.replace(regex, data[key]);
      });
      
      return template;
      
    } catch (error) {
      console.error('Template render error:', error);
      return '';
    }
  }
  
  async sendVerificationEmail(email, token) {
    const verificationUrl = `${process.env.WEB_URL}/verify-email/${token}`;
    
    const html = `
      <h2>Email Verification</h2>
      <p>Please click the link below to verify your email:</p>
      <a href="${verificationUrl}">Verify Email</a>
      <p>This link will expire in 24 hours.</p>
    `;
    
    return this.sendEmail(email, 'Verify Your Email', html);
  }
  
  async sendPasswordResetEmail(email, token) {
    const resetUrl = `${process.env.WEB_URL}/reset-password/${token}`;
    
    const html = `
      <h2>Password Reset</h2>
      <p>Click the link below to reset your password:</p>
      <a href="${resetUrl}">Reset Password</a>
      <p>This link will expire in 1 hour.</p>
    `;
    
    return this.sendEmail(email, 'Password Reset', html);
  }
  
  async sendExamResultEmail(email, examTitle, score) {
    const html = `
      <h2>Exam Result</h2>
      <p>Your result for <strong>${examTitle}</strong>:</p>
      <h3>Score: ${score}%</h3>
      <p>Thank you for taking the exam!</p>
    `;
    
    return this.sendEmail(email, `Exam Result: ${examTitle}`, html);
  }
}

module.exports = new EmailService();
