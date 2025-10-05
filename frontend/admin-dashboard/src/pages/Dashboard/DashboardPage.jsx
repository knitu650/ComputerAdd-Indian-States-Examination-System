import React from 'react';
import Overview from '../../components/dashboard/Overview/Overview';
import styles from './DashboardPage.module.css';

const DashboardPage = () => {
  return (
    <div className={styles.dashboard}>
      <h1>Dashboard Overview</h1>
      <Overview />
    </div>
  );
};

export default DashboardPage;