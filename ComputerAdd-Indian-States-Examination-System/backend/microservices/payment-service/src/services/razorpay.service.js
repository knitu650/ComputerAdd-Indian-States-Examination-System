const Razorpay = require('razorpay');
const crypto = require('crypto');

class RazorpayService {
  
  constructor() {
    this.client = new Razorpay({
      key_id: process.env.RAZORPAY_KEY_ID,
      key_secret: process.env.RAZORPAY_KEY_SECRET
    });
  }
  
  async createOrder(orderData) {
    try {
      const order = await this.client.orders.create(orderData);
      return order;
    } catch (error) {
      console.error('Razorpay create order error:', error);
      throw error;
    }
  }
  
  verifySignature(orderId, paymentId, signature) {
    try {
      const text = orderId + '|' + paymentId;
      const generated_signature = crypto
        .createHmac('sha256', process.env.RAZORPAY_KEY_SECRET)
        .update(text)
        .digest('hex');
      
      return generated_signature === signature;
    } catch (error) {
      console.error('Signature verification error:', error);
      return false;
    }
  }
  
  async capturePayment(paymentId, amount) {
    try {
      const payment = await this.client.payments.capture(paymentId, amount);
      return payment;
    } catch (error) {
      console.error('Payment capture error:', error);
      throw error;
    }
  }
  
  async refundPayment(paymentId, amount) {
    try {
      const refund = await this.client.payments.refund(paymentId, {
        amount: amount
      });
      return refund;
    } catch (error) {
      console.error('Refund error:', error);
      throw error;
    }
  }
}

module.exports = new RazorpayService();
