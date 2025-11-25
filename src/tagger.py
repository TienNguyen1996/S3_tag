import boto3
import csv

def apply_tags_from_csv(csv_file):
    s3 = boto3.client("s3")
    with open(csv_file, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 3:
                print(f"⚠️ Skipping invalid row: {row}")
                continue

            object_path, tag_key, tag_value = row
            bucket, key = object_path.replace("s3://", "").split("/", 1)

            print(f"Tagging {bucket}/{key} with {tag_key}={tag_value}")
            s3.put_object_tagging(
                Bucket=bucket,
                Key=key,
                Tagging={"TagSet": [{"Key": tag_key, "Value": tag_value}]},
            )
