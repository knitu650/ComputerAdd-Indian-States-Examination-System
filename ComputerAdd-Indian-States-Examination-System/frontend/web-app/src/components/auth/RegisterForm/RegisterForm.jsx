import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import styles from './RegisterForm.module.css';

const RegisterForm = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
    firstName: '',
    lastName: '',
    phoneNumber: '',
    dateOfBirth: '',
    gender: 'male'
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (formData.password !== formData.confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    setLoading(true);
    setError('');

    try {
      await axios.post('/api/v1/auth/register', {
        email: formData.email,
        password: formData.password,
        profile: {
          firstName: formData.firstName,
          lastName: formData.lastName,
          phoneNumber: formData.phoneNumber,
          dateOfBirth: formData.dateOfBirth,
          gender: formData.gender
        }
      });
      navigate('/login?registered=true');
    } catch (err) {
      setError(err.response?.data?.message || 'Registration failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <h2>Create Account</h2>
      
      {error && <div className={styles.error}>{error}</div>}
      
      <div className={styles.row}>
        <div className={styles.field}>
          <label>First Name</label>
          <input name="firstName" value={formData.firstName} onChange={handleChange} required />
        </div>
        <div className={styles.field}>
          <label>Last Name</label>
          <input name="lastName" value={formData.lastName} onChange={handleChange} required />
        </div>
      </div>

      <div className={styles.field}>
        <label>Email</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange} required />
      </div>

      <div className={styles.field}>
        <label>Phone Number</label>
        <input name="phoneNumber" value={formData.phoneNumber} onChange={handleChange} required />
      </div>

      <div className={styles.field}>
        <label>Date of Birth</label>
        <input type="date" name="dateOfBirth" value={formData.dateOfBirth} onChange={handleChange} required />
      </div>

      <div className={styles.field}>
        <label>Gender</label>
        <select name="gender" value={formData.gender} onChange={handleChange}>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
      </div>

      <div className={styles.field}>
        <label>Password</label>
        <input type="password" name="password" value={formData.password} onChange={handleChange} required />
      </div>

      <div className={styles.field}>
        <label>Confirm Password</label>
        <input type="password" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} required />
      </div>

      <button type="submit" disabled={loading}>
        {loading ? 'Creating Account...' : 'Register'}
      </button>

      <div className={styles.links}>
        <a href="/login">Already have an account? Login</a>
      </div>
    </form>
  );
};

export default RegisterForm;
