import { useSelector, useDispatch } from 'react-redux';
import { login as loginAction, logout as logoutAction } from '../store/actions/authActions';

export const useAuth = () => {
  const dispatch = useDispatch();
  const { user, token, isAuthenticated, loading } = useSelector(state => state.auth);

  const login = async (email, password) => {
    return await dispatch(loginAction(email, password));
  };

  const logout = () => {
    dispatch(logoutAction());
  };

  return {
    user,
    token,
    isAuthenticated,
    loading,
    login,
    logout,
  };
};
