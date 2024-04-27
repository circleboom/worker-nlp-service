# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libffi-dev \
    libssl-dev \
    python3-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /usr/src/app
COPY nlp_service/requirements.txt ./

# Pre-install Cython to avoid compilation issues during spaCy installation
RUN pip install Cython

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install spaCy and download the model
RUN python -m spacy download xx_ent_wiki_sm

# Copy the rest of the application
COPY nlp_service/ ./

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME NLP_Service

# Start Gunicorn with the Flask application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]