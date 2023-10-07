def bubbleSortTuned(input):
    i = 0
    while i < len(input) - 1:
        k = len(input) - 1
        for j in range(len(input) - 1, i, -1):
            if input[j - 1] > input[j]:
                tmp = input[j]
                input[j] = input[j - 1]
                input[j - 1] = tmp
                k = j
        i = k

    return input
