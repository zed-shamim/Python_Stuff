#!/bin/bash
snapshots_to_delete=($(aws ec2 describe-snapshots --query 'Snapshots[?StartTime>=`2018-06-01`].SnapshotId' --output text))
echo "List of snapshots to delete: $snapshots_to_delete"
