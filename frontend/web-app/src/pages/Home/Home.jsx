import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Home.module.css';

const HomePage = () => {
  return (
    <div className={styles.home}>
      <section className={styles.hero}>
        <h1>Welcome to the Indian States Examination System</h1>
        <p>Your journey to mastering knowledge about India's states starts here.</p>
        <Link to="/exams" className={styles.ctaButton}>Browse Exams</Link>
      </section>

      <section className={styles.features}>
        <h2>Why Choose Us?</h2>
        <div className={styles.featureGrid}>
          <div className={styles.feature}>
            <h3>Comprehensive Content</h3>
            <p>Covering all 28 states and 8 union territories with in-depth material.</p>
          </div>
          <div className={styles.feature}>
            <h3>AI-Powered Proctoring</h3>
            <p>Ensuring a fair and secure examination environment for everyone.</p>
          </div>
          <div className={styles.feature}>
            <h3>Interactive Learning</h3>
            <p>Engage with maps, quizzes, and multimedia content to enhance learning.</p>
          </div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;