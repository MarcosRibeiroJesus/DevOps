# Basic Syntax
name = "Marcos"
count = 5
active = True
if active:
    print(f"User {name} has {count} active sessions")

# Functions
def greet(user):
    return f"Hello, {user}!"
print(greet("Marcos"))

# File Operations
with open("output.log", "w") as f:
    f.write("Deployment completed\n")

# Shell Commands
import subprocess
result = subprocess.run(["df", "-h"], capture_output=True, text=True)
print(result.stdout)

# Environment Variables
import os
region = os.getenv("AWS_REGION", "us-east-1")
os.environ["ENV"] = "production"

# AWS with boto3
import boto3
ec2 = boto3.client("ec2")
instances = ec2.describe_instances()
for r in instances["Reservations"]:
    for i in r["Instances"]:
        print(i["InstanceId"], i["State"]["Name"])

# JSON & YAML
import json, yaml
data = {"name": "Marcos", "env": "prod"}
print(json.dumps(data, indent=2))
print(yaml.dump(data))

# Logging
import logging
logging.basicConfig(filename="app.log", level=logging.INFO)
logging.info("Service started")

# Argparse (CLI Arguments)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--env", help="Environment name")
args = parser.parse_args()
print(f"Deploying to {args.env}")

# Restart EC2 Instances by Tag
import boto3
ec2 = boto3.client("ec2")
instances = ec2.describe_instances(Filters=[{"Name": "tag:Environment", "Values": ["dev"]}])
ids = [i["InstanceId"] for r in instances["Reservations"] for i in r["Instances"]]
if ids:
    ec2.reboot_instances(InstanceIds=ids)
    print("Rebooted:", ids)
