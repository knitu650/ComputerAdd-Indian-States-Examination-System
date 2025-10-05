import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useExam } from '../../../hooks/useExam';
import { useTimer } from '../../../hooks/useTimer';
import { useProctoring } from '../../../hooks/useProctoring';
import QuestionPanel from './QuestionPanel';
import AnswerPanel from './AnswerPanel';
import NavigationPanel from './NavigationPanel';
import TimerPanel from './TimerPanel';
import styles from './ExamInterface.module.css';

const ExamInterface = () => {
  const { examId } = useParams();
  const navigate = useNavigate();
  const { 
    exam, 
    currentQuestion, 
    submitAnswer, 
    submitExam,
    goToQuestion 
  } = useExam(examId);
  
  const { timeRemaining, formatTime } = useTimer(exam?.duration * 60);
  const { startProctoring, violations } = useProctoring(examId);

  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [flaggedQuestions, setFlaggedQuestions] = useState(new Set());

  useEffect(() => {
    if (exam?.proctoring?.enabled) {
      startProctoring();
    }
  }, [exam]);

  useEffect(() => {
    if (timeRemaining === 0) {
      handleSubmitExam();
    }
  }, [timeRemaining]);

  const handleAnswerSelect = (answer) => {
    setSelectedAnswer(answer);
  };

  const handleSubmitAnswer = async () => {
    if (selectedAnswer) {
      await submitAnswer(currentQuestion.id, selectedAnswer);
      setSelectedAnswer(null);
      
      // Move to next question
      if (currentQuestion.number < exam.totalQuestions) {
        goToQuestion(currentQuestion.number + 1);
      }
    }
  };

  const handleFlagQuestion = () => {
    const newFlagged = new Set(flaggedQuestions);
    if (newFlagged.has(currentQuestion.id)) {
      newFlagged.delete(currentQuestion.id);
    } else {
      newFlagged.add(currentQuestion.id);
    }
    setFlaggedQuestions(newFlagged);
  };

  const handleSubmitExam = async () => {
    if (window.confirm('Are you sure you want to submit the exam?')) {
      await submitExam();
      navigate(`/exams/${examId}/result`);
    }
  };

  if (!exam || !currentQuestion) {
    return <div className={styles.loading}>Loading exam...</div>;
  }

  return (
    <div className={styles.examInterface}>
      <div className={styles.header}>
        <h1>{exam.title}</h1>
        <TimerPanel 
          timeRemaining={timeRemaining} 
          formatTime={formatTime} 
        />
      </div>

      {violations.length > 0 && (
        <div className={styles.violationAlert}>
          <i className="fas fa-exclamation-triangle"></i>
          Violation detected: {violations[violations.length - 1].type}
        </div>
      )}

      <div className={styles.content}>
        <div className={styles.leftPanel}>
          <QuestionPanel 
            question={currentQuestion}
            questionNumber={currentQuestion.number}
            totalQuestions={exam.totalQuestions}
          />

          <AnswerPanel
            question={currentQuestion}
            selectedAnswer={selectedAnswer}
            onAnswerSelect={handleAnswerSelect}
          />

          <div className={styles.actions}>
            <button 
              className={styles.flagBtn}
              onClick={handleFlagQuestion}
            >
              {flaggedQuestions.has(currentQuestion.id) ? 'Unflag' : 'Flag'} Question
            </button>
            
            <button 
              className={styles.clearBtn}
              onClick={() => setSelectedAnswer(null)}
            >
              Clear Answer
            </button>
            
            <button 
              className={styles.submitBtn}
              onClick={handleSubmitAnswer}
              disabled={!selectedAnswer}
            >
              Save & Next
            </button>
          </div>
        </div>

        <div className={styles.rightPanel}>
          <NavigationPanel
            questions={exam.questions}
            currentQuestion={currentQuestion.number}
            answeredQuestions={exam.answeredQuestions}
            flaggedQuestions={flaggedQuestions}
            onQuestionSelect={goToQuestion}
          />

          <button 
            className={styles.submitExamBtn}
            onClick={handleSubmitExam}
          >
            Submit Exam
          </button>
        </div>
      </div>
    </div>
  );
};

export default ExamInterface;
