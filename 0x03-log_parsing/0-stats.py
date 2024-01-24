#!/usr/bin/python3

import sys


def print_statistics(status_code_dict, total_size):
    """
    Function to print the statistics
        Args:
            status_code_dict: Dictionary of status codes
            total_size: Total size of the files
        Returns:
            None
    """

    print("File size: {}".format(total_size))
    for key, val in sorted(status_code_dict.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_size = 0
status_code = 0
line_counter = 0
status_code_dict = {"200": 0,
                    "301": 0,
                    "400": 0,
                    "401": 0,
                    "403": 0,
                    "404": 0,
                    "405": 0,
                    "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Splitting the line into parts
        parsed_line = parsed_line[::-1]  # Reversing the parts

        if len(parsed_line) > 2:
            line_counter += 1

            if line_counter <= 10:
                total_size += int(parsed_line[0])
                status_code = parsed_line[1]  # Extracting the status code

                if (status_code in status_code_dict.keys()):
                    status_code_dict[status_code] += 1

            if (line_counter == 10):
                print_statistics(status_code_dict, total_size)
                line_counter = 0

finally:
    print_statistics(status_code_dict, total_size)
