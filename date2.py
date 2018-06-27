#!/usr/local/aws/bin/python
import datetime
from datetime import timedelta
import boto3
import json
from time import sleep

client = boto3.client('ec2')

snplist = []
for d in range(12,15):
 ago = datetime.date.today() - timedelta(days=d) 
 daysreq = ago.strftime("%Y-%m-%d")
 response = client.describe_snapshots(Filters=[{'Name': 'description', 'Values': [ 'Snapshot from cluster: *nonprod*: %s*'%daysreq]}])
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
   del key['Encrypted']
   del key['Tags']

 for z in snapshotlist:
   snplist.append(z['Description'])

 newlist = list(set(snplist))
 newlist.sort()
 del newlist[-1]

 for tyre in range(len(newlist)):    
    desc = (newlist[tyre])
    res = client.describe_snapshots(Filters=[{'Name': 'description', 'Values': [ '{}'.format(desc)]}])
    sshotlist = res['Snapshots'] 
    
    for y in sshotlist:
      print "deleteing"+' '+y['Description']+' '+y['SnapshotId']
      client.delete_snapshot(SnapshotId=y['SnapshotId'])
 del snplist[:] 
 del newlist[:]
 #sleep(60)
