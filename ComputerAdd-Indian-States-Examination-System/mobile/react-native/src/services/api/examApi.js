import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1/exams';

export const examApi = {
  getAllExams: async () => {
    const response = await axios.get(API_URL);
    return response.data;
  },

  getExamById: async (examId) => {
    const response = await axios.get(`${API_URL}/${examId}`);
    return response.data;
  },

  startExam: async (examId) => {
    const response = await axios.post(`${API_URL}/${examId}/start`);
    return response.data;
  },

  submitAnswer: async (examId, questionId, answer) => {
    const response = await axios.post(
      `${API_URL}/${examId}/questions/${questionId}/answer`,
      { answer }
    );
    return response.data;
  },

  submitExam: async (examId) => {
    const response = await axios.post(`${API_URL}/${examId}/submit`);
    return response.data;
  },
};
