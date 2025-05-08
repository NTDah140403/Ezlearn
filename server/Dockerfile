# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (for some Python packages like OpenCV, etc.)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libgl1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file and install Python packages
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Set environment variables (OPTIONAL - Cloud Run can override these)
ENV MODULE_NAME="main"
ENV VARIABLE_NAME="app"
ENV APP_MODULE="${MODULE_NAME}:${VARIABLE_NAME}"

# Cloud Run expects the app to listen on PORT=8080
ENV PORT=8080

# Expose port 8080 (required by Cloud Run)
EXPOSE 8080

# Start the server using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
