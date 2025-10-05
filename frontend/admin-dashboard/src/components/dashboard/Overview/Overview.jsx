import React from 'react';
import styles from './Overview.module.css';

const Overview = () => {
  // Placeholder data
  const stats = [
    { label: 'Total Users', value: '1,250' },
    { label: 'Active Exams', value: '15' },
    { label: 'Exams Today', value: '3' },
    { label: 'Proctoring Alerts', value: '8' },
  ];

  return (
    <div className={styles.overviewGrid}>
      {stats.map((stat, index) => (
        <div key={index} className={styles.statCard}>
          <h3>{stat.label}</h3>
          <p>{stat.value}</p>
        </div>
      ))}
    </div>
  );
};

export default Overview;