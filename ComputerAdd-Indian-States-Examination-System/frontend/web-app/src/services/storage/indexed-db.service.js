class IndexedDBService {
  constructor() {
    this.dbName = 'ExamPortalDB';
    this.version = 1;
    this.db = null;
  }

  async init() {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.dbName, this.version);

      request.onerror = () => reject(request.error);
      request.onsuccess = () => {
        this.db = request.result;
        resolve(this.db);
      };

      request.onupgradeneeded = (event) => {
        const db = event.target.result;

        // Create object stores
        if (!db.objectStoreNames.contains('answers')) {
          db.createObjectStore('answers', { keyPath: 'id', autoIncrement: true });
        }

        if (!db.objectStoreNames.contains('exams')) {
          db.createObjectStore('exams', { keyPath: 'id' });
        }

        if (!db.objectStoreNames.contains('cache')) {
          db.createObjectStore('cache', { keyPath: 'key' });
        }
      };
    });
  }

  async saveAnswer(examId, questionId, answer) {
    if (!this.db) await this.init();

    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['answers'], 'readwrite');
      const store = transaction.objectStore('answers');
      
      const request = store.put({
        examId,
        questionId,
        answer,
        timestamp: Date.now()
      });

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  async getAnswers(examId) {
    if (!this.db) await this.init();

    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['answers'], 'readonly');
      const store = transaction.objectStore('answers');
      const request = store.getAll();

      request.onsuccess = () => {
        const answers = request.result.filter(a => a.examId === examId);
        resolve(answers);
      };
      request.onerror = () => reject(request.error);
    });
  }

  async clearAnswers(examId) {
    if (!this.db) await this.init();

    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['answers'], 'readwrite');
      const store = transaction.objectStore('answers');
      const request = store.clear();

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }
}

export default new IndexedDBService();
