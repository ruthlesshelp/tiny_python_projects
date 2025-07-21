#!/usr/bin/env python3
"""
Author: RuthlessHelp
Date: 2025-07-21
File: picnic.py
Purpose: A script to manage picnic items
"""

import argparse


# --------------------------------------------------
def get_args():
    """
    Parse command-line arguments for picnic items
    """

    parser = argparse.ArgumentParser(
        description='Picnic items',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='items',
                        nargs='+',
                        type=str,
                        help='A list of items to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='A boolean flag',
                        default=False,
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """
    Main function to handle picnic items
    """

    args = get_args()
    if args.sorted:
        args.items.sort()

    if len(args.items) == 0:
        print('You are not bringing anything.')
    elif len(args.items) == 1:
        print(f'You are bringing {args.items[0]}.')
    elif len(args.items) == 2:
        print(f'You are bringing {args.items[0]} and {args.items[1]}.')
    else:
        last_item = args.items.pop()
        print(f'You are bringing {", ".join(args.items)}, and {last_item}.')


if __name__ == '__main__':
    main()
