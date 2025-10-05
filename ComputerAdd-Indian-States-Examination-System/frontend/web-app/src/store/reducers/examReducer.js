import { createSlice } from '@reduxjs/toolkit';

const examSlice = createSlice({
  name: 'exam',
  initialState: {
    currentExam: null,
    questions: [],
    currentQuestionIndex: 0,
    answers: {}
  },
  reducers: {
    setCurrentExam: (state, action) => {
      state.currentExam = action.payload;
    },
    setQuestions: (state, action) => {
      state.questions = action.payload;
    },
    saveAnswer: (state, action) => {
      const { questionId, answer } = action.payload;
      state.answers[questionId] = answer;
    },
    nextQuestion: (state) => {
      if (state.currentQuestionIndex < state.questions.length - 1) {
        state.currentQuestionIndex += 1;
      }
    }
  }
});

export const { setCurrentExam, setQuestions, saveAnswer, nextQuestion } = examSlice.actions;
export default examSlice.reducer;
