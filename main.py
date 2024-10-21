import threading
import time


def prime_numbers(n: int, start: int = 2) -> list[int]:
    if n <= 1:
        print("Erreur, chiffre trop petit")
        return []
    if start < 2:
        print("Erreur, début trop petit")
        return []

    result: list[int] = []
    for i in range(start, n):
        for j in range(start, i):
            if (i % j) == 0:
                break
        else:
            result.append(i)
    return result


if __name__ == "__main__":
    goal: int = 100_000

    curr = time.time()
    prime_numbers(goal)
    print(time.time() - curr)

    thread1 = threading.Thread(target=prime_numbers, args=(goal//2, 2))
    thread2 = threading.Thread(target=prime_numbers, args=(goal - goal//2, goal//2))

    curr = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(time.time() - curr)