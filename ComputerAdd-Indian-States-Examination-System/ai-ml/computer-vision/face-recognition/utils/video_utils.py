import cv2
import numpy as np

class VideoUtils:
    """Video processing utilities"""
    
    @staticmethod
    def extract_frames(video_path, fps=1):
        """Extract frames from video at specified fps"""
        cap = cv2.VideoCapture(video_path)
        frames = []
        
        frame_interval = int(cap.get(cv2.CAP_PROP_FPS) / fps)
        frame_count = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            if frame_count % frame_interval == 0:
                frames.append(frame)
            
            frame_count += 1
        
        cap.release()
        return frames
    
    @staticmethod
    def save_video(frames, output_path, fps=30):
        """Save frames as video"""
        if not frames:
            return
        
        height, width = frames[0].shape[:2]
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        for frame in frames:
            out.write(frame)
        
        out.release()
    
    @staticmethod
    def process_video_stream(cap, processor_func):
        """Process video stream with custom function"""
        results = []
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            result = processor_func(frame)
            results.append(result)
        
        return results
