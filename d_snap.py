#!/usr/local/aws/bin/python
import datetime
from datetime import timedelta
import boto3

client = boto3.client('ec2')
snplist = []
for i in range(3,4):
  daysreq = "18-05-25"        
  response = client.describe_snapshots(Filters=[{'Name': 'description', 'Values': [ 'Snapshot from cluster: sandpit Time: %s*'%daysreq]}])
  snapshotlist = response['Snapshots']
  for snap in snapshotlist:
    print snap
   # snplist.append(snap['Description'])
  #print len(snplist) 
  #del snplist [:] 



#for snap in range(len(snplist)):
  #print (snplist[snap])   
