import axios from 'axios';
import authService from '../../services/api/auth.service';

const apiMiddleware = () => next => action => {
  // Add auth token to axios requests
  const token = authService.getToken();
  if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  }

  // Handle token expiration
  axios.interceptors.response.use(
    response => response,
    error => {
      if (error.response?.status === 401) {
        authService.logout();
        window.location.href = '/login';
      }
      return Promise.reject(error);
    }
  );

  return next(action);
};

export default apiMiddleware;
