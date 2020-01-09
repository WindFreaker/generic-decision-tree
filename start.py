from data_handler import *
from algorithm import *

dataset_name = input('Input dataset name: ')
print('Gathering data...')
data_set(dataset_name)
print(columns)
set_thresholds(99, 9)  # best values? needs to be improved
print('Creating tree...')
root_node = create_tree(data)

while True:
    unknown = input("Input test values: ")
    values = unknown.split(' ')
    node = root_node
    while node.answer is None:
        node = node.traverse(values[node.question])
        if node is None:
            print('There is no branch for this path')
            break
    if node is not None:
        print('Prediction: ' + str(node.answer))
