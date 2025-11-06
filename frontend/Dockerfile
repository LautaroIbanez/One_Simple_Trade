# Dockerfile for frontend (minimal, for development)
FROM node:20-alpine

WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

# Copy dependency files
COPY package.json pnpm-lock.yaml* ./

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy application code
COPY . .

# Expose port
EXPOSE 5173

# Run development server
CMD ["pnpm", "dev", "--host", "0.0.0.0"]


