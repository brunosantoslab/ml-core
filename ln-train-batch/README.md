# Linear Regression Training Batch

This project implements a **Linear Regression Training Batch** system. Initially, it focuses on **simple linear regression** using a single variable as the predictor. In future updates, the model will be extended to handle **multiple variables** for regression (multiple linear regression).

## Overview

This project is structured to train and deploy a linear regression model using batch processing. The current implementation uses a single independent variable (predictor) to model the relationship with the dependent variable (target). The system processes incoming data files in a batch manner and updates the model accordingly.

Future versions will incorporate multiple predictor variables to expand the capabilities of the model to handle more complex data and batch processing using S3 events/ AWS Lambda to start the training as soon as the files are uploaded to the S3 bucket.

### Key Features
- **Single-variable linear regression** (simple linear regression).
- Designed to process CSV data from S3.
- Configured to use Docker for local development and testing.
- Easily extensible to support multiple regression in future versions.

## Project Structure

```
/ln-train-batch
│
├── Dockerfile                # Docker image definition for development environment
├── docker-compose.yml        # Docker Compose configuration for running local services
├── requirements.txt          # Python dependencies for the project
├── .env.example              # Environment variables file
├── src/                      # Source code for the application
├── tests/                    # Unit tests
└── README.md                 # Project documentation
```

## Getting Started

### Prerequisites

Ensure the following are installed on your machine:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **AWS CLI**: [Install AWS CLI](https://aws.amazon.com/cli/)
- **Python 3.12**: [Install Python](https://www.python.org/downloads/)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ln-train-batch.git
   cd ln-train-batch
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root of the project, following the structure in the `.env.example`:
   ```env
   AWS_ACCESS_KEY_ID=your-access-key
   AWS_SECRET_ACCESS_KEY=your-secret-key
   AWS_REGION=your-region
   S3_BUCKET_NAME=your-s3-bucket-name
   LOCAL_DATA_PATH=./tmp/input_data
   MODEL_OUTPUT_PATH=./tmp/output_data
   LOG_LEVEL=DEBUG
   PYTHONPATH=/app/src
   ```

### Running Locally

#### Using Docker Compose

1. **Build and run the services**:
   ```bash
   docker-compose up --build
   ```

#### Running Tests

1. **Run tests using Docker**:
   ```bash
   docker exec -it ln-train-batch-app pytest
   ```

2. **Clean up Docker containers**:
   ```bash
   docker-compose down
   ```

### Future Updates

This project will be expanded to support **multiple variable linear regression**. This will involve updating the model to handle more complex relationships between variables, and batch processing using S3 events/ AWS Lambda to start the training as soon as the files are uploaded to the S3 bucket.

## Troubleshooting

- **S3 Bucket Issues**: Ensure the S3 bucket name used in the template is globally unique and exists.
- **Docker Build Errors**: If you encounter issues while building Docker images, ensure you have sufficient permissions and disk space.

## Contributing

Feel free to submit issues, pull requests, and suggestions to improve the project. All contributions are welcome as we work to add more features to this regression model system.