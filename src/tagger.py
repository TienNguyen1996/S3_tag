import boto3
import csv

def apply_tags_from_csv(csv_file):
    s3 = boto3.client('s3')
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            object_path, tag = row
            bucket, key = object_path.replace("s3://", "").split("/", 1)
            s3.put_object_tagging(
                Bucket=bucket,
                Key=key,
                Tagging={'TagSet': [{'Key': 'custom-tag', 'Value': tag}]}
            )
