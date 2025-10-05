import React from 'react';
import { useParams } from 'react-router-dom';
import ExamInterface from '../../../components/examination/ExamInterface/ExamInterface';
import styles from './ExamRoom.module.css';

const ExamRoomPage = () => {
  const { id } = useParams();

  // In a real app, you would fetch exam details using the id
  const examDetails = {
    id,
    title: `Examination on Indian States - Part ${id}`,
    duration: 120, // in minutes
  };

  return (
    <div className={styles.examRoom}>
      <h2>{examDetails.title}</h2>
      <ExamInterface exam={examDetails} />
    </div>
  );
};

export default ExamRoomPage;