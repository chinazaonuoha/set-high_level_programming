#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys


def print_metrics(total_file_size, status_codes):
    """Prints the current accumulated metrics."""
    print(f"File size: {total_file_size}", flush=True)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}", flush=True)


def process_line(line):
    """Parses a single log line and extracts
    file size and status code."""
    parts = line.split()
    if len(parts) < 2:
        return 0, None

    try:
        file_size = int(parts[-1])
    except (ValueError, IndexError):
        file_size = 0

    try:
        status_code = int(parts[-2])
    except (ValueError, IndexError):
        status_code = None

    return file_size, status_code


def main():
    """Main execution loop for streaming log data."""
    total_file_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            file_size, status_code = process_line(line)
            total_file_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            if line_count % 10 == 0:
                print_metrics(total_file_size, status_codes)

    except KeyboardInterrupt:
        pass
    finally:
        print_metrics(total_file_size, status_codes)


if __name__ == "__main__":
    main()
