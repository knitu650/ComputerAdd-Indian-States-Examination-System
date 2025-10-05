import time
import numpy as np
from queue import Queue
from threading import Thread

class RealTimeInferencePipeline:
    """Real-time inference pipeline for proctoring"""
    
    def __init__(self, models):
        self.models = models
        self.input_queue = Queue(maxsize=100)
        self.output_queue = Queue(maxsize=100)
        self.is_running = False
        
        self.inference_thread = None
    
    def start(self):
        """Start inference pipeline"""
        self.is_running = True
        self.inference_thread = Thread(target=self._inference_loop)
        self.inference_thread.start()
        
        print("Real-time inference pipeline started")
    
    def stop(self):
        """Stop inference pipeline"""
        self.is_running = False
        if self.inference_thread:
            self.inference_thread.join()
        
        print("Real-time inference pipeline stopped")
    
    def process_frame(self, frame):
        """Add frame to processing queue"""
        if not self.input_queue.full():
            self.input_queue.put({
                'frame': frame,
                'timestamp': time.time()
            })
    
    def get_results(self, timeout=1.0):
        """Get inference results"""
        try:
            return self.output_queue.get(timeout=timeout)
        except:
            return None
    
    def _inference_loop(self):
        """Main inference loop"""
        while self.is_running:
            try:
                # Get input
                data = self.input_queue.get(timeout=1.0)
                
                frame = data['frame']
                timestamp = data['timestamp']
                
                # Run inference
                results = self._run_inference(frame)
                
                # Add timestamp
                results['timestamp'] = timestamp
                results['latency'] = time.time() - timestamp
                
                # Put results
                if not self.output_queue.full():
                    self.output_queue.put(results)
                
            except:
                continue
    
    def _run_inference(self, frame):
        """Run all models on frame"""
        results = {}
        
        # Face detection
        if 'face_detector' in self.models:
            faces = self.models['face_detector'].detect_faces(frame)
            results['num_faces'] = len(faces)
            results['faces'] = faces
        
        # Object detection
        if 'object_detector' in self.models:
            objects = self.models['object_detector'].detect_objects(frame)
            results['objects'] = objects
            results['has_unauthorized_objects'] = len(objects) > 0
        
        # Pose analysis
        if 'pose_analyzer' in self.models:
            pose = self.models['pose_analyzer'].analyze_pose(frame)
            results['pose'] = pose
            if pose:
                results['looking_away'] = pose.get('is_looking_away', False)
        
        # Behavior analysis
        if 'behavior_detector' in self.models:
            behavior = self.models['behavior_detector'].analyze_frame(results)
            results['behavior'] = behavior
        
        return results

if __name__ == '__main__':
    models = {}
    pipeline = RealTimeInferencePipeline(models)
    print("Real-time inference pipeline initialized")
