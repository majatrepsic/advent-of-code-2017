import re
with open('inputs/07.txt') as f:
    all_keys = set()
    all_values = set()
    for line in f:
        line_matcher = re.match(r"(\w+) \((\d+)\)(.*)", line)
        name = line_matcher.group(1)
        all_keys.add(name)
        values = line_matcher.group(3)
        if len(values) > 0:
            subvalue_list = re.findall(r'\w+', values)
            for subvalue in subvalue_list:
                all_values.add(subvalue)

for key in all_keys:
    if key not in all_values:
        print key