from ft_rus_round import ft_rus_round
from ft_leap_year import ft_leap_year


month_dict = {
    0: "December",
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
}


def ft_compare(num: int, year: int) -> int:
    return int((num - 1) * 100 / ft_month(12, year)) -\
           int(num * 100 / ft_month(12, year))


def ft_print_time(day: int, percent: int, year: int) -> None:
    date = ft_month(12, year) * percent / 100
    answer = ft_time(date)
    if answer != "00:00":
        print(f"{day} {percent}.0000% {ft_time(date)}")


def ft_print_month(month: int) -> None:
    print("=" * 12)
    print(" " * (ft_rus_round((13 -
                               len(month_dict[month % 12])) / 2) - 1),
          month_dict[month % 12])
    print("=" * 12)


def ft_print_years(month: int, year: int) -> None:
    print("=" * 24)
    print(" " * (ft_rus_round((25 - len(str(year))) / 2) - 1), year)
    print("=" * 24)
    ft_year(ft_month(12, year), month + 1, year)


def ft_month(number: int, year: int) -> int:
    if not number:
        return 0
    if number == 1:
        return 31
    if number == 2:
        return ft_month(number - 1, year) + ft_leap_year(year)
    if number in [3, 5, 7, 8, 10, 12]:
        return ft_month(number - 1, year) + 31
    return ft_month(number - 1, year) + 30


def ft_time(time: float) -> str:
    time = (time - int(time)) * 24
    string = ""
    if time < 10:
        string = "0"
    string += str(int(time)) + ":"
    time = (time - int(time)) * 60
    if round(time) < 10:
        string += "0"
    string += str(round(time))
    return string


def ft_year(length: int, month: int, year: int) -> None:
    if month == 0:
        start = ft_month(0, year)
        end = ft_month(12, year)
        value = ft_month(month, year)
    else:
        start = ft_month(month - 1, year)
        end = ft_month(month, year)
        ft_print_month(month)
        value = ft_month(month - 1, year)
    for i in range(start, end):
        if i >= ft_month(month, year):
            value = ft_month(month, year)
            if ft_compare(i, year):
                if not i - value:
                    ft_print_time(i - ft_month(month - 1, year),
                                  int(i * 100 / length), year)
            month += 1
            ft_print_month(month)

        if int((i - 1) * 100 / length) - int(i * 100 / length):
            if i - value:
                ft_print_time(i - value, int(i * 100 / length), year)

        print(f"{i + 1 - value} {(i * 100 / length):.4f}%")
