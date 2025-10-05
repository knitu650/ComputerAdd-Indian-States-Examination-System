# Base image
FROM node:18-alpine

# Create app directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy app source
COPY ./src ./src

# Environment variables
# The .env file should be managed securely, not copied directly
# For development, you can mount it as a volume in docker-compose

# Expose port
EXPOSE 8081

# Start command
CMD [ "npm", "start" ]