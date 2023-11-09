# Base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code into container
COPY app /app/app

# Expose port 80
EXPOSE 80

# Start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]