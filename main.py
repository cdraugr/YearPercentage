#!/usr/bin/env python3

from src.parse_arguments import parse
from src.print_percentage import to_print


def main():
    to_print(parse())


if __name__ == '__main__':
    main()
