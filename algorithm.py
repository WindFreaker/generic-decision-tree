from collections import Counter
from math import log2


class TreeNode:
    def __init__(self, question, answer):
        self.question = question
        self.branches = []
        self.answer = answer

    def set_branch(self, answer, node):
        self.branches.append([answer, node])

    def traverse(self, test):
        for branch in self.branches:
            if branch[0] == test:
                return branch[1]
        return None

    def print_path(self):
        if self.answer is None:
            print('Question: ' + str(self.question))
            for branch in self.branches:
                branch[1].print_path()
        else:
            print('Answer: ' + str(self.answer))


def create_tree(data):
    return fill_branch(data, [])


def print_tree(node):
    node.print_path()


intermediate_threshold = 1  # good threshold around 99 (>99%)
terminal_threshold = 1      # good threshold around 9 (>90%)


def set_thresholds(v1, v2):
    global intermediate_threshold, terminal_threshold
    intermediate_threshold = v1
    terminal_threshold = v2


def fill_branch(data, excluded):
    value = value_test(data, intermediate_threshold)
    if value is not None:
        return TreeNode(None, value)
    if len(data[0]) - len(excluded) == 1:
        # print(len(data))
        new_value = value_test(data, terminal_threshold)
        if new_value is not None:
            return TreeNode(None, new_value)
        # print(count_data(data))
        return TreeNode(None, 'Undefined')
    gain_index = calc_gains(data, excluded)
    excluded.append(gain_index)
    new_node = TreeNode(gain_index, None)
    branches = branch_list(gain_index, data)
    for branch in branches:
        new_node.set_branch(branch, fill_branch(reduce_data(gain_index, branch, data), excluded))
    return new_node


def calc_gains(data, excluded):
    column_count = len(data[0]) - 1
    default_value = data[0][-1]
    total_rows = len(data)
    gains = []
    for a in range(column_count):
        if a in excluded:
            gains.append(2)  # arbitrary addition so indexes are in correct positions
            continue
        values = []
        pos_values = []
        neg_values = []
        for row in data:
            if row[a] not in values:
                values.append(row[a])
            if row[-1] == default_value:
                pos_values.append(row[a])
            else:
                neg_values.append(row[a])
        gain = 0
        for value in values:
            p_cnt = pos_values.count(value)
            n_cnt = neg_values.count(value)
            t_cnt = p_cnt + n_cnt
            try:
                gain += (t_cnt / total_rows) * (-p_cnt/t_cnt * log2(p_cnt/t_cnt) - n_cnt/t_cnt * log2(n_cnt/t_cnt))
            except ValueError:
                pass  # log2 0 error, adding nothing to gain
        gains.append(gain)
    return gains.index(min(gains))


def branch_list(index, data):
    answers = []
    for row in data:
        if row[index] not in answers:
            answers.append(row[index])
    return answers


def value_test(data, threshold):
    list = []
    for entry in data:
        list.append(entry[-1])
    counted = Counter(list)
    common = counted.most_common(2)
    if len(common) == 1:
        name, temp = common[0]
        return name
    one_name, one_count = common[0]
    two_name, two_count = common[1]
    if one_count > two_count * threshold:
        return one_name
    else:
        return None


def reduce_data(index, value, data):
    new_data = []
    for row in data:
        if row[index] == value:
            new_data.append(row)
    return new_data
