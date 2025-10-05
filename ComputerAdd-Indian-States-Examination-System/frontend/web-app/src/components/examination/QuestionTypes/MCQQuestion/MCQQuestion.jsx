import React from 'react';
import styles from './MCQQuestion.module.css';

const MCQQuestion = ({ question, selectedAnswer, onAnswerSelect }) => {
  return (
    <div className={styles.mcq}>
      <h3>{question.questionText}</h3>
      
      {question.media?.imageUrl && (
        <img src={question.media.imageUrl} alt="Question" className={styles.image} />
      )}

      <div className={styles.options}>
        {question.options.map((option, index) => (
          <label key={index} className={styles.option}>
            <input
              type="radio"
              name="answer"
              value={option.text}
              checked={selectedAnswer === option.text}
              onChange={() => onAnswerSelect(option.text)}
            />
            <span>{option.text}</span>
          </label>
        ))}
      </div>
    </div>
  );
};

export default MCQQuestion;
