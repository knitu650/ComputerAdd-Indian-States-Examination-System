
self.addEventListener('message', async (event) => {
  const { type, imageData } = event.data;
  
  if (type === 'PROCESS_FRAME') {
    try {
      const processed = await processFrame(imageData);
      self.postMessage({ type: 'FRAME_PROCESSED', data: processed });
    } catch (error) {
      self.postMessage({ type: 'PROCESSING_ERROR', error: error.message });
    }
  }
});

async function processFrame(imageData) {
  // Image processing logic
  // Could include face detection, image compression, etc.
  
  return {
    processed: true,
    timestamp: Date.now(),
    data: imageData
  };
}
