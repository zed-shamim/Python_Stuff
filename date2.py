#!/usr/local/aws/bin/python
import datetime
from datetime import timedelta
import boto3
import json

client = boto3.client('ec2')
snplist = []
for d in range(15,17):
 ago = datetime.date.today() - timedelta(days=d) 
 daysreq = ago.strftime("%Y-%m-%d")    
 response = client.describe_snapshots(Filters=[{'Name': 'description', 'Values': [ 'Snapshot from cluster: prod Time: %s*'%daysreq]}])
 print response
 snapshotlist = response['Snapshots'] 
 for key in snapshotlist: 
   del key['StartTime']
   del key['State']  
   del key['Progress']
   del key['SnapshotId']
   del key['VolumeSize']
   del key['VolumeId']
   del key['OwnerId']
   del key['KmsKeyId']
   del key ['Encrypted']
   del key ['Tags']

 for z in snapshotlist:
   snplist.append(z['Description'])

 newlist = list(set(snplist))
 newlist.sort()
 del newlist[-1]
 for tyre in range(len(newlist)):
    print (newlist[tyre]) 
 del newlist[:]
 del snplist[:] 
