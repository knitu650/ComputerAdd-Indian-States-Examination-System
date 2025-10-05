import cv2
import numpy as np

class ImageEnhancer:
    """Enhance image quality"""
    
    @staticmethod
    def enhance_contrast(image):
        """Enhance image contrast using CLAHE"""
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        
        limg = cv2.merge((cl,a,b))
        enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        
        return enhanced
    
    @staticmethod
    def enhance_brightness(image, alpha=1.0, beta=50):
        """Adjust brightness and contrast"""
        return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    
    @staticmethod
    def sharpen_image(image):
        """Sharpen image"""
        kernel = np.array([[-1,-1,-1],
                          [-1, 9,-1],
                          [-1,-1,-1]])
        return cv2.filter2D(image, -1, kernel)
    
    @staticmethod
    def denoise_image(image):
        """Remove noise from image"""
        return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
