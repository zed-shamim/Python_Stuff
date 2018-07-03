#!/usr/local/aws/bin/python
import datetime
from datetime import timedelta,date
from time import sleep
import sys
import boto3
def days_old(date):
    date_obj = date.replace(tzinfo=None)
    diff = datetime.datetime.now() - date_obj
    return diff.days

print days_old()
