def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def euler(n: int) -> float:
    result = 1.0
    factorial = 1

    for i in range(1, n):
        factorial *= i
        result += 1 / factorial

    return result


print(euler(1_000_000_000))
