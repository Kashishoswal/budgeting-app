# Dockerfile

# Start with a lightweight official Python image as a base
FROM python:3.10-slim

# Set the folder where our app will live inside the container
WORKDIR /app

# Copy the dependencies file first to take advantage of Docker's layer caching
COPY requirements.txt .

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of our application code (app.py, static folder, etc.) into the container
COPY . .

# Tell Docker that the container will listen on port 5000
EXPOSE 5000

# The command to run when the container starts
CMD ["python", "app.py"]
