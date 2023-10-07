from typing import List
from utils.bubbleSortTuned import bubbleSortTuned
from utils.bubbleSort import bubbleSort
from utils.insertionSort import insertionSort
from utils.mergeSort import mergeSort
from utils.heapSort import heapSort
from utils.quickSort import quickSort
from utils.selectionSort import selectionSort
from utils.shellSort import shellSort

# from utils.bucketSort import bucketSort

import time
from enum import Enum
from numpy.random import randint, seed


class SORT_ENUM(str, Enum):
    BUBBLE = "bubble"
    BUBBLE_TUNE = "bubble_tuned"
    INSERTION = "insertion"
    MERGE = "merge"
    HEAP = "heap"
    SELECTION = "selection"
    SHELL = "shell"
    QUICK = "quick"
    # BUCKET = "bucket"


def get_sort_func(name: str, input):
    start = time.time()
    target = input.copy()
    sorted_list = []
    match name:
        case SORT_ENUM.BUBBLE:
            sorted_list = bubbleSort(target)
        case SORT_ENUM.BUBBLE_TUNE:
            sorted_list = bubbleSortTuned(target)
        case SORT_ENUM.INSERTION:
            sorted_list = insertionSort(target)
        case SORT_ENUM.MERGE:
            sorted_list = mergeSort(target)
        case SORT_ENUM.HEAP:
            sorted_list = heapSort(target)
        case SORT_ENUM.SELECTION:
            sorted_list = selectionSort(target)
        case SORT_ENUM.SHELL:
            sorted_list = shellSort(target)
        # case SORT_ENUM.BUCKET:
        #     sorted_list = bucketSort(target)
        case SORT_ENUM.QUICK:
            sorted_list = quickSort(target, 0, len(target) - 1)

    end = time.time()
    ellapsed = end - start
    res = {"ellapsed": ellapsed, "sorted_list": sorted_list}

    return res


def sort_execution(length: int, algorithms: List[SORT_ENUM]):
    seed(1)
    random_input = randint(0, length, length).tolist()
    sort_response = {}
    response = {}

    for sort_algo in algorithms:
        sort_response[sort_algo.value] = get_sort_func(sort_algo, random_input)

    for i in sort_response:
        response[i] = sort_response[i]["ellapsed"]

    return {"input_size": length, "time_table": response}
