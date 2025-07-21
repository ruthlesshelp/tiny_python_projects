#! /usr/bin/env python3
"""
Author: RuthlessHelp
Date: 2025-07-21
File: hello.py
Purpose: A simple script to print "Hello, World!"
"""

import argparse


def def_args():
    """Define command line arguments."""
    parser = argparse.ArgumentParser(description="Say hello.")
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    args = parser.parse_args()
    return args


def main():
    """Main function to execute the script."""
    args = def_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
