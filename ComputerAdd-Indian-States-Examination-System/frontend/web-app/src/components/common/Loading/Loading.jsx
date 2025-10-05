import React from 'react';
import styles from './Loading.module.css';

const Loading = ({ message = 'Loading...' }) => {
  return (
    <div className={styles.loading}>
      <div className={styles.spinner}></div>
      <p>{message}</p>
    </div>
  );
};

export default Loading;
