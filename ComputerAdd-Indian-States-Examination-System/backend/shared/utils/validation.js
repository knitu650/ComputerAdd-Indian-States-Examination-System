const validator = require('validator');

class ValidationUtils {
  
  static validateEmail(email) {
    return validator.isEmail(email);
  }
  
  static validatePassword(password) {
    // At least 8 chars, 1 uppercase, 1 lowercase, 1 number
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d@$!%*?&]{8,}$/;
    return regex.test(password);
  }
  
  static validatePhone(phone) {
    // Indian phone numbers
    const regex = /^[6-9]\d{9}$/;
    return regex.test(phone);
  }
  
  static validatePincode(pincode) {
    const regex = /^[1-9][0-9]{5}$/;
    return regex.test(pincode);
  }
  
  static sanitizeInput(input) {
    if (typeof input !== 'string') return input;
    
    return validator.escape(input);
  }
  
  static validateObjectId(id) {
    return validator.isMongoId(id);
  }
  
  static validateURL(url) {
    return validator.isURL(url);
  }
}

module.exports = ValidationUtils;
