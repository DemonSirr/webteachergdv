def my_sum(arr: list[float | int]) -> float | int:
    sum = 0
    for i in arr:
        sum += i
    return sum


def my_len(arr: list[float | int]) -> int:
    len = 0
    for i in arr:
        len += 1
    return len
  

def my_avg(arr: list[float | int]) -> float | int:
    if my_len(arr) == 0:
        return 0
    return my_sum(arr) / my_len(arr)


def my_min(arr: list[float | int]) -> float | int:
    if my_len(arr) == 0:
        raise ValueError("Список пуст")
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min


def my_max(arr: list[float | int]) -> float | int:
    if my_len(arr) == 0:
        raise ValueError("Список пуст")
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


def my_max_filter(arr: list[float | int], num: float | int) -> list[float | int]:
    max_f = []
    for i in arr:
        if i > num:
            max_f.append(i)
    return max_f

