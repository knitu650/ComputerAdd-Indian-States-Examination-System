import { useSelector, useDispatch } from 'react-redux';
import { setUser, setToken, logout as logoutAction } from '../store/reducers/authReducer';
import axios from 'axios';

export const useAuth = () => {
  const { user, token, isAuthenticated } = useSelector(state => state.auth);
  const dispatch = useDispatch();

  const login = async (email, password) => {
    try {
      const response = await axios.post('/api/v1/auth/login', { email, password });
      dispatch(setUser(response.data.data.user));
      dispatch(setToken(response.data.data.token));
      return response.data;
    } catch (error) {
      throw error;
    }
  };

  const logout = () => {
    dispatch(logoutAction());
  };

  return { user, token, isAuthenticated, login, logout };
};
