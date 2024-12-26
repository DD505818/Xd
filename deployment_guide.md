# Deployment Guide

## Google Cloud Run

### Prerequisites
1. Enable the following Google Cloud APIs:
   - Artifact Registry (artifactregistry.googleapis.com)
   - Cloud Run (run.googleapis.com)
   - IAM Credentials API (iamcredentials.googleapis.com)
2. Create and configure a Workload Identity Provider for GitHub.
3. Grant the necessary IAM permissions:
   - Artifact Registry Administrator (roles/artifactregistry.admin)
   - Cloud Run Developer (roles/run.developer)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/DD505818/Xd.git
   cd Xd
   ```
2. Set up the environment variables in the `.github/workflows/google-cloudrun-docker.yml` file.
3. Commit and push the changes to the `main` branch.
4. The GitHub Actions workflow will automatically build and deploy the application to Google Cloud Run.

## Google Kubernetes Engine (GKE)

### Prerequisites
1. Enable the following Google Cloud APIs:
   - Artifact Registry (artifactregistry.googleapis.com)
   - Google Kubernetes Engine (container.googleapis.com)
   - IAM Credentials API (iamcredentials.googleapis.com)
2. Ensure that your repository contains the necessary configuration for your GKE cluster, including `deployment.yml`, `kustomization.yml`, `service.yml`, etc.
3. Create and configure a Workload Identity Provider for GitHub.
4. Grant the necessary IAM permissions:
   - Artifact Registry Administrator (roles/artifactregistry.admin)
   - Kubernetes Engine Developer (roles/container.developer)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/DD505818/Xd.git
   cd Xd
   ```
2. Set up the environment variables in the `.github/workflows/google.yml` file.
3. Commit and push the changes to the `main` branch.
4. The GitHub Actions workflow will automatically build and deploy the application to GKE.

## OpenShift

### Prerequisites
1. Have access to an OpenShift cluster.
2. Create the `OPENSHIFT_SERVER` and `OPENSHIFT_TOKEN` repository secrets.
3. (Optional) Edit the top-level 'env' section in the `.github/workflows/openshift.yml` file if the defaults are not suitable for your project.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/DD505818/Xd.git
   cd Xd
   ```
2. Set up the environment variables in the `.github/workflows/openshift.yml` file.
3. Commit and push the changes to the `main` branch.
4. The GitHub Actions workflow will automatically build and deploy the application to OpenShift.

## Setting Up Environment Variables in Workflow Files

### Google Cloud Run
1. Open the `.github/workflows/google-cloudrun-docker.yml` file.
2. Update the following environment variables with your values:
   - `PROJECT_ID`: Your Google Cloud project ID
   - `REGION`: Your region
   - `SERVICE`: Your service name
   - `WORKLOAD_IDENTITY_PROVIDER`: Your workload identity provider

### Google Kubernetes Engine (GKE)
1. Open the `.github/workflows/google.yml` file.
2. Update the following environment variables with your values:
   - `PROJECT_ID`: Your Google Cloud project ID
   - `GAR_LOCATION`: Your region
   - `GKE_CLUSTER`: Your cluster name
   - `GKE_ZONE`: Your cluster zone
   - `DEPLOYMENT_NAME`: Your deployment name
   - `REPOSITORY`: Your Artifact Registry docker repository name
   - `IMAGE`: Your image name
   - `WORKLOAD_IDENTITY_PROVIDER`: Your workload identity provider

### OpenShift
1. Open the `.github/workflows/openshift.yml` file.
2. Update the following environment variables with your values:
   - `OPENSHIFT_SERVER`: Your OpenShift server URL
   - `OPENSHIFT_TOKEN`: Your OpenShift token
   - `OPENSHIFT_NAMESPACE`: Your namespace
   - `APP_NAME`: Your app name
   - `APP_PORT`: Your app port
   - `IMAGE_REGISTRY`: Your image registry
   - `IMAGE_REGISTRY_USER`: Your image registry username
   - `IMAGE_REGISTRY_PASSWORD`: Your image registry password
