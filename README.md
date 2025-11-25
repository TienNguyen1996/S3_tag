# S3 Tagging Tool

A simple Python command‑line utility to apply or remove tags from Amazon S3 objects in bulk using CSV files.

---

## Features
- **Apply tags:** Bulk tag S3 objects from a CSV file.
- **Clean tags:** Remove all tags from S3 objects listed in a CSV file.
- **Credential control:** Use AWS profiles, environment variables, or custom credential file paths.
- **Modular design:** Separation of concerns via `tagger.py` and `cleaner.py`.

---

## Requirements
- **Python:** 3.8+
- **Dependencies:** boto3

Install:
    pip install boto3

---

## Setup AWS credentials

You can provide AWS credentials in one of three ways:

### 1. Environment variables
Linux/macOS (bash/zsh):
    export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY"
    export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY"
    export AWS_DEFAULT_REGION="us-east-1"

Windows PowerShell:
    $env:AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY"
    $env:AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY"
    $env:AWS_DEFAULT_REGION="us-east-1"

### 2. AWS profiles (credentials and config files)
Create `~/.aws/credentials`:
    [default]
    aws_access_key_id = YOUR_ACCESS_KEY
    aws_secret_access_key = YOUR_SECRET_KEY

    [my-profile]
    aws_access_key_id = OTHER_ACCESS_KEY
    aws_secret_access_key = OTHER_SECRET_KEY

Create `~/.aws/config`:
    [default]
    region = us-east-1
    output = json

    [profile my-profile]
    region = ap-southeast-1
    output = json

### 3. Custom credentials file path (optional)
    export AWS_SHARED_CREDENTIALS_FILE="/custom/path/credentials"
    export AWS_CONFIG_FILE="/custom/path/config"

---

## CSV format

### Tagging (tag)
Each row contains an S3 object path and tags:
    s3://my-bucket/data/file1.csv,Key1=Value1;Key2=Value2
    s3://another-bucket/images/photo.png,env=prod;owner=team-a

### Cleaning (clean)
Each row contains only the S3 object path:
    s3://my-bucket/data/file1.csv
    s3://my-bucket/data/file2.csv

---

## Usage
Apply tags:
    python script.py tag objects_with_tags.csv

Remove tags:
    python script.py clean objects_to_clean.csv

Use a specific AWS profile (if supported):
    python script.py tag objects_with_tags.csv --profile my-profile
    python script.py clean objects_to_clean.csv --profile my-profile

---

## Permissions
- **Required IAM actions:** `s3:PutObjectTagging`, `s3:DeleteObjectTagging`
- **Scope:** Grant on the relevant buckets/keys your CSV references.

---

## Project structure
    .
    ├── script.py        # CLI entry point (argparse: tag/clean subcommands)
    ├── tagger.py        # apply_tags_from_csv(csv_path)
    ├── cleaner.py       # clean_tags_from_csv(csv_path)
    └── README.md
