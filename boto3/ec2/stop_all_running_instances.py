import boto3

# Initialize the Boto3 EC2 client
ec2 = boto3.client('ec2')

# Define a dictionary for the desired tag for filtering instances
dev_tag = {"Key": "Environment", "Value": "Dev"}

# Initialize an empty list to store the running instance IDs
instances_running = []

# Describe EC2 instances that are in the 'running' state
response = ec2.describe_instances(
    Filters=[
        {'Name': 'instance-state-name', 'Values': ['running']}
    ])

# Iterate through reservations and instances in the response
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # Check if the 'Tags' key exists in the instance metadata
        if "Tags" in instance.keys():
            # Check if the desired 'Environment' tag is present
            if dev_tag in instance['Tags']:
                # Append the instance ID to the list
                instances_running.append(instance["InstanceId"])

# Print the list of running Development environment instances
print('This is a list of the running Development environment instances: ', instances_running)

# Check if there are no running instances
if instances_running == []:
    print('No running instances to be stopped')
else:
    # Stop the running instances using their IDs
    ec2.stop_instances(InstanceIds=instances_running)
    print("All running instances stopped")
