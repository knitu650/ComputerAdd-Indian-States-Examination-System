import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Home.module.css';

const Home = () => {
  return (
    <div className={styles.home}>
      <section className={styles.hero}>
        <h1>Indian States Examination System</h1>
        <p>Test your knowledge about Indian States</p>
        <Link to="/exams" className={styles.ctaButton}>
          Browse Exams
        </Link>
      </section>

      <section className={styles.features}>
        <div className={styles.feature}>
          <h3>28 States + 8 UTs</h3>
          <p>Complete coverage of all Indian states and union territories</p>
        </div>
        <div className={styles.feature}>
          <h3>AI Proctoring</h3>
          <p>Advanced computer vision based proctoring</p>
        </div>
        <div className={styles.feature}>
          <h3>Multi-language</h3>
          <p>Available in 22 Indian languages</p>
        </div>
      </section>
    </div>
  );
};

export default Home;
