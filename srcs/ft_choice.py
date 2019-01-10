from ft_error import ft_error
from ft_try import ft_try
from ft_moment import ft_month


def ft_choice() -> int:
    print("Choice on of the buttons:\n"
          "One year is 1.\nSome years is 2.\n"
          "One month is 3.\nOne day is 4.\n"
          "Exit is 0.\n")
    trace = 0
    while True:
        choice = ft_try("".join(filter(str.isdigit,
                                       input(" Your choice = "))))
        if choice in [1, 2, 3, 4]:
            break
        elif choice == 0:
            exit("Bye")
        trace += 1
        ft_error(trace)
    return choice


def ft_one_year():
    trace = 0
    while True:
        year = input("Year = ")
        year = ft_try("".join(filter(str.isdigit, year)))
        if 0 <= year:
            break
        trace += 1
        ft_error(trace)
    return year, year, 0


def ft_some_years():
    trace = 0
    while True:
        start_year = input("Start year = ")
        start_year = ft_try("".join(filter(str.isdigit, start_year)))
        if 0 <= start_year:
            break
        trace += 1
        ft_error(trace)
    trace = 0
    while True:
        end_year = input("End year = ")
        end_year = ft_try("".join(filter(str.isdigit, end_year)))
        if end_year > start_year:
            break
        trace += 1
        ft_error(trace)
    return start_year, end_year, 0


def ft_one_month():
    trace = 0
    while True:
        year = input("Year = ")
        year = ft_try("".join(filter(str.isdigit, year)))
        if 0 <= year:
            break
        trace += 1
        ft_error(trace)
    trace = 0
    while True:
        month = input("Month = ")
        month = ft_try("".join(filter(str.isdigit, month)))
        if 1 <= month <= 12:
            break
        trace += 1
        ft_error(trace)
    return year, year, month


def ft_one_day():
    trace = 0
    while True:
        year = input("Year = ")
        year = ft_try("".join(filter(str.isdigit, year)))
        if 0 <= year:
            break
        trace += 1
        ft_error(trace)
    trace = 0
    while True:
        month = input("Month = ")
        month = ft_try("".join(filter(str.isdigit, month)))
        if 1 <= month <= 12:
            break
        trace += 1
        ft_error(trace)
    month_limit =\
        ft_month(month, year) - ft_month(month - 1, year)
    trace = 0
    while True:
        day = input("Day = ")
        day = ft_try("".join(filter(str.isdigit, day)))
        if 1 <= day <= month_limit:
            break
        trace += 1
        ft_error(trace)
    print(f"At the end of {day}.{month}.{year}\n"
          f"will be", end=" ")
    print("%.4f" % ((ft_month(month - 1, year) + day) * 100
                    / ft_month(12, year)), "%", sep="")
    exit()


def ft_choice_maker(choice: int):
    if choice == 1:
        return ft_one_year()
    if choice == 2:
        return ft_some_years()
    if choice == 3:
        return ft_one_month()
    return ft_one_day()


def ft_array_with_choice():
    return ft_choice_maker(ft_choice())
