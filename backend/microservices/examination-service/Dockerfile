# Base image
FROM node:18-alpine

# Create app directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy app source
COPY ./src ./src

# Expose port
EXPOSE 8082

# Start command
CMD [ "npm", "start" ]