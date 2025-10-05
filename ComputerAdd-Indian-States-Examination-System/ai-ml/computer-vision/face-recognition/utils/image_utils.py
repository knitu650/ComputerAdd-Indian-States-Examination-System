import cv2
import numpy as np
from PIL import Image

class ImageUtils:
    """Image processing utilities for face recognition"""
    
    @staticmethod
    def resize_image(image, target_size=(224, 224)):
        """Resize image to target size"""
        return cv2.resize(image, target_size)
    
    @staticmethod
    def normalize_image(image):
        """Normalize image to 0-1 range"""
        return image.astype('float32') / 255.0
    
    @staticmethod
    def crop_face(image, bbox):
        """Crop face region from image"""
        x, y, w, h = bbox
        return image[y:y+h, x:x+w]
    
    @staticmethod
    def pad_image(image, target_size):
        """Pad image to target size maintaining aspect ratio"""
        old_size = image.shape[:2]
        ratio = min(target_size[0]/old_size[0], target_size[1]/old_size[1])
        new_size = tuple([int(x*ratio) for x in old_size])
        
        im = cv2.resize(image, (new_size[1], new_size[0]))
        
        delta_w = target_size[1] - new_size[1]
        delta_h = target_size[0] - new_size[0]
        top, bottom = delta_h//2, delta_h-(delta_h//2)
        left, right = delta_w//2, delta_w-(delta_w//2)
        
        color = [0, 0, 0]
        new_im = cv2.copyMakeBorder(im, top, bottom, left, right, 
                                    cv2.BORDER_CONSTANT, value=color)
        
        return new_im
    
    @staticmethod
    def augment_image(image):
        """Apply random augmentations"""
        # Random rotation
        angle = np.random.randint(-15, 15)
        M = cv2.getRotationMatrix2D((image.shape[1]//2, image.shape[0]//2), angle, 1)
        image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
        
        # Random brightness
        value = np.random.randint(-30, 30)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        v = cv2.add(v, value)
        final_hsv = cv2.merge((h, s, v))
        image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        
        return image
