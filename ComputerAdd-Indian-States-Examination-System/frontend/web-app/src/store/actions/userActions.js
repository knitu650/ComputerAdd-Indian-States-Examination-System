export const USER_ACTIONS = {
  GET_PROFILE_REQUEST: 'GET_PROFILE_REQUEST',
  GET_PROFILE_SUCCESS: 'GET_PROFILE_SUCCESS',
  GET_PROFILE_FAILURE: 'GET_PROFILE_FAILURE',
  
  UPDATE_PROFILE_REQUEST: 'UPDATE_PROFILE_REQUEST',
  UPDATE_PROFILE_SUCCESS: 'UPDATE_PROFILE_SUCCESS',
  UPDATE_PROFILE_FAILURE: 'UPDATE_PROFILE_FAILURE',
  
  UPLOAD_AVATAR_REQUEST: 'UPLOAD_AVATAR_REQUEST',
  UPLOAD_AVATAR_SUCCESS: 'UPLOAD_AVATAR_SUCCESS',
  UPLOAD_AVATAR_FAILURE: 'UPLOAD_AVATAR_FAILURE',
};

export const getProfile = () => async (dispatch, getState, { userService }) => {
  dispatch({ type: USER_ACTIONS.GET_PROFILE_REQUEST });
  
  try {
    const response = await userService.getProfile();
    dispatch({
      type: USER_ACTIONS.GET_PROFILE_SUCCESS,
      payload: response.data
    });
  } catch (error) {
    dispatch({
      type: USER_ACTIONS.GET_PROFILE_FAILURE,
      payload: error.response?.data?.message || error.message
    });
  }
};

export const updateProfile = (data) => async (dispatch, getState, { userService }) => {
  dispatch({ type: USER_ACTIONS.UPDATE_PROFILE_REQUEST });
  
  try {
    const response = await userService.updateProfile(data);
    dispatch({
      type: USER_ACTIONS.UPDATE_PROFILE_SUCCESS,
      payload: response.data
    });
  } catch (error) {
    dispatch({
      type: USER_ACTIONS.UPDATE_PROFILE_FAILURE,
      payload: error.response?.data?.message || error.message
    });
  }
};

export const uploadAvatar = (file) => async (dispatch, getState, { userService }) => {
  dispatch({ type: USER_ACTIONS.UPLOAD_AVATAR_REQUEST });
  
  try {
    const response = await userService.uploadAvatar(file);
    dispatch({
      type: USER_ACTIONS.UPLOAD_AVATAR_SUCCESS,
      payload: response.data
    });
  } catch (error) {
    dispatch({
      type: USER_ACTIONS.UPLOAD_AVATAR_FAILURE,
      payload: error.response?.data?.message || error.message
    });
  }
};
