import React from 'react';
import ExamList from '../../components/exam-management/ExamList/ExamList';
import styles from './ExamListPage.module.css';

const ExamListPage = () => {
  // Placeholder data for exams
  const exams = [
    { id: 'e1', title: 'Geography of Northern States', subject: 'Geography', questions: 25, status: 'Active' },
    { id: 'e2', title: 'History of the Mauryan Empire', subject: 'History', questions: 40, status: 'Draft' },
    { id: 'e3', title: 'Culture of Southern States', subject: 'Culture', questions: 30, status: 'Archived' },
  ];

  return (
    <div className={styles.examPage}>
      <h1>Exam Management</h1>
      <button className={styles.createButton}>Create New Exam</button>
      <ExamList exams={exams} />
    </div>
  );
};

export default ExamListPage;