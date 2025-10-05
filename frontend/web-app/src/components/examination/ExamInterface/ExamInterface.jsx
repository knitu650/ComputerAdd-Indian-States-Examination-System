import React, { useState, useEffect } from 'react';
import styles from './ExamInterface.module.css';

// Placeholder components that would be in their own files
const QuestionPanel = ({ question }) => (
  <div className={styles.questionPanel}>
    <h3>Question:</h3>
    <p>{question}</p>
  </div>
);

const AnswerPanel = ({ onAnswer }) => (
  <div className={styles.answerPanel}>
    <h3>Your Answer:</h3>
    <textarea placeholder="Type your answer here..."></textarea>
    <button onClick={() => onAnswer({})}>Submit Answer</button>
  </div>
);

const TimerPanel = ({ duration }) => {
  const [timeLeft, setTimeLeft] = useState(duration * 60); // in seconds

  useEffect(() => {
    const timer = setInterval(() => {
      setTimeLeft(prevTime => (prevTime > 0 ? prevTime - 1 : 0));
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
  };

  return (
    <div className={styles.timerPanel}>
      Time Left: <strong>{formatTime(timeLeft)}</strong>
    </div>
  );
};


const ExamInterface = ({ exam }) => {
  const [currentQuestion, setCurrentQuestion] = useState('What is the capital of Maharashtra?');

  const handleAnswerSubmit = (answer) => {
    console.log('Answer submitted:', answer);
    // Logic to move to the next question
    setCurrentQuestion('Which is the largest state by area in India?');
  };

  return (
    <div className={styles.examInterface}>
      <TimerPanel duration={exam.duration} />
      <div className={styles.mainContent}>
        <QuestionPanel question={currentQuestion} />
        <AnswerPanel onAnswer={handleAnswerSubmit} />
      </div>
      <div className={styles.navigation}>
        <button>Previous</button>
        <button>Next</button>
        <button className={styles.finishButton}>Finish Exam</button>
      </div>
    </div>
  );
};

export default ExamInterface;