import argparse
import calendar
import typing

from datetime import datetime, timedelta


class Percentage:
    def __init__(self, year: int, month: int, day: int, format_code: str):
        self.given_month = month
        self.given_day = day

        self.current_day = datetime(year=year, month=month or 1, day=day or 1)
        self.format_code = format_code

        self.year_begin = datetime(year=year, month=1, day=1).timestamp()
        self.delta = datetime(year=year + 1, month=1, day=1).timestamp() - self.year_begin

    def _get_format_percentage(self, value: typing.Union[int, float]) -> str:
        return f'{float(value):{self.format_code}}%%'

    def _get_percentage(self, timestamp: typing.Optional[float] = None) -> float:
        if timestamp is None:
            timestamp = self.current_day.timestamp()
        return (timestamp - self.year_begin) / self.delta * 100

    def _print_day(self) -> datetime:
        percentage = self._get_percentage()
        print(self.current_day.strftime(f'%d {self._get_format_percentage(percentage)}'))

        next_day = self.current_day + timedelta(days=1)
        next_percentage = self._get_percentage(next_day.timestamp())
        if int(percentage) - int(next_percentage) and not next_percentage.is_integer():
            round_date = datetime.fromtimestamp(self.year_begin + self.delta * int(next_percentage) / 100)
            print(round_date.strftime(f'%d {self._get_format_percentage(int(next_percentage))} %H:%M'))

        return next_day

    def _print_month_name(self):
        month_name = calendar.month_name[self.current_day.month]
        extra_spaces_count = 3
        spaces_count = len(month_name) + extra_spaces_count * 2
        print('=' * spaces_count)
        print(f'{" " * extra_spaces_count}{month_name}')
        print('=' * spaces_count)

    def _print_month(self):
        self._print_month_name()

        for _ in range(calendar.monthrange(self.current_day.year, self.current_day.month)[1]):
            self.current_day = self._print_day()

    def _print_year(self):
        for month in range(1, 13):
            self._print_month()
            print(end='\n' if month != 12 else '')

    def print(self):
        if self.given_day:
            self._print_day()
        elif self.given_month:
            self._print_month()
        else:
            self._print_year()


def to_print(arguments: argparse.Namespace):
    format_code = f'0{arguments.accuracy + 3}.{arguments.accuracy}f'
    Percentage(arguments.year, arguments.month, arguments.day, format_code).print()
