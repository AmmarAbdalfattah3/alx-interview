#!/usr/bin/python3
"""
This module reads stdin line by line and computes metrics
"""


import sys
from collections import defaultdict


def print_metrics(file_size_sum, status_counts):
    """Print the total file size and counts of status codes."""
    print(f"File size: {file_size_sum}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")


def main():
    """Process log lines from stdin and compute statistics."""
    file_size_sum = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) != 7:
                continue

            ip_address, dash, date_bracket, method, status_code, file_size = (
                parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]
            )

            if (dash == '-' and date_bracket.startswith('[') and
                    method.startswith('"GET') and status_code.isdigit() and
                    file_size.isdigit()):
                try:
                    status_code = int(status_code)
                    file_size = int(file_size)
                except ValueError:
                    continue

                if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                    status_counts[status_code] += 1
                    file_size_sum += file_size
                    line_count += 1

                if line_count % 10 == 0:
                    print_metrics(file_size_sum, status_counts)

    except KeyboardInterrupt:
        print_metrics(file_size_sum, status_counts)


if __name__ == "__main__":
    main()
