# Frontend Dockerfile - Development
FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Expose port
EXPOSE 5173

# Run development server with hot reload
CMD ["npm", "run", "dev", "--", "--host"]
