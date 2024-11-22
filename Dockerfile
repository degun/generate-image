# Use the official lightweight Python image
FROM python:3.11-slim-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.6.1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:$PATH"

# Install system dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        build-essential \
        curl \
        libffi-dev \
        libssl-dev \
        libjpeg-dev \
        zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set the working directory
WORKDIR /app

# Copy only the Poetry lock file and project file
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --only main

COPY . .

EXPOSE 2013
