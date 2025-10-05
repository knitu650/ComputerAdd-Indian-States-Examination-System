import axios from 'axios';

const API_URL = '/api/v1/exams';

export const examService = {
  getAllExams: async () => {
    const response = await axios.get(API_URL);
    return response.data;
  },

  getExamById: async (id) => {
    const response = await axios.get(`${API_URL}/${id}`);
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

  getResults: async (examId) => {
    const response = await axios.get(`${API_URL}/${examId}/results`);
    return response.data;
  }
};
