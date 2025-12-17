# Use official Python image
FROM python:3.12.0

# Set working directory inside container
WORKDIR /app

# Copy requirements if you have them
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Run FastAPI with uvicorn when container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
