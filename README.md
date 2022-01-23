# WIP: emr-cluster-manager

A simple tool for EMR cluster management. 

!!! Work in progress !!!

Action Plan:

* Web Api to manager clusters
* Cluster Lifecycle
* Running Cluster over configurations
* Spark Optimizations
* Docker Image
* Configuration with Dynaconf
* Powered by boto3
* Integration with Airflow

# Configuration

Set .secret.toml with this configurations:

aws_profile = "value"

or 

aws_access_key = "value"
aws_secret_key = "value"

Without any this configurations, will be used a default role configurations (running in EC2 instance)
