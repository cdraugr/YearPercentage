def ft_error(trace: int) -> None:
    if trace < 10:
        print("Mistake")
    if 5 <= trace < 10:
        print("STOP IT!")
    elif trace == 10:
        exit("Bye")
