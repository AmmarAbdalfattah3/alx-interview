#!/usr/bin/python3
"""
This module reads stdin line by line and computes metrics
"""


import sys
import re
from collections import defaultdict


# Regular expression pattern to match log lines
LOG_PATTERN = re.compile(
    r' ^ (\d{1, 3}\.\d{1, 3}\.\d{1, 3}\.\d{1, 3})
    - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3})(\d+)$'
)

# Status codes to track
status_codes = {200, 301, 400, 401, 403, 404, 405, 500}

# Variables to hold metrics
file_size_total = 0
status_counts = defaultdict(int)
line_count = 0


def print_metrics():
    # Print the accumulated metrics
    print(f'File size: {file_size_total}')
    for status_code in sorted(status_codes):
        if status_counts[status_code] > 0:
            print(f'{status_code}: {status_counts[status_code]}')


try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            # Extract file size and status code
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # Update metrics
            file_size_total += file_size
            if status_code in status_codes:
                status_counts[status_code] += 1

            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics()

except KeyboardInterrupt:
    # Print metrics on keyboard interruption
    print_metrics()
