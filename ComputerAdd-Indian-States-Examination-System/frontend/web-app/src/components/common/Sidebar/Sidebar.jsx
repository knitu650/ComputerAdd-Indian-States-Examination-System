import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FaHome, FaBook, FaChartBar, FaUser, FaCog, FaSignOutAlt } from 'react-icons/fa';
import styles from './Sidebar.module.css';

const Sidebar = ({ isOpen, onClose }) => {
  const location = useLocation();
  const [collapsed, setCollapsed] = useState(false);

  const menuItems = [
    { path: '/dashboard', icon: FaHome, label: 'Dashboard' },
    { path: '/exams', icon: FaBook, label: 'Exams' },
    { path: '/states', icon: FaBook, label: 'Indian States' },
    { path: '/analytics', icon: FaChartBar, label: 'Analytics' },
    { path: '/profile', icon: FaUser, label: 'Profile' },
    { path: '/settings', icon: FaCog, label: 'Settings' },
  ];

  return (
    <>
      {isOpen && <div className={styles.overlay} onClick={onClose} />}
      
      <aside className={`${styles.sidebar} ${isOpen ? styles.open : ''} ${collapsed ? styles.collapsed : ''}`}>
        <div className={styles.header}>
          <h2 className={styles.logo}>Exam Portal</h2>
          <button 
            className={styles.collapseBtn}
            onClick={() => setCollapsed(!collapsed)}
          >
            ☰
          </button>
        </div>

        <nav className={styles.nav}>
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;
            
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`${styles.navItem} ${isActive ? styles.active : ''}`}
                onClick={onClose}
              >
                <Icon className={styles.icon} />
                {!collapsed && <span>{item.label}</span>}
              </Link>
            );
          })}
        </nav>

        <button className={styles.logoutBtn}>
          <FaSignOutAlt className={styles.icon} />
          {!collapsed && <span>Logout</span>}
        </button>
      </aside>
    </>
  );
};

export default Sidebar;
