# Step by Step
1. docker build -t fastapi-app:latest .
2. docker container run --publish 8080:80 --name fastapi-app-container fastapi-app
3. If you want to see the container's files: docker exec -it fastapi-app-container ls -l {subfolder}
4. GET /users
5. If works local, deploy API on Heroku or Glitch
