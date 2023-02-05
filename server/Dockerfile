# Use an existing Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the server script
COPY server.py .

# Expose the default port for Flask (5000)
EXPOSE 5000

# Set the entrypoint command
ENTRYPOINT ["python", "server.py"]