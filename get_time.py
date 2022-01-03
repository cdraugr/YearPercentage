#!/usr/bin/env python3

import argparse

from datetime import datetime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int)
    parser.add_argument('percentage', type=float)
    arguments = parser.parse_args()

    year_begin = datetime(year=arguments.year, month=1, day=1).timestamp()
    delta = datetime(year=arguments.year + 1, month=1, day=1).timestamp() - year_begin
    result = datetime.fromtimestamp(year_begin + delta * arguments.percentage / 100)
    print(result.strftime(f'%d-%m %H:%M:%S'))


if __name__ == '__main__':
    main()
