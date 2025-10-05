import React from 'react';
import LoginForm from '../../../components/auth/LoginForm/LoginForm';
import styles from './Login.module.css';

const LoginPage = () => {
  return (
    <div className={styles.loginPage}>
      <div className={styles.loginContainer}>
        <h2>Login to Your Account</h2>
        <LoginForm />
      </div>
    </div>
  );
};

export default LoginPage;