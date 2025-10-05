import React from 'react';
import styles from './ExamList.module.css';

const ExamList = ({ exams }) => {
  return (
    <div className={styles.examListContainer}>
      <table className={styles.examTable}>
        <thead>
          <tr>
            <th>Title</th>
            <th>Subject</th>
            <th>Questions</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {exams.map((exam) => (
            <tr key={exam.id}>
              <td>{exam.title}</td>
              <td>{exam.subject}</td>
              <td>{exam.questions}</td>
              <td><span className={`${styles.status} ${styles[exam.status.toLowerCase()]}`}>{exam.status}</span></td>
              <td>
                <button className={styles.actionButton}>View</button>
                <button className={styles.actionButton}>Edit</button>
                <button className={`${styles.actionButton} ${styles.deleteButton}`}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ExamList;