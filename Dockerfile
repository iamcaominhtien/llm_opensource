# Python image to use.
FROM python:3.12-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the entire project first
COPY . .

# Install build dependencies and pip tools
RUN apk add --no-cache gcc musl-dev && \
    pip install --upgrade pip setuptools wheel

# Install project dependencies
RUN pip install -e .

# Run app.py when the container launches
ENTRYPOINT ["python", "app.py"]
