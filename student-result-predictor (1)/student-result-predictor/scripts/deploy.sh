#!/bin/bash
set -e

APP_DIR="/home/ubuntu/student-result-predictor"

echo "Starting deployment..."
cd "$APP_DIR"

echo "Stopping old container if it exists..."
sudo docker rm -f student-app || true

echo "Building the new image..."
sudo docker build -t student-app .

echo "Starting the application..."
sudo docker run -d \
  --name student-app \
  --restart unless-stopped \
  -p 80:5000 \
  student-app

echo "Checking application health..."
for i in {1..30}; do
    if curl -fsS http://127.0.0.1/ > /dev/null; then
        echo "Deployment successful."
        exit 0
    fi
    sleep 2
done

echo "Application did not become healthy."
sudo docker logs student-app
exit 1
