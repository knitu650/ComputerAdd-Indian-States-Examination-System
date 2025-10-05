import ReactNativeBiometrics from 'react-native-biometrics';

const rnBiometrics = new ReactNativeBiometrics();

export const BiometricService = {
  /**
   * Check if biometric authentication is available
   */
  async isBiometricAvailable() {
    try {
      const { available, biometryType } = await rnBiometrics.isSensorAvailable();
      return { available, type: biometryType };
    } catch (error) {
      console.error('Biometric check failed:', error);
      return { available: false, type: null };
    }
  },

  /**
   * Authenticate using biometric
   */
  async authenticate(promptMessage = 'Authenticate to continue') {
    try {
      const { success } = await rnBiometrics.simplePrompt({
        promptMessage,
        cancelButtonText: 'Cancel',
      });

      return { success };
    } catch (error) {
      console.error('Biometric authentication failed:', error);
      return { success: false, error: error.message };
    }
  },

  /**
   * Create signature for secure operations
   */
  async createSignature(payload) {
    try {
      const { success, signature } = await rnBiometrics.createSignature({
        promptMessage: 'Sign in',
        payload: payload,
      });

      return { success, signature };
    } catch (error) {
      console.error('Signature creation failed:', error);
      return { success: false };
    }
  },
};
