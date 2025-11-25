# cli.py
import argparse

def build_parser():
    parser = argparse.ArgumentParser(
        description="Tag or clean S3 object tags from a CSV file"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Tag command
    tag_parser = subparsers.add_parser("tag", help="Apply tags to S3 objects")
    tag_parser.add_argument("csv_file", help="Path to CSV file with object paths and tags")

    # Clean command
    clean_parser = subparsers.add_parser("clean", help="Remove tags from S3 objects")
    clean_parser.add_argument("csv_file", help="Path to CSV file with object paths")

    return parser
