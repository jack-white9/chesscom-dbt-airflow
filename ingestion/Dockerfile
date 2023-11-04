# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the .env file into the container
COPY .env .env

# Install any dependencies from requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Specify the command to run your Python application
CMD ["python", "main.py"]
