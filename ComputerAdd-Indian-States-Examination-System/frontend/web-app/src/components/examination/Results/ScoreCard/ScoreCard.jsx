import React from 'react';
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import styles from './ScoreCard.module.css';

const ScoreCard = ({ result }) => {
  const percentage = result.percentage || 0;
  const grade = result.grade || 'N/A';
  
  const getColor = (percentage) => {
    if (percentage >= 90) return '#10b981';
    if (percentage >= 75) return '#3b82f6';
    if (percentage >= 60) return '#f59e0b';
    return '#ef4444';
  };

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h2 className={styles.title}>Exam Result</h2>
        <span className={`${styles.badge} ${styles[grade.toLowerCase().replace('+', 'plus')]}`}>
          Grade {grade}
        </span>
      </div>

      <div className={styles.content}>
        <div className={styles.scoreCircle}>
          <CircularProgressbar
            value={percentage}
            text={`${percentage.toFixed(1)}%`}
            styles={buildStyles({
              textSize: '1.5rem',
              pathColor: getColor(percentage),
              textColor: getColor(percentage),
              trailColor: '#e5e7eb',
              pathTransitionDuration: 1.5,
            })}
          />
        </div>

        <div className={styles.stats}>
          <div className={styles.statItem}>
            <span className={styles.statLabel}>Total Marks</span>
            <span className={styles.statValue}>{result.totalMarks}</span>
          </div>
          
          <div className={styles.statItem}>
            <span className={styles.statLabel}>Marks Obtained</span>
            <span className={styles.statValue}>{result.obtainedMarks}</span>
          </div>
          
          <div className={styles.statItem}>
            <span className={styles.statLabel}>Correct Answers</span>
            <span className={styles.statValue}>
              {result.questionResults?.filter(q => q.isCorrect).length || 0}
            </span>
          </div>
          
          <div className={styles.statItem}>
            <span className={styles.statLabel}>Wrong Answers</span>
            <span className={styles.statValue}>
              {result.questionResults?.filter(q => !q.isCorrect).length || 0}
            </span>
          </div>
        </div>
      </div>

      <div className={styles.footer}>
        <div className={styles.message}>
          {percentage >= 90 && '🎉 Outstanding Performance!'}
          {percentage >= 75 && percentage < 90 && '👏 Great Job!'}
          {percentage >= 60 && percentage < 75 && '✓ Good Effort!'}
          {percentage < 60 && '💪 Keep Practicing!'}
        </div>
      </div>
    </div>
  );
};

export default ScoreCard;
