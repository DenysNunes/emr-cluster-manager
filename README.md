# emr-cluster-manager

A simple tool for EMR cluster management. 

 !!! Work in progress !!!

Action Plan:

* Web Api (tornado or flask based) to manager clusters
* Cluster Lifecycle
* Cluster configurations based on a database
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

Without any this configurations, will be used a default role configurations (Like running EC2 instance)