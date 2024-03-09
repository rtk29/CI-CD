# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /application

# Copy the requiremnets file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . /application

# Expose the port on which the application will run
EXPOSE 8000

# Run the FASTAPI application using the uvicorn server.
CMD ["uvicorn", "fastapi-main:app", "--host", "0.0.0.0", "--port", "8080"]

