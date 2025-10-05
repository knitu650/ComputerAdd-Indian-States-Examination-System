import React from 'react';
import styles from './Footer.module.css';

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <div className={styles.container}>
        <div className={styles.section}>
          <h4>About</h4>
          <p>Indian States Examination System</p>
        </div>
        <div className={styles.section}>
          <h4>Quick Links</h4>
          <a href="/about">About Us</a>
          <a href="/contact">Contact</a>
          <a href="/privacy">Privacy Policy</a>
        </div>
        <div className={styles.section}>
          <h4>Support</h4>
          <a href="/help">Help Center</a>
          <a href="/faq">FAQ</a>
        </div>
      </div>
      <div className={styles.copyright}>
        © 2025 ComputerAdd. All rights reserved.
      </div>
    </footer>
  );
};

export default Footer;
