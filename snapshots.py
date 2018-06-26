#!/usr/local/aws/bin/python
import boto3
import datetime
from datetime import timedelta

snplist = []
owner='994432210064'
client = boto3.client('ec2')

#for i in range(4,5):
del snplist[:]
daysago = datetime.date.today() - timedelta(days=2)

string_in_string = "Snapshot from cluster: prep Time: {}*".format(daysago)          
print string_in_string
response = client.describe_snapshots(Filters=[{'Name': 'description', 'Values': [ string_in_string ]}])



snapshotlist = response['Snapshots']
print len(snapshotlist)


       
            
             
























#response = client.describe_snapshots(Filters=[{'Name': 'description', 'Values': ['Snapshot from cluster: sandpit Time: 18*']}])
#snapshotlist = response['Snapshots']
#print string_in_string
#for snap in snapshotlist:
#    snplist.append(snap['OwnerId'])

#pamba = len(snplist)-1

#for i in range(0,pamba):
#    print snplist[i]
