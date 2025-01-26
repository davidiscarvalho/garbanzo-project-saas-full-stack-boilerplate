#!/bin/bash

echo "Testing Backend API..."
curl -I http://localhost:8000

if [ $? -eq 0 ]; then
  echo "Backend API is reachable!"
else
  echo "Error: Could not reach Backend API."
fi

echo "Testing PostgreSQL connection..."
docker exec -it postgres psql -U your_postgres_user -c '\l'

if [ $? -eq 0 ]; then
  echo "PostgreSQL connection is working!"
else
  echo "Error: Could not connect to PostgreSQL."
fi
