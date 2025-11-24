import boto3
import csv

def apply_tags_from_csv(csv_file):
    s3 = boto3.client("s3")
    with open(csv_file, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 2:
                print(f"⚠️ Skipping invalid row: {row}")
                continue
            object_path, tag = row
            bucket, key = object_path.replace("s3://", "").split("/", 1)
            print(f"Tagging {bucket}/{key} with {tag}")
            s3.put_object_tagging(
                Bucket=bucket,
                Key=key,
                Tagging={"TagSet": [{"Key": "custom-tag", "Value": tag}]},
            )
