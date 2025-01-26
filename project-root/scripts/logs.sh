#!/bin/bash

# Get the service name from the user
SERVICE=$1

if [ -z "$SERVICE" ]; then
  echo "Usage: ./logs.sh [service_name]"
  exit 1
fi

# Display logs for the specified service
docker-compose logs -f $SERVICE
