import CryptoJS from 'crypto-js';

const SECRET_KEY = process.env.REACT_APP_ENCRYPTION_KEY || 'default-secret-key';

export const encrypt = (data) => {
  try {
    return CryptoJS.AES.encrypt(JSON.stringify(data), SECRET_KEY).toString();
  } catch (error) {
    console.error('Encryption error:', error);
    return null;
  }
};

export const decrypt = (encryptedData) => {
  try {
    const bytes = CryptoJS.AES.decrypt(encryptedData, SECRET_KEY);
    return JSON.parse(bytes.toString(CryptoJS.enc.Utf8));
  } catch (error) {
    console.error('Decryption error:', error);
    return null;
  }
};

export const hashPassword = (password) => {
  return CryptoJS.SHA256(password).toString();
};

export const generateRandomKey = (length = 32) => {
  return CryptoJS.lib.WordArray.random(length).toString();
};
