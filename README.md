


# SpotifyDataSearcherAPI - A Containerized FastAPI Application 

## Introduction

Just a FastAPI wrapper for SpotifyAPI search function for. It uses Github Actions to contanarize and publish app on Azure

## Prerequisites
Before proceeding with the deployment, make sure you have the following:

- A FastAPI application that you want to deploy.
- An Azure account with appropriate permissions to create and manage resources.
- Docker installed on your local machine.
- GitHub repository containing your FastAPI application code.

## Workflow Description
The deployment process consists of the following steps:

1. **GitHub Actions Setup**: Configure a GitHub Actions workflow to automate the deployment process.
2. **Login via Azure CLI**: Authenticate with Azure CLI to access Azure resources.
3. **Build and Push Docker Image**: Build the Docker image for the FastAPI application and push it to the Azure Container Registry.
4. **Deploy to Azure Container Instances**: Deploy the Docker image to Azure Container Instances (ACI) using the azure/aci-deploy action.

## Deployment Instructions

### 1. Configure GitHub Actions Workflow
Create a GitHub Actions workflow file (e.g., `.github/workflows/deploy.yml`) in your repository with the provided content.

### 2. Set Up Secrets
In your GitHub repository, go to `Settings` > `Secrets` and add the required secrets mentioned in the workflow.

## Conclusion
By following these instructions, you should be able to automate the deployment of your FastAPI application to Azure Container Instances using GitHub Actions. If you encounter any issues, refer to the troubleshooting section or consult the Azure documentation for additional assistance.

