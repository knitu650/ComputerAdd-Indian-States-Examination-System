import React, { useState } from 'react';
import { FaSearchPlus, FaSearchMinus } from 'react-icons/fa';
import styles from './ImageBasedQuestion.module.css';

const ImageBasedQuestion = ({ question, answer, onAnswer }) => {
  const [zoom, setZoom] = useState(1);
  const [lightbox, setLightbox] = useState(false);

  return (
    <div className={styles.container}>
      <h3 className={styles.question}>{question.text}</h3>
      
      <div className={styles.imageContainer}>
        <img 
          src={question.image} 
          alt="Question" 
          className={styles.image}
          style={{ transform: `scale(${zoom})` }}
          onClick={() => setLightbox(true)}
        />
        
        <div className={styles.zoomControls}>
          <button 
            onClick={() => setZoom(Math.min(zoom + 0.25, 2))}
            className={styles.zoomBtn}
          >
            <FaSearchPlus />
          </button>
          <button 
            onClick={() => setZoom(Math.max(zoom - 0.25, 0.5))}
            className={styles.zoomBtn}
          >
            <FaSearchMinus />
          </button>
        </div>
      </div>

      <div className={styles.options}>
        {question.options.map((option, index) => (
          <button
            key={index}
            className={`${styles.option} ${answer === option ? styles.selected : ''}`}
            onClick={() => onAnswer(option)}
          >
            <span className={styles.optionLabel}>{String.fromCharCode(65 + index)}.</span>
            {option}
          </button>
        ))}
      </div>

      {lightbox && (
        <div className={styles.lightbox} onClick={() => setLightbox(false)}>
          <img src={question.image} alt="Enlarged" className={styles.lightboxImage} />
        </div>
      )}
    </div>
  );
};

export default ImageBasedQuestion;
