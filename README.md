# Project Title: Dockerized Python NLP Service

## Description

This project implements a Python-based NLP service using Flask and spaCy, containerized with Docker. It is designed to extract keywords from provided text, supporting multiple languages. The service is deployed using Gunicorn as the WSGI server for production environments.

## Features

- **Keyword Extraction**: Extract keywords from input text using [spaCy](https://github.com/explosion/spaCy).
- **Multi-language Support**: Uses the spaCy 'xx_ent_wiki_sm' model to support multiple languages.
- **Dockerized Application**: Containerized with Docker for easy deployment and scalability.
- **Production-Ready**: Includes Gunicorn for production-level deployments.

## Requirements

- Docker
- Any system that supports Docker (Windows/Linux/Mac)

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/circleboom/worker-nlp-service.git
   cd nlp-service

2. **Build the Docker Image:**:
    ```bash
    docker build -t nlp-service .
    ```

3. **Run the Docker Container:**
    ```bash
    docker run -p 4000:5000 nlp-service
    ```

This command runs the Docker container, mapping port 5000 in the container to port 4000 on the host.

##Usage

Send a POST request to the service to extract keywords:

```bash
curl -X POST http://localhost:4000/extract_keywords \
     -H "Content-Type: application/json" \
     -d '{"text": "Your text here"}'
```

###Using the Service with C#
Refer to the C# code snippet provided in the integration section to setup and call this service from a C# application.

##Development

###Local Setup
For local development without Docker:

1. Ensure Python 3.8+ is installed.
2. Install dependencies:
    ```bash
    Copy code
    pip install -r requirements.txt
    python3 -m spacy download xx_ent_wiki_sm
    ```
3. Run the Flask app locally:
    ```bash
    Copy code
    python3 run.py
    ```
###Adding New Features
* Extend the service by adding new routes or integrating more NLP features from spaCy.
* Update the spaCy model or switch to a different model for enhanced accuracy or different capabilities.

## Running Tests

To ensure that all features function as intended and to prevent regressions, we have a comprehensive test suite. Follow these steps to run the tests:

### Setup
Before running the tests, make sure that you have the project's dependencies installed and your virtual environment activated. If you haven't set up the virtual environment or installed the dependencies, refer to the Installation section of this README.

### Executing Tests
We use `pytest` for running tests due to its simplicity and powerful features. To execute the tests, follow these steps:

1. *Navigate to the Project Root*:

    Ensure you are in the root directory of the project where the pytest configuration files (`pytest.ini` or `conftest.py`) are located.
2. *Run Pytest*:
    
    Execute the following command in your terminal:
    ```bash
    python3 -m pytest
    ```
    This command will discover and run all test cases in the `tests` directory.

### What the Tests Cover
The tests are designed to cover:

* Basic functionality of all routes.
* Integration tests to ensure different parts of the application work together correctly.
* Edge cases and error handling scenarios.

### Test Output
`pytest` will provide a detailed report for each test, indicating whether it passed or failed. Review the output to ensure all tests pass. If a test fails, `pytest` will provide a detailed error that can be used to diagnose and resolve the issue.

### Continuous Integration
This project is configured to run these tests automatically via Continuous Integration (CI) tools every time changes are pushed to the repository. Ensure that all tests pass before pushing to ensure seamless integration and deployment.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with new features or fixes. For major changes, please open an issue first to discuss what you would like to change.

Ensure to update tests as appropriate.

## Disclaimer

This project was created with the help of an AI, ChatGPT 4, developed by OpenAI, designed to assist in software development and other intellectual tasks.

