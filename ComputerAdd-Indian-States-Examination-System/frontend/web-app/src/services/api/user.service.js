import axios from 'axios';
import authService from './auth.service';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const getAuthHeader = () => ({
  headers: {
    Authorization: `Bearer ${authService.getToken()}`
  }
});

class UserService {
  async getProfile() {
    const response = await axios.get(`${API_URL}/profile`, getAuthHeader());
    return response.data;
  }

  async updateProfile(data) {
    const response = await axios.put(`${API_URL}/profile`, data, getAuthHeader());
    return response.data;
  }

  async uploadAvatar(file) {
    const formData = new FormData();
    formData.append('avatar', file);
    
    const response = await axios.post(
      `${API_URL}/profile/avatar`, 
      formData,
      {
        ...getAuthHeader(),
        headers: {
          ...getAuthHeader().headers,
          'Content-Type': 'multipart/form-data'
        }
      }
    );
    return response.data;
  }

  async changePassword(currentPassword, newPassword) {
    const response = await axios.post(
      `${API_URL}/auth/change-password`,
      { currentPassword, newPassword },
      getAuthHeader()
    );
    return response.data;
  }

  async deleteAccount() {
    const response = await axios.delete(`${API_URL}/profile`, getAuthHeader());
    return response.data;
  }
}

export default new UserService();
