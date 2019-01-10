def ft_rus_round(x: float) -> int:
    if x - int(x) >= 0.5:
        x = int(x) + 1
    x = int(x)
    return x
