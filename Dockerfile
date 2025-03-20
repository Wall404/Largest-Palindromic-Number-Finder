
### Docker Setup

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install pipenv
RUN pip install pipenv

# Install the dependencies in the Pipfile
RUN pipenv install --deploy --ignore-pipfile

# Expose the port for the app (if applicable, based on your app)
EXPOSE 8000

# Define the command to run your app
CMD ["pipenv", "run", "python", "app.py"]
