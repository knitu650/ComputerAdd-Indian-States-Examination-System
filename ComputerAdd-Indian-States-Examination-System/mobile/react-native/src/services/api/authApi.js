import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

const API_URL = 'http://localhost:8000/api/v1/auth';

export const authApi = {
  login: async (email, password) => {
    const response = await axios.post(`${API_URL}/login`, {
      email,
      password,
    });
    
    if (response.data.success) {
      await AsyncStorage.setItem('authToken', response.data.data.token);
      axios.defaults.headers.common['Authorization'] = 
        `Bearer ${response.data.data.token}`;
    }
    
    return response.data;
  },

  register: async (userData) => {
    const response = await axios.post(`${API_URL}/register`, userData);
    return response.data;
  },

  logout: async () => {
    await AsyncStorage.removeItem('authToken');
    delete axios.defaults.headers.common['Authorization'];
  },

  getStoredToken: async () => {
    return await AsyncStorage.getItem('authToken');
  },
};
