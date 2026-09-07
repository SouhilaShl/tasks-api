# Tasks API

A simple REST API for managing tasks, built with FastAPI.
This project demonstrates a secure CI/CD pipeline with automated
testing and vulnerability scanning.

## Features

- Create a task
- Retrieve a task by ID
- Health check endpoint

## Tech stack

- Python 3.12
- FastAPI
- Docker
- pytest for testing
- Trivy for vulnerability scanning

## Running locally

Install dependencies and start the server:

    pip install -r requirements.txt
    uvicorn app.main:app --reload

Then open http://localhost:8000/docs to explore the API.

## Running the tests

    pytest

## Running with Docker

    docker build -t tasks-api .
    docker run -p 8000:8000 tasks-api