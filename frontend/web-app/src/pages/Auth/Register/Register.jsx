import React from 'react';
import RegisterForm from '../../../components/auth/RegisterForm/RegisterForm';
import styles from './Register.module.css';

const RegisterPage = () => {
  return (
    <div className={styles.registerPage}>
      <div className={styles.registerContainer}>
        <h2>Create a New Account</h2>
        <RegisterForm />
      </div>
    </div>
  );
};

export default RegisterPage;