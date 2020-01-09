import csv
import math
from collections import Counter

columns = []
data = []
folded_data = []


def data_set(name):
    with open(f'Datasets/{name}.csv') as file:
        reader = csv.reader(file, delimiter=';')
        columns.append(next(reader))
        for row in reader:
            data.append(row)


def return_point(column, row):
    print(data[int(row)][int(column)])


def fold_data(k):
    new_space = math.ceil(len(data) / k)
    for a in range(k):
        folded_data.append([])
    for a in range(len(data)):
        folded_data[int(a / new_space)].append(data[a])


def count_data(test_data):
    results_list = []
    for row in test_data:
        results_list.append(row[-1])
    results_count = Counter(results_list)
    print(results_count)
