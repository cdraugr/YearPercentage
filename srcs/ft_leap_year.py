def ft_leap_year(number: int) -> int:
    if (number % 4 == 0 and number % 100 != 0) or\
            (number % 400 == 0):
        return 29
    return 28
