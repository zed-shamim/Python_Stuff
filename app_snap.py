#!/usr/local/aws/bin/python
import boto3
from datetime import date,time,timedelta
snplist = []
owner='994432210064'
t=18 
client = boto3.client('ec2')

response = client.describe_snapshots(Filters=[{'Name': 'description', 'Values': ['Snapshot from cluster: prep Time: *']}])
snapshotlist = response['Snapshots']

#print snapshotlist
for snap in snapshotlist:
    snplist.append(snap['Description'])

pamba = len(snplist)-1

for i in range(0,pamba):
    print snplist[i]
