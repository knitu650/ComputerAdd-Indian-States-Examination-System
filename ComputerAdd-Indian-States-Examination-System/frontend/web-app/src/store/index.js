import { configureStore } from '@reduxjs/toolkit';
import authReducer from './reducers/authReducer';
import examReducer from './reducers/examReducer';

const store = configureStore({
  reducer: {
    auth: authReducer,
    exam: examReducer
  }
});

export default store;
