#!/usr/local/aws/bin/python
import datetime
from datetime import timedelta
import boto3
import json

client = boto3.client('ec2')
snplist = []
daysreq = "2018-05-30"        
response = client.describe_snapshots(Filters=[{'Name': 'description', 'Values': [ 'Snapshot from cluster: prep Time: %s*'%daysreq]}])
snaphostlist = response['Snapshots'] 
for snap in snaphostlist:
  snplist.append (snap ['Description'])
newlist = list(set(snplist))
newlist.sort()
del newlist[-1]
for i in range(len(newlist)):
  print (newlist[i])  
