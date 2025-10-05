module.exports = {
  async up(db) {
    // Users collection
    await db.collection('users').createIndex({ email: 1 }, { unique: true });
    await db.collection('users').createIndex({ 'profile.firstName': 1, 'profile.lastName': 1 });
    await db.collection('users').createIndex({ createdAt: -1 });
    
    // Exams collection
    await db.collection('exams').createIndex({ isActive: 1, createdAt: -1 });
    await db.collection('exams').createIndex({ category: 1 });
    await db.collection('exams').createIndex({ 'settings.difficulty': 1 });
    
    // Results collection
    await db.collection('results').createIndex({ userId: 1, examId: 1 });
    await db.collection('results').createIndex({ examId: 1, percentage: -1 });
    await db.collection('results').createIndex({ createdAt: -1 });
    
    console.log('Indexes created successfully');
  },
  
  async down(db) {
    await db.collection('users').dropIndexes();
    await db.collection('exams').dropIndexes();
    await db.collection('results').dropIndexes();
  }
};
