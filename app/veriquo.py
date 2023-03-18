import requests

# Prompt the user for input values
api_key = input("Enter Qovery API key: ")
project_id = input("Enter Qovery project ID: ")
rule_name = input("Enter Deployment Rule name: ")
rule_mode = input("Enter Deployment Rule mode: ")
cluster_id = input("Enter cluster ID to deploy to: ")
auto_deploy = input("Enable auto-deploy? (y/n): ")
auto_delete = input("Enable auto-delete? (y/n): ")
start_hour = input("Enter start hour (in UTC): ")
start_minute = input("Enter start minute (in UTC): ")
end_hour = input("Enter end hour (in UTC): ")
end_minute = input("Enter end minute (in UTC): ")
environment_names = input(
    "Enter environment names to target (comma-separated): ").split(',')

# Build the request payload
payload = {
    "name": rule_name,
    "mode": rule_mode,
    "deployment": {
        "auto_deploy": auto_deploy.lower() == 'y',
        "auto_delete": auto_delete.lower() == 'y',
        "schedule": {
            "start_hour": start_hour,
            "start_minute": start_minute,
            "end_hour": end_hour,
            "end_minute": end_minute,
        },
        "clusters": [
            cluster_id,
        ]
    },
    "environment_ids": [],
}

# Get the list of environments in the project
headers = {"Authorization": f"Bearer {api_key}"}
url = f"https://api.qovery.com/registry/v1/projects/{project_id}/environments"
response = requests.get(url, headers=headers)
environments = response.json()

# Find the IDs of the environments to target
for env in environments:
    if env["name"] in environment_names:
        payload["environment_ids"].append(env["id"])

# Make the API call to create the Deployment Rule
url = f"https://api.qovery.com/registry/v1/projects/{project_id}/deployment_rules"
response = requests.post(url, headers=headers, json=payload)

# Check if the API call was successful
if response.status_code == 200:
    print("Deployment Rule created successfully!")
else:
    print(f"Error creating Deployment Rule: {response.text}")
