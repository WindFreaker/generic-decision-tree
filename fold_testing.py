from data_handler import *
from algorithm import *

dataset_name = input('Input dataset name: ')
data_set(dataset_name)

threshold_one = int(input('Input intermediate threshold: '))
threshold_two = int(input('Input terminal threshold: '))
set_thresholds(threshold_one, threshold_two)

fold_count = int(input('Input fold count: '))

missing_branch_total = 0
successful_total = 0
undefined_total = 0
failed_total = 0

fold_data(fold_count)
for a in range(fold_count):
    print(f'Testing fold #{a + 1}...')
    missing_branch_runs = 0
    successful_runs = 0
    undefined_runs = 0
    failed_runs = 0
    combined_folds = []
    for b in range(fold_count):
        if a != b:
            combined_folds += folded_data[b]
    root_node = create_tree(combined_folds)
    for set in folded_data[a]:
        node = root_node
        while node.answer is None:
            node = node.traverse(set[node.question])
            if node is None:
                missing_branch_runs += 1
                break
        if node is not None:
            if node.answer == set[-1]:
                successful_runs += 1
            elif node.answer == 'Undefined':
                undefined_runs += 1
            else:
                failed_runs += 1
    print(f'S:{successful_runs} F:{failed_runs} U:{undefined_runs} MB:{missing_branch_runs}')
    missing_branch_total += missing_branch_runs
    successful_total += successful_runs
    undefined_total += undefined_runs
    failed_total += failed_runs

print()
print(f'Accuracy: {round(successful_total / (successful_total + failed_total) * 100, 3)}%')
print(f'Accuracy w/ U: {round(successful_total / (successful_total + failed_total + undefined_total) * 100, 3)}%')
print(f'Accuracy w/ MB: {round(successful_total / (successful_total + failed_total + missing_branch_total) * 100, 3)}%')
print(f'Accuracy w/ Both: {round(successful_total / (successful_total + failed_total + missing_branch_total + undefined_total) * 100, 3)}%')
print(f'Prediction made: {round((successful_total + failed_total) / (successful_total + failed_total + missing_branch_total + undefined_total) * 100, 3)}%')
