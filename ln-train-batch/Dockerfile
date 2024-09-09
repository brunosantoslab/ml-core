FROM jupyter/scipy-notebook:latest

# Set environment variables to avoid writing .pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER root

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies using pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --prefer-binary

# Copy the application code and test files to the working directory
COPY src/ ./src/
COPY tests/ ./tests/

# Ensure the /tmp directory exists and has the correct permissions
RUN mkdir -p /tmp && chmod 777 /tmp

# Default command to start a Jupyter Notebook server for running and testing your code
CMD ["start.sh", "jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
