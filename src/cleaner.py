import boto3
import csv

def clean_tags_from_csv(csv_file):
    s3 = boto3.client("s3")
    with open(csv_file, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                print(f"⚠️ Skipping invalid row: {row}")
                continue
            object_path = row[0]
            bucket, key = object_path.replace("s3://", "").split("/", 1)
            print(f"Removing tags from {bucket}/{key}")
            s3.delete_object_tagging(Bucket=bucket, Key=key)
