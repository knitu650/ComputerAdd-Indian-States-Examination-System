import axios from 'axios';
import authService from './auth.service';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const getAuthHeader = () => ({
  headers: {
    Authorization: `Bearer ${authService.getToken()}`
  }
});

class AnalyticsService {
  async getUserPerformance(userId) {
    const response = await axios.get(
      `${API_URL}/analytics/performance/${userId}`,
      getAuthHeader()
    );
    return response.data;
  }

  async getDashboardStats() {
    const response = await axios.get(
      `${API_URL}/analytics/dashboard`,
      getAuthHeader()
    );
    return response.data;
  }

  async getStateWiseAnalysis(userId) {
    const response = await axios.get(
      `${API_URL}/analytics/state-wise/${userId}`,
      getAuthHeader()
    );
    return response.data;
  }

  async getProgressReport(userId, startDate, endDate) {
    const response = await axios.get(
      `${API_URL}/analytics/progress/${userId}`,
      {
        ...getAuthHeader(),
        params: { startDate, endDate }
      }
    );
    return response.data;
  }

  async exportReport(userId, format = 'pdf') {
    const response = await axios.get(
      `${API_URL}/analytics/export/${userId}`,
      {
        ...getAuthHeader(),
        params: { format },
        responseType: 'blob'
      }
    );
    return response.data;
  }
}

export default new AnalyticsService();
