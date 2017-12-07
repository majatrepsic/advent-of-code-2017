with open('inputs/07_test.txt') as f:
    tree = dict()
    for line in f:
        print line
        line_parts = line.split('->')
        k = line_parts[0].strip().split(' ')[0]
        tree[k] = None
        if len(line_parts) > 1:
            v = line_parts[1].strip()
            tree_node = dict()
            for part in v.split(','):
                tree_node[part.strip()] = None
            tree[k] = tree_node

print len(tree.keys())

# find element that is not empty

for element in tree:
    if tree[element] is not None:
        subtree = tree[element]
        for subelement in subtree:
            print subelement
            if tree.has_key(subelement):
                temp = tree[subelement]
                del tree[subelement]
                subtree[subelement] = temp
                print 'replace'

print len(tree.keys())


