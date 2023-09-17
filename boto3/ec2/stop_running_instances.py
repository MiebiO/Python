import boto3

# Initialize the Boto3 EC2 client
ec2 = boto3.client('ec2')

# Initialize an empty list to store the running instance IDs
instances_running = []

cloud9_instances_filter = [{'Name': 'tag:Name', 'Values': ['*aws-cloud9*']}]


# Describe EC2 instances that are in the 'running' state
response = ec2.describe_instances(
    Filters=[
        {'Name': 'instance-state-name', 'Values': ['running']}
    ])

# Iterate through reservations and instances in the response
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
                instances_running.append(instance["InstanceId"])

#Describe EC2 instances that are running AWS Cloud9
response = ec2.describe_instances(Filters=cloud9_instances_filter)

#Remove AWS Cloud9 instances from the instances_running list
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
                instances_running.remove(instance["InstanceId"])
                
# Print the list of running Development environment instances
print('This is a list of the running Development environment instances: ', instances_running)

response = ec2.describe_instances
# Check if there are no running instances
if instances_running == []:
    print('No running instances to be stopped')
else:
    # Stop the running instances using their IDs
    ec2.stop_instances(InstanceIds=instances_running)
    print("All running instances stopped")
