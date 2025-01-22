# Use Ubuntu as base image for better Ollama compatibility
FROM ubuntu:22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies and Python
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y \
    python3.12 \
    python3.12-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install pip for Python 3.12 and upgrade it
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12 && \
    python3.12 -m pip install --upgrade pip

# Copy the project
COPY . .

# Install project dependencies with force-reinstall to handle distutils packages
RUN python3.12 -m pip install --ignore-installed --force-reinstall -e .

# Install Ollama (this requires Ubuntu/Debian)
RUN curl -fsSL https://ollama.com/install.sh | sh

# The Ollama model pull should be done at runtime, not build time
# because it requires the Ollama service to be running

# Run app.py when the container launches
ENTRYPOINT ["python3.12", "app.py"]
