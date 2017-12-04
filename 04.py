import csv

# Part one

valid_inputs = 0
with open('inputs/04.txt', 'rb') as csvfile:
    input_reader = csv.reader(csvfile, delimiter=' ')
    for row in input_reader:
        # print len(row)
        # print len(set(row))
        if len(row) == len(set(row)):
            valid_inputs += 1
print valid_inputs

# Part two

def check_permutations(row):
    for i in range(0,len(row)):
        for j in range (i+1, len(row)):
            # print row[i] + ',' + row[j]
            # print str(sorted(row[i])) + ',' + str(sorted(row[j]))
            if (len(row[i]) == len(row[j])) \
                    and (sorted(row[i]) == sorted(row[j])):
                return False
    return True


valid_inputs_permutation = 0
with open('inputs/04.txt', 'rb') as csvfile:
    input_reader = csv.reader(csvfile, delimiter=' ')
    for row in input_reader:
        if len(row) == len(set(row)):
            # print row
            if check_permutations(row):
                valid_inputs_permutation += 1
print valid_inputs_permutation