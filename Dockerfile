# Use Python 3.10-slim as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first, to leverage Docker layer caching
COPY requirements.txt .

# Install any necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
