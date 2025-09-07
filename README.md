# DevOps CI/CD Pipeline Project

A complete DevOps automation solution demonstrating modern CI/CD practices with containerization and cloud native deployment strategies.

## Project Structure

```
devops-cicd-project/
├── .github/
│   └── workflows/
│       └── workflow.yml
├── .tekton/
│   └── tasks.yml
├── src/
│   ├── app.py
│   └── __init__.py
├── tests/
│   ├── test_app.py
│   └── __init__.py
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── requirements.txt
├── Dockerfile
└── README.md
```

## Technologies Used

### Core Application
- **Python 3.9**: Primary programming language
- **Flask**: Lightweight web framework
- **Gunicorn**: WSGI HTTP server

### Testing & Quality
- **Nose**: Unit testing framework
- **Flake8**: Code linting and style checking
- **Coverage**: Code coverage analysis
- **Pytest**: Additional testing support

### CI/CD Pipeline
- **GitHub Actions**: Continuous integration and deployment
- **Tekton**: Kubernetes native CI/CD pipelines
- **Docker**: Application containerization

### Infrastructure
- **OpenShift**: Container orchestration platform
- **Kubernetes**: Container deployment and management
- **PersistentVolumeClaim**: Storage management

## Features

- Automated code quality checks
- Comprehensive unit testing
- Container based deployment
- Health monitoring endpoints
- Production ready configuration
- Scalable architecture

## Quick Start

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run application: `python src/app.py`
4. Execute tests: `nosetests tests/`

## API Endpoints

- `GET /` - Application status
- `GET /health` - Health check
- `GET /info` - Environment information

## Deployment

The application is containerized and ready for deployment on OpenShift clusters with automated CI/CD pipelines handling the entire deployment lifecycle.