import argparse
import calendar
import typing

from datetime import datetime, timedelta


def _print_month_name(month: int):
    month_name = calendar.month_name[month]
    print('=' * (len(month_name) + 6))
    print(f'   {month_name}')
    print('=' * (len(month_name) + 6))


def _print_percentage(value: typing.Union[int, float], format_code: str) -> str:
    return f'{float(value):{format_code}}%%'


def _print_month(year: int, month: int, format_code: str):
    _print_month_name(month)

    year_begin = datetime(year=year, month=1, day=1).timestamp()
    delta = datetime(year=year + 1, month=1, day=1).timestamp() - year_begin

    current_day = datetime(year=year, month=month, day=1)
    for _ in range(calendar.monthrange(year, month)[1]):
        percentage = (current_day.timestamp() - year_begin) / delta * 100
        print(current_day.strftime(f'%d {_print_percentage(percentage, format_code)}'))

        next_day = current_day + timedelta(days=1)
        next_percentage = (next_day.timestamp() - year_begin) / delta * 100
        if int(percentage) - int(next_percentage) and not next_percentage.is_integer():
            round_date = datetime.fromtimestamp(year_begin + delta * int(next_percentage) / 100)
            print(round_date.strftime(f'%d {_print_percentage(int(next_percentage), format_code)} %H:%M'))

        current_day = next_day


def _print_year(year: int, format_code: str):
    for month in range(1, 13):
        _print_month(year, month, format_code)
        print(end='\n' if month != 12 else '')


def to_print(arguments: argparse.Namespace):
    format_code = f'0{arguments.accuracy + 3}.{arguments.accuracy}f'

    if arguments.month:
        _print_month(arguments.year, arguments.month, format_code)
    else:
        _print_year(arguments.year, format_code)
