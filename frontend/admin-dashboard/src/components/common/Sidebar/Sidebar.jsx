import React from 'react';
import { NavLink } from 'react-router-dom';
import styles from './Sidebar.module.css';

const Sidebar = () => {
  return (
    <aside className={styles.sidebar}>
      <nav>
        <ul>
          <li>
            <NavLink to="/" className={({ isActive }) => isActive ? styles.active : ''}>
              Dashboard
            </NavLink>
          </li>
          <li>
            <NavLink to="/users" className={({ isActive }) => isActive ? styles.active : ''}>
              User Management
            </NavLink>
          </li>
          <li>
            <NavLink to="/exams" className={({ isActive }) => isActive ? styles.active : ''}>
              Exam Management
            </NavLink>
          </li>
          <li>
            <NavLink to="/analytics" className={({ isActive }) => isActive ? styles.active : ''}>
              Analytics
            </NavLink>
          </li>
          <li>
            <NavLink to="/proctoring" className={({ isActive }) => isActive ? styles.active : ''}>
              Proctoring
            </NavLink>
          </li>
          <li>
            <NavLink to="/settings" className={({ isActive }) => isActive ? styles.active : ''}>
              Settings
            </NavLink>
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;