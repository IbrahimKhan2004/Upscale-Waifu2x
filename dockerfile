# Use a base image with Python installed
FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the code to the container
COPY . .

# Command to run when the container starts
CMD ["python", "main.py"]
