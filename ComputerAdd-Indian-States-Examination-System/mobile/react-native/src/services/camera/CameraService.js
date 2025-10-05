import { Camera } from 'react-native-camera';
import { PermissionsAndroid, Platform } from 'react-native';

export const CameraService = {
  /**
   * Request camera permission
   */
  async requestCameraPermission() {
    if (Platform.OS === 'android') {
      try {
        const granted = await PermissionsAndroid.request(
          PermissionsAndroid.PERMISSIONS.CAMERA,
          {
            title: 'Camera Permission',
            message: 'App needs access to your camera for proctoring',
            buttonNeutral: 'Ask Me Later',
            buttonNegative: 'Cancel',
            buttonPositive: 'OK',
          },
        );
        return granted === PermissionsAndroid.RESULTS.GRANTED;
      } catch (err) {
        console.warn(err);
        return false;
      }
    }
    return true;
  },

  /**
   * Capture image from camera
   */
  async captureImage(cameraRef) {
    if (cameraRef && cameraRef.current) {
      try {
        const options = { quality: 0.7, base64: true };
        const data = await cameraRef.current.takePictureAsync(options);
        return data;
      } catch (error) {
        console.error('Failed to capture image:', error);
        return null;
      }
    }
    return null;
  },

  /**
   * Start video recording
   */
  async startRecording(cameraRef) {
    if (cameraRef && cameraRef.current) {
      try {
        const promise = cameraRef.current.recordAsync({
          quality: Camera.Constants.VideoQuality['480p'],
        });
        return promise;
      } catch (error) {
        console.error('Failed to start recording:', error);
        return null;
      }
    }
    return null;
  },

  /**
   * Stop video recording
   */
  stopRecording(cameraRef) {
    if (cameraRef && cameraRef.current) {
      cameraRef.current.stopRecording();
    }
  },
};
