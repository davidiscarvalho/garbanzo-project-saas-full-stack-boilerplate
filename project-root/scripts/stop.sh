#!/bin/bash

# Stop Docker Compose
echo "Stopping Docker containers..."
docker-compose down

# Check if containers stopped successfully
if [ $? -eq 0 ]; then
  echo "Containers stopped successfully!"
else
  echo "Error: Could not stop containers."
fi
