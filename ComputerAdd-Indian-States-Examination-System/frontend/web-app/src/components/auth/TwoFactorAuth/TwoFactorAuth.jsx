import React, { useState, useRef, useEffect } from 'react';
import styles from './TwoFactorAuth.module.css';

const TwoFactorAuth = ({ onVerify, onResend }) => {
  const [code, setCode] = useState(['', '', '', '', '', '']);
  const [loading, setLoading] = useState(false);
  const inputRefs = useRef([]);

  useEffect(() => {
    inputRefs.current[0]?.focus();
  }, []);

  const handleChange = (index, value) => {
    if (value.length <= 1 && /^[0-9]*$/.test(value)) {
      const newCode = [...code];
      newCode[index] = value;
      setCode(newCode);

      if (value && index < 5) {
        inputRefs.current[index + 1]?.focus();
      }

      if (newCode.every(digit => digit !== '')) {
        handleSubmit(newCode.join(''));
      }
    }
  };

  const handleKeyDown = (index, e) => {
    if (e.key === 'Backspace' && !code[index] && index > 0) {
      inputRefs.current[index - 1]?.focus();
    }
  };

  const handlePaste = (e) => {
    e.preventDefault();
    const pastedData = e.clipboardData.getData('text').slice(0, 6);
    
    if (/^[0-9]{6}$/.test(pastedData)) {
      const newCode = pastedData.split('');
      setCode(newCode);
      handleSubmit(pastedData);
    }
  };

  const handleSubmit = async (fullCode) => {
    setLoading(true);
    try {
      await onVerify(fullCode);
    } catch (error) {
      setCode(['', '', '', '', '', '']);
      inputRefs.current[0]?.focus();
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.iconWrapper}>
        <div className={styles.icon}>🔐</div>
      </div>

      <h2 className={styles.title}>Two-Factor Authentication</h2>
      <p className={styles.subtitle}>
        Enter the 6-digit code sent to your registered device
      </p>

      <div className={styles.codeInputs} onPaste={handlePaste}>
        {code.map((digit, index) => (
          <input
            key={index}
            ref={(el) => (inputRefs.current[index] = el)}
            type="text"
            inputMode="numeric"
            maxLength="1"
            value={digit}
            onChange={(e) => handleChange(index, e.target.value)}
            onKeyDown={(e) => handleKeyDown(index, e)}
            className={styles.codeInput}
            disabled={loading}
          />
        ))}
      </div>

      {loading && <div className={styles.loader}>Verifying...</div>}

      <button onClick={onResend} className={styles.resendBtn}>
        Didn't receive code? Resend
      </button>
    </div>
  );
};

export default TwoFactorAuth;
