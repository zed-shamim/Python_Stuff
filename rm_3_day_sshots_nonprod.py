#!/usr/local/aws/bin/python
import datetime
from datetime import timedelta
import boto3

snplist = []
td = 5
try:
 ago = datetime.date.today() - timedelta(days=td) 
 daysreq = ago.strftime("%Y-%m-%d")
 client = boto3.client('ec2')
 response = client.describe_snapshots(Filters=[{'Name': 'description', 'Values': [ 'Snapshot from cluster: nonprod*: %s*'%daysreq]}])
 snapshotlist = response['Snapshots']
 for snap in snapshotlist:
    snplist.append(snap['Description'])
 srl = list(set(snplist))
 srl.sort()
 del srl[-1]
 for rs in range(len(srl)):
    res = client.describe_snapshots(Filters=[{'Name': 'description', 'Values': [ '{}'.format((srl[rs]))]}])
    sslist = res['Snapshots']
    for des in sslist:
      print "deleteing"+' '+des['Description']+' '+des['SnapshotId']
      client.delete_snapshot(SnapshotId=des['SnapshotId']) 
except Exception as e: 
 print (e) 
 
