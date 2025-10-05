import React from 'react';
import styles from './Header.module.css';

const Header = () => {
  return (
    <header className={styles.header}>
      <div className={styles.title}>Admin Dashboard</div>
      <div className={styles.userMenu}>
        <span>Welcome, Admin</span>
        <button>Logout</button>
      </div>
    </header>
  );
};

export default Header;