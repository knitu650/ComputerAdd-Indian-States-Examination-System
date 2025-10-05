const redis = require('redis');
const { logger } = require('../utils/logger');

/**
 * Redis Configuration and Client
 * Handles caching and session management
 */

let redisClient = null;

const createRedisClient = async () => {
  try {
    // Create Redis client
    const client = redis.createClient({
      url: process.env.REDIS_URL || 'redis://localhost:6379',
      socket: {
        reconnectStrategy: (retries) => {
          if (retries > 10) {
            logger.error('Redis max reconnection attempts reached');
            return new Error('Redis reconnection failed');
          }
          const delay = Math.min(retries * 100, 3000);
          logger.warn(`Redis reconnecting in ${delay}ms...`);
          return delay;
        }
      }
    });

    // Event handlers
    client.on('error', (err) => {
      logger.error('Redis error:', err);
    });

    client.on('connect', () => {
      logger.info('Redis client connecting...');
    });

    client.on('ready', () => {
      logger.info('✅ Redis client ready');
    });

    client.on('reconnecting', () => {
      logger.warn('Redis client reconnecting...');
    });

    client.on('end', () => {
      logger.info('Redis client disconnected');
    });

    // Connect to Redis
    await client.connect();

    redisClient = client;
    return client;

  } catch (error) {
    logger.error('Failed to create Redis client:', error);
    throw error;
  }
};

/**
 * Get Redis client instance
 */
const getRedisClient = () => {
  if (!redisClient) {
    throw new Error('Redis client not initialized');
  }
  return redisClient;
};

/**
 * Redis Helper Functions
 */

const RedisHelper = {
  /**
   * Set key-value with optional expiry
   */
  async set(key, value, expirySeconds = null) {
    try {
      const client = getRedisClient();
      const stringValue = typeof value === 'object' ? JSON.stringify(value) : String(value);
      
      if (expirySeconds) {
        await client.setEx(key, expirySeconds, stringValue);
      } else {
        await client.set(key, stringValue);
      }
      
      return true;
    } catch (error) {
      logger.error('Redis SET error:', error);
      return false;
    }
  },

  /**
   * Get value by key
   */
  async get(key) {
    try {
      const client = getRedisClient();
      const value = await client.get(key);
      
      if (!value) return null;
      
      // Try to parse as JSON
      try {
        return JSON.parse(value);
      } catch {
        return value;
      }
    } catch (error) {
      logger.error('Redis GET error:', error);
      return null;
    }
  },

  /**
   * Delete key
   */
  async del(key) {
    try {
      const client = getRedisClient();
      await client.del(key);
      return true;
    } catch (error) {
      logger.error('Redis DEL error:', error);
      return false;
    }
  },

  /**
   * Check if key exists
   */
  async exists(key) {
    try {
      const client = getRedisClient();
      const result = await client.exists(key);
      return result === 1;
    } catch (error) {
      logger.error('Redis EXISTS error:', error);
      return false;
    }
  },

  /**
   * Set expiry on key
   */
  async expire(key, seconds) {
    try {
      const client = getRedisClient();
      await client.expire(key, seconds);
      return true;
    } catch (error) {
      logger.error('Redis EXPIRE error:', error);
      return false;
    }
  },

  /**
   * Increment counter
   */
  async incr(key) {
    try {
      const client = getRedisClient();
      return await client.incr(key);
    } catch (error) {
      logger.error('Redis INCR error:', error);
      return null;
    }
  },

  /**
   * Add to set
   */
  async sadd(key, ...members) {
    try {
      const client = getRedisClient();
      return await client.sAdd(key, members);
    } catch (error) {
      logger.error('Redis SADD error:', error);
      return false;
    }
  },

  /**
   * Get set members
   */
  async smembers(key) {
    try {
      const client = getRedisClient();
      return await client.sMembers(key);
    } catch (error) {
      logger.error('Redis SMEMBERS error:', error);
      return [];
    }
  },

  /**
   * Add to hash
   */
  async hset(key, field, value) {
    try {
      const client = getRedisClient();
      const stringValue = typeof value === 'object' ? JSON.stringify(value) : String(value);
      await client.hSet(key, field, stringValue);
      return true;
    } catch (error) {
      logger.error('Redis HSET error:', error);
      return false;
    }
  },

  /**
   * Get from hash
   */
  async hget(key, field) {
    try {
      const client = getRedisClient();
      const value = await client.hGet(key, field);
      
      if (!value) return null;
      
      try {
        return JSON.parse(value);
      } catch {
        return value;
      }
    } catch (error) {
      logger.error('Redis HGET error:', error);
      return null;
    }
  },

  /**
   * Get all hash fields
   */
  async hgetall(key) {
    try {
      const client = getRedisClient();
      return await client.hGetAll(key);
    } catch (error) {
      logger.error('Redis HGETALL error:', error);
      return {};
    }
  },

  /**
   * Delete pattern matching keys
   */
  async deletePattern(pattern) {
    try {
      const client = getRedisClient();
      const keys = await client.keys(pattern);
      
      if (keys.length > 0) {
        await client.del(keys);
      }
      
      return keys.length;
    } catch (error) {
      logger.error('Redis DELETE PATTERN error:', error);
      return 0;
    }
  },

  /**
   * Flush database (use with caution)
   */
  async flushdb() {
    try {
      const client = getRedisClient();
      await client.flushDb();
      logger.warn('Redis database flushed');
      return true;
    } catch (error) {
      logger.error('Redis FLUSHDB error:', error);
      return false;
    }
  }
};

/**
 * Close Redis connection
 */
const closeRedis = async () => {
  try {
    if (redisClient) {
      await redisClient.quit();
      logger.info('Redis connection closed');
    }
  } catch (error) {
    logger.error('Error closing Redis connection:', error);
  }
};

// Initialize Redis on import
createRedisClient().catch(err => {
  logger.error('Failed to initialize Redis:', err);
});

module.exports = {
  createRedisClient,
  getRedisClient,
  RedisHelper,
  closeRedis,
  // Export client directly for middleware compatibility
  get: RedisHelper.get.bind(RedisHelper),
  set: RedisHelper.set.bind(RedisHelper),
  del: RedisHelper.del.bind(RedisHelper)
};
