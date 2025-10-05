import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../../hooks/useAuth';
import { useNotification } from '../../../hooks/useNotification';
import styles from './Header.module.css';

const Header = () => {
  const { user, logout } = useAuth();
  const { notifications, unreadCount } = useNotification();
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      await logout();
      navigate('/login');
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <header className={styles.header}>
      <div className={styles.container}>
        <Link to="/" className={styles.logo}>
          <img src="/assets/logo.png" alt="Exam System" />
          <span>Indian States Exam</span>
        </Link>

        <nav className={styles.nav}>
          <Link to="/dashboard" className={styles.navLink}>Dashboard</Link>
          <Link to="/exams" className={styles.navLink}>Exams</Link>
          <Link to="/states" className={styles.navLink}>States</Link>
          <Link to="/practice" className={styles.navLink}>Practice</Link>
          <Link to="/results" className={styles.navLink}>Results</Link>
        </nav>

        <div className={styles.actions}>
          <button className={styles.notificationBtn}>
            <i className="fas fa-bell"></i>
            {unreadCount > 0 && (
              <span className={styles.badge}>{unreadCount}</span>
            )}
          </button>

          <div className={styles.userMenu}>
            <button className={styles.userBtn}>
              <img 
                src={user?.profile?.avatar || '/assets/default-avatar.png'} 
                alt={user?.fullName} 
              />
              <span>{user?.profile?.firstName}</span>
            </button>
            
            <div className={styles.dropdown}>
              <Link to="/profile">Profile</Link>
              <Link to="/settings">Settings</Link>
              <Link to="/help">Help</Link>
              <button onClick={handleLogout}>Logout</button>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
