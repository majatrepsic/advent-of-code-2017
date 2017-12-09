import re

#class WeightedNode:


with open('inputs/07.txt') as f:
    tree = dict()
    for line in f:
        line_matcher = re.match(r"(\w+) \((\d+)\)(.*)", line)
        name = line_matcher.group(1)
        weight = line_matcher.group(2)
        value = line_matcher.group(3)
        tree[name] = None
        if len(value) > 0:
            tree_node = dict()
            subvalue_list = re.findall(r'\w+', value)
            for subvalue in subvalue_list:
                tree_node[subvalue] = None
            tree[name] = tree_node

# i = 0
# while len(tree.keys()) > 1 and i < 20:
#     i += 1
#     for root_key, root_value in tree.items():
#         if root_value is not None:
#             subtree = root_value
#             subtree_key = root_key
#             for k in subtree.keys():
#                 if tree.has_key(k) and tree[k] is None:
#                     del tree[k]
#                     del subtree[k]
#             if len(subtree) == 0:
#                 del tree[subtree_key]
#
#     print len(tree.keys())
# print tree.keys()[0]

