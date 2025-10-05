import React from 'react';
import styles from './TrueFalseQuestion.module.css';

const TrueFalseQuestion = ({ question, answer, onAnswer }) => {
  return (
    <div className={styles.container}>
      <h3 className={styles.question}>{question.text}</h3>
      
      {question.image && (
        <img src={question.image} alt="Question" className={styles.image} />
      )}
      
      <div className={styles.options}>
        <button
          className={`${styles.option} ${answer === 'true' ? styles.selected : ''}`}
          onClick={() => onAnswer('true')}
        >
          <span className={styles.icon}>✓</span>
          True
        </button>
        
        <button
          className={`${styles.option} ${answer === 'false' ? styles.selected : ''}`}
          onClick={() => onAnswer('false')}
        >
          <span className={styles.icon}>✗</span>
          False
        </button>
      </div>
    </div>
  );
};

export default TrueFalseQuestion;
