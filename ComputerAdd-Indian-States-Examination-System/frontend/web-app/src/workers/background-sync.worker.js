
self.addEventListener('message', (event) => {
  const { type, payload } = event.data;
  
  switch (type) {
    case 'SYNC_ANSWERS':
      syncAnswers(payload);
      break;
    case 'SYNC_PROGRESS':
      syncProgress(payload);
      break;
    default:
      console.log('Unknown message type:', type);
  }
});

async function syncAnswers(data) {
  try {
    const response = await fetch('/api/v1/exams/sync-answers', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    });
    
    if (response.ok) {
      self.postMessage({ type: 'SYNC_SUCCESS', payload: await response.json() });
    } else {
      self.postMessage({ type: 'SYNC_ERROR', payload: 'Sync failed' });
    }
  } catch (error) {
    self.postMessage({ type: 'SYNC_ERROR', payload: error.message });
  }
}

async function syncProgress(data) {
  // Implement progress sync logic
  self.postMessage({ type: 'PROGRESS_SYNCED', payload: data });
}
