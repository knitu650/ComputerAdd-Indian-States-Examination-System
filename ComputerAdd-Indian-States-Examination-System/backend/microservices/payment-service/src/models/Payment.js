const mongoose = require('mongoose');

const paymentSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  
  examId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Exam'
  },
  
  orderId: {
    type: String,
    required: true
  },
  
  paymentId: String,
  
  amount: {
    type: Number,
    required: true
  },
  
  currency: {
    type: String,
    default: 'INR'
  },
  
  status: {
    type: String,
    enum: ['created', 'pending', 'success', 'failed', 'refunded'],
    default: 'created'
  },
  
  paymentMethod: {
    type: String,
    enum: ['card', 'netbanking', 'upi', 'wallet']
  },
  
  gateway: {
    type: String,
    enum: ['razorpay', 'payu', 'stripe'],
    default: 'razorpay'
  },
  
  transactionId: String,
  
  metadata: {
    ipAddress: String,
    userAgent: String
  },
  
  refund: {
    status: Boolean,
    amount: Number,
    refundId: String,
    refundedAt: Date,
    reason: String
  }
  
}, { timestamps: true });

paymentSchema.index({ userId: 1, createdAt: -1 });
paymentSchema.index({ orderId: 1 });
paymentSchema.index({ status: 1 });

module.exports = mongoose.model('Payment', paymentSchema);
