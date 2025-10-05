const paymentService = require('../services/razorpay.service');

exports.createOrder = async (req, res) => {
  try {
    const { amount, currency = 'INR', examId } = req.body;
    const { userId } = req.user;
    
    const order = await paymentService.createOrder({
      amount: amount * 100, // Convert to paise
      currency,
      receipt: `exam_${examId}_${userId}`,
      notes: {
        examId,
        userId
      }
    });
    
    res.json({
      success: true,
      data: order
    });
    
  } catch (error) {
    console.error('Create order error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to create order'
    });
  }
};

exports.verifyPayment = async (req, res) => {
  try {
    const { orderId, paymentId, signature } = req.body;
    
    const isValid = paymentService.verifySignature(orderId, paymentId, signature);
    
    if (!isValid) {
      return res.status(400).json({
        success: false,
        message: 'Invalid payment signature'
      });
    }
    
    // Save payment to database
    // const payment = await Payment.create({ ... });
    
    res.json({
      success: true,
      message: 'Payment verified successfully'
    });
    
  } catch (error) {
    console.error('Verify payment error:', error);
    res.status(500).json({
      success: false,
      message: 'Payment verification failed'
    });
  }
};

exports.getPaymentHistory = async (req, res) => {
  try {
    const { userId } = req.user;
    
    // const payments = await Payment.find({ userId }).sort({ createdAt: -1 });
    
    res.json({
      success: true,
      data: []
    });
    
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Failed to get payment history'
    });
  }
};
