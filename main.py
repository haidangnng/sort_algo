import click
import inquirer
from utils.sortExe import SORT_ENUM, sort_execution
from utils.plot import plotBar


METHODS = {
    "Bubble Sort": SORT_ENUM.BUBBLE,
    "Bubble Sort (Tuned)": SORT_ENUM.BUBBLE_TUNE,
    "Insertion sort": SORT_ENUM.INSERTION,
    "Merge sort": SORT_ENUM.MERGE,
    "Heap Sort": SORT_ENUM.HEAP,
    "Selection Sort": SORT_ENUM.SELECTION,
    "Shell Sort": SORT_ENUM.SHELL,
    "Quick Sort": SORT_ENUM.QUICK,
}


@click.command()
def main():
    question = [
        inquirer.Text("array_length", message="Input array length"),
        inquirer.Checkbox(
            "methods",
            choices=METHODS.keys(),
            message="Algorithm to use",
            carousel=True,
        ),
    ]

    answer = inquirer.prompt(question)
    input_length = answer["array_length"]
    methods = map(lambda n: METHODS.get(n), answer["methods"])

    result = sort_execution(int(input_length), list(methods))
    plotBar(result["time_table"])


if __name__ == "__main__":
    main()
