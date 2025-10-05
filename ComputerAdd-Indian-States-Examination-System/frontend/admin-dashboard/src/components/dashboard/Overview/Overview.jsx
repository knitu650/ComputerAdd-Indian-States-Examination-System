import React, { useEffect, useState } from 'react';
import axios from 'axios';
import styles from './Overview.module.css';

const Overview = () => {
  const [stats, setStats] = useState({
    totalUsers: 0,
    totalExams: 0,
    activeExams: 0,
    totalRevenue: 0
  });

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const response = await axios.get('/api/v1/analytics/dashboard');
      setStats(response.data.data);
    } catch (error) {
      console.error('Failed to fetch stats', error);
    }
  };

  return (
    <div className={styles.overview}>
      <h2>Dashboard Overview</h2>
      
      <div className={styles.statsGrid}>
        <div className={styles.statCard}>
          <h3>Total Users</h3>
          <p className={styles.number}>{stats.totalUsers}</p>
        </div>

        <div className={styles.statCard}>
          <h3>Total Exams</h3>
          <p className={styles.number}>{stats.totalExams}</p>
        </div>

        <div className={styles.statCard}>
          <h3>Active Exams</h3>
          <p className={styles.number}>{stats.activeExams}</p>
        </div>

        <div className={styles.statCard}>
          <h3>Revenue</h3>
          <p className={styles.number}>₹{stats.totalRevenue}</p>
        </div>
      </div>
    </div>
  );
};

export default Overview;
