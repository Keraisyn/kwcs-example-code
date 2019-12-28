def my_max(list):
    """Finds the maximum number from a list."""
    max = list[0]

    for num in list:
        if max < num:
            max = num

    return max


def my_min(list):
    """Finds the minimum number from a list."""
    min = list[0]

    for num in list:
        if min > num:
            min = num

    return min


def switcheroo(list):
    max = my_max(list)
    min = my_min(list)

    max_index = list.index(max)
    min_index = list.index(min)

    list[max_index] = min
    list[min_index] = max

    return list

print(switcheroo([12, 21, 5, 11, 79, 8]))
