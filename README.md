# AccuKnox QA Test

## Overview
This project is an assigment given by AccuKnox Hiring team. It shows the automation testing using integration of Selenium (Python) and PyTest deployed in a Kubernetes (Kubectl) cluster. It includes setup instruction for deploying and testing the given web application.

## Prerequisites
- Ubuntu System
- Python 3.x
- Docker
- Kubernetes (for deployment)
- kubectl (Kubernetes CLI)
- Selenium

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
    ```bash
        minikube start
    ```

### Project Setup
1. **Clone the Repository**:
    Clone both the sample application repo: 
   ```bash
    git clone https://github.com/Vengatesh-m/qa-test.git
    cd qa-test/Deployment
    ```
    And this repo which contains the test scripts:
    ```bash
    git clone https://github.com/Pishone/AccuKnox-QA-Test.git
    cd AccuKnox-QA-Test/
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Deploy YAML files**
    ```bash
    kubectl apply -f frontend-deployment.yaml
    kubectl apply -f backend-deployment.yaml
    ```

4. **Access the Frontend Service**
   To find the url of the frontend service, use
    ```bash
    minikube service frontend-deployment --url
    ```
    Access the resulting URL. Verify if the application is working. You'd see the text "Hello from the Backend!"

5. **Running Tests using PyTest**
    With dependencies installed, application deployed in K8, you can start running selenium tests using PyTest.
    ```bash
    pytest -v -s --html=report.html
    ```