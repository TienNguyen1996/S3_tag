import argparse
import sys
from tagger import apply_tags_from_csv
from cleaner import clean_tags_from_csv

def main():
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

    args = parser.parse_args()

    if args.command == "tag":
        print(f"Applying tags from {args.csv_file}...")
        apply_tags_from_csv(args.csv_file)
        print("✅ Tagging completed.")

    elif args.command == "clean":
        print(f"Cleaning tags from {args.csv_file}...")
        clean_tags_from_csv(args.csv_file)
        print("✅ Cleaning completed.")

    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
