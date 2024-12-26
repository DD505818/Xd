# Deployment Instructions

## Google Cloud Run

1. Ensure the necessary Google Cloud APIs are enabled:
   - Artifact Registry
   - Cloud Run
   - IAM Credentials API

2. Create and configure a Workload Identity Provider for GitHub.

3. Update the `.github/workflows/google-cloudrun-docker.yml` file with your project-specific values.

4. Push your changes to the main branch to trigger the deployment workflow.

## Google Kubernetes Engine (GKE)

1. Ensure the necessary Google Cloud APIs are enabled:
   - Artifact Registry
   - Google Kubernetes Engine
   - IAM Credentials API

2. Ensure your repository contains the necessary configuration for your GKE cluster.

3. Create and configure a Workload Identity Provider for GitHub.

4. Update the `.github/workflows/google.yml` file with your project-specific values.

5. Push your changes to the main branch to trigger the deployment workflow.

## OpenShift

1. Ensure you have access to an OpenShift cluster.

2. Create the `OPENSHIFT_SERVER` and `OPENSHIFT_TOKEN` repository secrets.

3. Update the `.github/workflows/openshift.yml` file with your project-specific values.

4. Push your changes to the main branch to trigger the deployment workflow.

## Running `deploy.sh` Script

1. Ensure the `api_keys.json` file is properly configured with your API keys and secrets.

2. Run the `deploy.sh` script to set up the virtual environment, install dependencies, and configure environment variables.

3. The alert system, confirmation signals, risk management, and trade execution modules will be deployed as part of the `deploy.sh` script.

## Configuring `api_keys.json`

1. Open the `api_keys.json` file.

2. Add your API keys and secrets in the following format:

```json
{
    "binance": {
        "api_key": "your_binance_api_key",
        "api_secret": "your_binance_api_secret"
    },
    "slack": {
        "webhook_url": "your_slack_webhook_url"
    }
}
```

3. Save the file.
