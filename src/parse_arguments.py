import argparse
import calendar
import typing

from src import const


class DayAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        namespace.day = values
        if not namespace.month:
            if namespace.day:
                parser.error('Unable to set a day without month')
            else:
                return

        day_limit = calendar.monthrange(namespace.year, namespace.month)[1]
        if namespace.day > day_limit:
            parser.error(f'There are only {day_limit} days in {calendar.month_name[namespace.month]}\'{namespace.year}')


def _int_range(left: float, right: float) -> typing.Callable[[str], int]:
    def _int_range_checker(arg: str) -> int:
        try:
            value = int(arg)
        except ValueError:
            raise argparse.ArgumentTypeError('must be an integer number')

        if left > value or value > right:
            raise argparse.ArgumentTypeError(f'integer must be in range [{left}, {right}]')

        return value

    return _int_range_checker


def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument('year', type=_int_range(1, float('inf')), help='year of the date')
    parser.add_argument('month', type=_int_range(1, 12), nargs='?', help='month of the date', default=0)
    parser.add_argument('day', type=_int_range(1, 31), nargs='?', help='day of the date', default=0, action=DayAction)
    parser.add_argument('-a', '--accuracy', type=_int_range(1, 12), help='output accuracy', default=const.DEFAULT_ACCURACY)

    return parser.parse_args()
