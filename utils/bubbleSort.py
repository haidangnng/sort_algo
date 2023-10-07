def bubbleSort(input):
    for i in range(0, len(input) - 2):
        for j in range(len(input) - 1, i, -1):
            if input[j - 1] > input[j]:
                tmp = input[j]
                input[j] = input[j - 1]
                input[j - 1] = tmp

    return input
