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
 snapshotlist = response['Snapshots'] 

 for snap in snapshotlist:
  snplist.append (snap ['Description'])
 
 for i in range(len(snplist)):
  res = client.describe_snapshots(Filters=[{'Name': 'description', 'Values': [snplist[i]]}])
  sslist = res['Snapshots']
 for s in sslist:
   print s['SnapshotId']
  


 
 del snplist[:]
