import argparse
import calendar
import typing

from datetime import datetime, timedelta


def _print_month_name(month: int):
    month_name = calendar.month_name[month]
    extra_spaces_count = 3
    spaces_count = len(month_name) + extra_spaces_count * 2
    print('=' * spaces_count)
    print(f'{" " * extra_spaces_count}{month_name}')
    print('=' * spaces_count)


def _get_format_percentage(value: typing.Union[int, float], format_code: str) -> str:
    return f'{float(value):{format_code}}%%'


def _print_day(current_day: datetime, format_code: str, year_data: typing.Optional[typing.Tuple[float, float]] = None) -> datetime:
    if year_data is not None:
        year_begin, delta = year_data
    else:
        year_begin = datetime(year=current_day.year, month=1, day=1).timestamp()
        delta = datetime(year=current_day.year + 1, month=1, day=1).timestamp() - year_begin

    percentage = (current_day.timestamp() - year_begin) / delta * 100
    print(current_day.strftime(f'%d {_get_format_percentage(percentage, format_code)}'))

    next_day = current_day + timedelta(days=1)
    next_percentage = (next_day.timestamp() - year_begin) / delta * 100
    if int(percentage) - int(next_percentage) and not next_percentage.is_integer():
        round_date = datetime.fromtimestamp(year_begin + delta * int(next_percentage) / 100)
        print(round_date.strftime(f'%d {_get_format_percentage(int(next_percentage), format_code)} %H:%M'))

    return next_day


def _print_month(year: int, month: int, format_code: str):
    _print_month_name(month)

    year_begin = datetime(year=year, month=1, day=1).timestamp()
    delta = datetime(year=year + 1, month=1, day=1).timestamp() - year_begin

    current_day = datetime(year=year, month=month, day=1)
    for _ in range(calendar.monthrange(year, month)[1]):
        current_day = _print_day(current_day, format_code, (year_begin, delta))


def _print_year(year: int, format_code: str):
    for month in range(1, 13):
        _print_month(year, month, format_code)
        print(end='\n' if month != 12 else '')


def to_print(arguments: argparse.Namespace):
    format_code = f'0{arguments.accuracy + 3}.{arguments.accuracy}f'

    if arguments.day:
        _print_day(datetime(year=arguments.year, month=arguments.month, day=arguments.day), format_code)
    elif arguments.month:
        _print_month(arguments.year, arguments.month, format_code)
    else:
        _print_year(arguments.year, format_code)
