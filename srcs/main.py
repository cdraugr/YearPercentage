from ft_choice import ft_array_with_choice
from ft_moment import ft_print_years


def main() -> None:
    array = ft_array_with_choice()
    current_year = array[0] - 1
    count = array[1] - array[0] + 1
    current_month = array[2] - 1

    for _ in range(count):
        current_year += 1
        ft_print_years(current_month, current_year)


if __name__ == "__main__":
    main()
