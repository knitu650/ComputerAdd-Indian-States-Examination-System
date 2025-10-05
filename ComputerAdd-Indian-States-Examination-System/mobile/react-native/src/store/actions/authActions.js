export const LOGIN_REQUEST = 'LOGIN_REQUEST';
export const LOGIN_SUCCESS = 'LOGIN_SUCCESS';
export const LOGIN_FAILURE = 'LOGIN_FAILURE';
export const LOGOUT = 'LOGOUT';
export const SET_USER = 'SET_USER';

import { authApi } from '../../services/api/authApi';

export const login = (email, password) => async (dispatch) => {
  try {
    dispatch({ type: LOGIN_REQUEST });
    
    const response = await authApi.login(email, password);
    
    dispatch({
      type: LOGIN_SUCCESS,
      payload: {
        user: response.data.user,
        token: response.data.token,
      },
    });
    
    return response;
  } catch (error) {
    dispatch({
      type: LOGIN_FAILURE,
      payload: error.message,
    });
    throw error;
  }
};

export const logout = () => async (dispatch) => {
  await authApi.logout();
  dispatch({ type: LOGOUT });
};

export const setUser = (user) => ({
  type: SET_USER,
  payload: user,
});
