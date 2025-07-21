#!/usr/bin/env python3
"""
Author: RuthlessHelp
Date: 2025-07-21
File: crowsnest.py
Purpose: A script to greet the captain with a word from the crow's nest.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='A word argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
