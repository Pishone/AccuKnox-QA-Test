# AccuKnox QA Test

## Overview
This project is an assigment given by AccuKnox Hiring team. It shows the automation testing using integration of Selenium (Python) and PyTest deployed in a Kubernetes (Kubectl) cluster. It includes setup instruction for deploying and testing the given web application.

## Prerequisites
- Ubuntu System
- Python 3.x
- Docker
- Kubernetes (for deployment)
- kubectl (Kubernetes CLI)

## Installation and Setup
### Kubernetes Setup
1. **Install minikube**: Follow the [official minikube installation guide](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download) to install minikube on your system.
   
2. **Install kubectl**:
   - For Linux (x86-64):
     ```bash
        curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
     ```
   - For others, follow the instructions [here](https://kubernetes.io/docs/tasks/tools/).

3. **Start Kubernetes Cluster**:
   - You can start a local Kubernetes cluster using minikube by
    '''bash
        minikube start
    '''

### Project Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>
