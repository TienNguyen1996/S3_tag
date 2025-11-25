# main.py
import sys
from cli import build_parser
from auth import validate_credentials
from tagger import apply_tags_from_csv
from cleaner import clean_tags_from_csv
import notify

def main():
    parser = build_parser()
    args = parser.parse_args()

    # Step 1: validate credentials
    if not validate_credentials():
        notify.err("Credential validation failed.")
        sys.exit(1)
    notify.ok("Credential validation passed.")

    # Step 2: run the chosen action
    if args.command == "tag":
        notify.ok(f"Starting tagging from {args.csv_file}...")
        apply_tags_from_csv(args.csv_file)
        notify.ok("Tagging completed.")
    elif args.command == "clean":
        notify.ok(f"Starting cleaning from {args.csv_file}...")
        clean_tags_from_csv(args.csv_file)
        notify.ok("Cleaning completed.")
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
