import numpy as np
import matplotlib.pyplot as plt


def getTableData(values):
    row = []
    for i in range(0, len(values)):
        col = []
        for j in range(0, len(values)):
            col.append(float(values[i] / values[j]))
        row.append(col)
    return row


def plotBar(data):
    algos = list(data.keys())
    values = list(data.values())
    # Adjust layout to make room for the table:

    # creating the bar plot
    plt.bar(algos, values, color="maroon", width=0.2)
    plt.ylabel("Sort speed in milliseconds")
    plt.title("Comparing sort algorithms")
    plt.show()

    # Add a table at the bottom of the axes

    columns = rows = algos
    tableData = getTableData(values)
    n_rows = len(tableData)

    cell_text = []
    for row in range(n_rows):
        cell_text.append(["%.2f" % x for x in tableData[row]])

    plt.figure()
    # plt.table(cellText=cell_text, rowLabels=rows, colLabels=columns)
    plt.box(on=None)
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    the_table = plt.table(
        cellText=cell_text, rowLabels=rows, colLabels=columns, loc="center"
    )
    the_table.scale(1, 1.5)
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    plt.show()
