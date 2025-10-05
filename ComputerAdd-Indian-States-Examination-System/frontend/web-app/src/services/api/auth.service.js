import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

class AuthService {
  async register(userData) {
    const response = await axios.post(`${API_URL}/auth/register`, userData);
    if (response.data.data.token) {
      localStorage.setItem('token', response.data.data.token);
      localStorage.setItem('user', JSON.stringify(response.data.data.user));
    }
    return response.data;
  }

  async login(credentials) {
    const response = await axios.post(`${API_URL}/auth/login`, credentials);
    if (response.data.data.token) {
      localStorage.setItem('token', response.data.data.token);
      localStorage.setItem('user', JSON.stringify(response.data.data.user));
    }
    return response.data;
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  }

  async forgotPassword(email) {
    return axios.post(`${API_URL}/auth/forgot-password`, { email });
  }

  async resetPassword(token, password) {
    return axios.post(`${API_URL}/auth/reset-password`, { token, password });
  }

  async verifyEmail(token) {
    return axios.get(`${API_URL}/verification/email/verify/${token}`);
  }

  getToken() {
    return localStorage.getItem('token');
  }

  getUser() {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
  }

  isAuthenticated() {
    return !!this.getToken();
  }
}

export default new AuthService();
