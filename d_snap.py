#!/usr/local/aws/bin/python
import datetime
from datetime import timedelta
from time import sleep
import boto3
for d in range(12,19):
 ago = datetime.date.today() - timedelta(days=d)
 daysreq = ago.strftime("%Y-%m-%d")
 print daysreq
 sleep(30)
