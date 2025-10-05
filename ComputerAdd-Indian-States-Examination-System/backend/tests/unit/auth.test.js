const request = require('supertest');
const app = require('../../microservices/user-service/src/app');
const User = require('../../microservices/user-service/src/models/User');

describe('Authentication Tests', () => {
  
  beforeEach(async () => {
    await User.deleteMany({});
  });
  
  describe('POST /api/v1/auth/register', () => {
    it('should register a new user', async () => {
      const userData = {
        email: 'test@example.com',
        password: 'Test123!@#',
        profile: {
          firstName: 'Test',
          lastName: 'User',
          dateOfBirth: '1995-01-01',
          gender: 'male'
        }
      };
      
      const res = await request(app)
        .post('/api/v1/auth/register')
        .send(userData);
      
      expect(res.status).toBe(201);
      expect(res.body.success).toBe(true);
      expect(res.body.data).toHaveProperty('token');
    });
    
    it('should not register with duplicate email', async () => {
      const userData = {
        email: 'test@example.com',
        password: 'Test123!@#',
        profile: { firstName: 'Test', lastName: 'User' }
      };
      
      await request(app).post('/api/v1/auth/register').send(userData);
      
      const res = await request(app)
        .post('/api/v1/auth/register')
        .send(userData);
      
      expect(res.status).toBe(400);
      expect(res.body.success).toBe(false);
    });
  });
  
  describe('POST /api/v1/auth/login', () => {
    it('should login with valid credentials', async () => {
      // First register
      await request(app).post('/api/v1/auth/register').send({
        email: 'test@example.com',
        password: 'Test123!@#',
        profile: { firstName: 'Test', lastName: 'User' }
      });
      
      // Then login
      const res = await request(app)
        .post('/api/v1/auth/login')
        .send({
          email: 'test@example.com',
          password: 'Test123!@#'
        });
      
      expect(res.status).toBe(200);
      expect(res.body.success).toBe(true);
      expect(res.body.data).toHaveProperty('token');
    });
    
    it('should not login with invalid password', async () => {
      await request(app).post('/api/v1/auth/register').send({
        email: 'test@example.com',
        password: 'Test123!@#',
        profile: { firstName: 'Test', lastName: 'User' }
      });
      
      const res = await request(app)
        .post('/api/v1/auth/login')
        .send({
          email: 'test@example.com',
          password: 'WrongPassword'
        });
      
      expect(res.status).toBe(401);
      expect(res.body.success).toBe(false);
    });
  });
});
