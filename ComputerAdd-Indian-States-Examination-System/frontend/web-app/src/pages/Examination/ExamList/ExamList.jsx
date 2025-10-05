import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { FaClock, FaQuestionCircle, FaStar } from 'react-icons/fa';
import Card from '../../../components/ui/Card/Card';
import Button from '../../../components/ui/Button/Button';
import styles from './ExamList.module.css';

const ExamList = () => {
  const [exams, setExams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState('all');
  const navigate = useNavigate();

  useEffect(() => {
    fetchExams();
  }, [filter]);

  const fetchExams = async () => {
    setLoading(true);
    try {
      // API call would go here
      await new Promise(resolve => setTimeout(resolve, 1000));
      setExams([
        {
          id: 1,
          title: 'Indian States Geography',
          description: 'Comprehensive test on Indian states geography',
          duration: 60,
          totalQuestions: 50,
          difficulty: 'medium',
          category: 'Geography'
        },
        // ... more exams
      ]);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className={styles.loader}>Loading exams...</div>;
  }

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1 className={styles.title}>Available Exams</h1>
        <div className={styles.filters}>
          {['all', 'geography', 'history', 'culture'].map(f => (
            <button
              key={f}
              className={`${styles.filterBtn} ${filter === f ? styles.active : ''}`}
              onClick={() => setFilter(f)}
            >
              {f.charAt(0).toUpperCase() + f.slice(1)}
            </button>
          ))}
        </div>
      </div>

      <div className={styles.grid}>
        {exams.map(exam => (
          <Card key={exam.id} hoverable className={styles.examCard}>
            <div className={styles.cardContent}>
              <div className={styles.examHeader}>
                <h3 className={styles.examTitle}>{exam.title}</h3>
                <span className={`${styles.badge} ${styles[exam.difficulty]}`}>
                  {exam.difficulty}
                </span>
              </div>

              <p className={styles.description}>{exam.description}</p>

              <div className={styles.info}>
                <div className={styles.infoItem}>
                  <FaClock />
                  <span>{exam.duration} min</span>
                </div>
                <div className={styles.infoItem}>
                  <FaQuestionCircle />
                  <span>{exam.totalQuestions} questions</span>
                </div>
                <div className={styles.infoItem}>
                  <FaStar />
                  <span>{exam.category}</span>
                </div>
              </div>

              <Button
                fullWidth
                onClick={() => navigate(`/exam/${exam.id}`)}
              >
                Start Exam
              </Button>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default ExamList;
