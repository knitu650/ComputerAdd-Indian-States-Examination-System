#!/bin/bash
echo "💾 Starting backup..."

# Backup MongoDB
mongodump --uri="$MONGODB_URI" --out=backups/mongodb-$(date +%Y%m%d)

# Backup PostgreSQL
pg_dump $POSTGRES_URI > backups/postgres-$(date +%Y%m%d).sql

echo "✅ Backup complete!"
