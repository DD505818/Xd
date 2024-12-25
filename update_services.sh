#!/bin/bash

# Update services on Google Cloud Run
update_google_cloud_run() {
  echo "Updating Google Cloud Run service..."
  gcloud run services update my-service --image gcr.io/my-project/my-image:latest
  echo "Google Cloud Run service updated."
}

# Update services on GKE
update_gke() {
  echo "Updating GKE service..."
  kubectl set image deployment/my-deployment my-container=gcr.io/my-project/my-image:latest
  kubectl rollout status deployment/my-deployment
  echo "GKE service updated."
}

# Update services on OpenShift
update_openshift() {
  echo "Updating OpenShift service..."
  oc set image deployment/my-deployment my-container=quay.io/my-project/my-image:latest
  oc rollout status deployment/my-deployment
  echo "OpenShift service updated."
}

# Main function to update all services
main() {
  update_google_cloud_run
  update_gke
  update_openshift
}

main
