import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()

for route in response["RouteTables"]:
    print(route["RouteTableId"],route["VpcId"])
    for assoc in route["Associations"]:
        print(assoc["RouteTableAssociationId"])
        if "SubnetId" in assoc:
            print(assoc["SubnetId"])