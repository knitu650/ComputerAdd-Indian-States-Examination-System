const emailService = require('../services/email.service');

exports.sendEmail = async (req, res) => {
  try {
    const { to, subject, body, template } = req.body;
    
    let htmlContent = body;
    
    if (template) {
      htmlContent = await emailService.renderTemplate(template, req.body.data);
    }
    
    await emailService.sendEmail(to, subject, htmlContent);
    
    res.json({
      success: true,
      message: 'Email sent successfully'
    });
    
  } catch (error) {
    console.error('Send email error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to send email'
    });
  }
};

exports.sendBulkEmail = async (req, res) => {
  try {
    const { recipients, subject, template, data } = req.body;
    
    const results = await Promise.allSettled(
      recipients.map(recipient => 
        emailService.sendEmail(
          recipient,
          subject,
          emailService.renderTemplate(template, { ...data, email: recipient })
        )
      )
    );
    
    const sent = results.filter(r => r.status === 'fulfilled').length;
    const failed = results.filter(r => r.status === 'rejected').length;
    
    res.json({
      success: true,
      data: {
        total: recipients.length,
        sent,
        failed
      }
    });
    
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Failed to send bulk emails'
    });
  }
};
