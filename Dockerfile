FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all Python files to the working directory
COPY *.py .

# Specify the command to run the application
CMD ["python", "main.py"]