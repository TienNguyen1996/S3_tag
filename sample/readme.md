## 📂 S3 Object Tagging Definition File Format

This document defines the expected structure and content for the CSV file used to specify S3 object tags.

---

### 📝 Original Format (The Input)

The input file must be a standard comma-separated values (CSV) file where each row defines a single tag applied to a specific S3 object.

#### Structure

Each row is expected to contain three comma-separated fields, in this exact order:

1.  **S3 Object Path**: The full `s3://` path to the object (e.g., `s3://my-bucket/data/file.log`).
2.  **Tag Key**: The key for the tag (e.g., `environment`).
3.  **Tag Value**: The value associated with the key (e.g., `production`).

#### Example

```csv
s3://tag-sampling/sample1.txt,env,test
s3://tag-sampling/sample2.txt,env,dev
s3://tag-sampling/sample1.txt,owner,team-a