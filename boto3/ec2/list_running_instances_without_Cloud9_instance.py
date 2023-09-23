import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Define a filter to include only running instances
running_instances_filter = [{'Name': 'instance-state-name', 'Values': ['running']}]

# Define a filter to exclude instances with a specific tag indicating AWS Cloud9 hosting
exclude_cloud9_instances_filter = [{'Name': 'tag:Name', 'Values': ['*aws-cloud9*']}]

# Combine the filters using logical AND to get instances that are running and not hosting AWS Cloud9
combined_filter = running_instances_filter exclude_cloud9_instances_filter

# Describe EC2 instances with the combined filter
response = ec2.describe_instances(Filters=running_instances_filter,exclude_cloud9_instances_filter)

# Process the response data
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
