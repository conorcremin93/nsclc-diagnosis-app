# Base image with Python 3.11
FROM python:3.11-slim

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git wget curl build-essential libssl-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy scripts and notebooks
COPY scripts/ ./scripts/
COPY notebooks/ ./notebooks/

# Create directories for models, notebooks, outputs
RUN mkdir -p /app/models /app/outputs

# Set default command to just start a shell
CMD ["/bin/bash"]
