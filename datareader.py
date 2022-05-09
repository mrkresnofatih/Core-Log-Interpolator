import numpy as np


def read_data(file_name, column_names):
    row_count = 0
    column_indices = []

    with open(file_name, "r") as rdd:
        line = rdd.readline()
        headers = np.array(line.split(), dtype=str)

        for index, value in enumerate(headers):
            if value in column_names:
                column_indices.append(index)

        while line != "":
            row_count = row_count + 1
            line = rdd.readline()

    with open(file_name, "r") as rd:
        rd.readline()

        row_count = row_count - 1
        container = np.zeros((row_count, len(column_indices)), dtype=float)

        for i in range(0, row_count):
            line = rd.readline()
            temp = np.array(line.split())
            for index, val in enumerate(column_indices):
                container[i][index] = float(temp[val])

    return container
