Robotics Fleet Management Platform - DevOps Assignment
Overview

This project was developed as part of the KION DevOps Assignment.

The objective was to design, containerize and prepare a robotics-related application for deployment in a production Kubernetes environment while demonstrating DevOps best practices around automation, testing, security, monitoring and deployment.

The application simulates a Robotics Fleet Management Platform where Autonomous Guided Vehicles (AGVs) can be monitored through REST APIs and a web dashboard.
-----------------------------------------------------------------------------
Project Architecture

Application Stack:

Python Flask Application
HTML/CSS Dashboard
Docker Containerization
Kubernetes Deployment Manifests
GitHub Actions CI Pipeline
Prometheus Monitoring Configuration
-----------------------------------------------------------------------------
Project Structure:

robotics-devops-assignment/

├── app/

├── docker/

├── k8s/

├── monitoring/

├── .github/workflows/

├── docs/

└── README.md
-----------------------------------------------------------------------------
Development Approach

I started with a simple Flask application exposing health check endpoints and gradually enhanced it to resemble a small production-ready service.

Phase 1 – Application Development (FOR PHASE -1 --> Took help of AI using - Demo Project)
Created REST APIs for:

Health Status
Robot Fleet Information
Application Metrics
Application Version Information
Monitoring Endpoint

Implemented a Robotics Fleet Dashboard to visualize:

Active Robots
Charging Robots
Platform Health
Deployment Version
Fleet Status Table

---------------
Phase 2 – Testing
Implemented automated unit tests using Pytest.
All tests are executed automatically during CI pipeline execution.

------------------
Phase 3 – Containerization
Containerized the application using Docker.
I have used Slim image to reduce the size of Docker image
Used No-root user instead of root for security purpose
So Image built is light weight
Docker validation completeded locally
# Run
docker build -t robotics-app -f docker/Dockerfile .
docker build -t robotics-app -f docker/Dockerfile .
-----------------
Phase 4 – Kubernetes Deployment
Created Kubernetes manifests files created which consists Deployment, Service, ingress:
- 2 Replicas, Rolling update strategy, Environment variables, probes
- Exposing application internally through ClusterIP
- Ingress resource configured for external access & TLS configuration is also included in it.
-----------------
AI Usage

AI tools were used for guidance, troubleshooting and reviewing implementation approaches.

All configurations, code changes, testing and validation were performed manually before finalizing the solution.
---------------------------------------------------------------------------------

Running the Application Locally

Install dependencies:

pip install -r app/requirements.txt

Start application:

python app/app.py

Application will be available at:

http://localhost:5000
----------------------
Running Unit Tests

Execute:

pytest app/test_app.py

All test cases should pass successfully.
----------------------
Docker Implementation

Build Docker image:

docker build -t robotics-app -f docker/Dockerfile .

Run container:

docker run -d -p 5000:5000 --name robotics-dashboard robotics-app

The container runs using a non-root user following container security best practices.
----------------------