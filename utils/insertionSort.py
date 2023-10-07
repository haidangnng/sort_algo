def insertionSort(input):
    for i in range(1, len(input) - 1):
        tmp = input[i]
        j = i - 1

        while j > -1 and input[j] > tmp:
            input[j + 1] = input[j]
            j = j - 1

        input[j + 1] = tmp

    return input
