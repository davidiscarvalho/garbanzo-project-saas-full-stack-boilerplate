# Use an official Node.js image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy the package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the application code
COPY . .

# Build the frontend
RUN npm run build

# Expose the app on port 3000
EXPOSE 3000

# Serve the app
CMD ["npm", "start"]
