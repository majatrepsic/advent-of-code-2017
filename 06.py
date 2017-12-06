with open('inputs/06.txt') as f:
    banks = map(int, f.readline().strip().split("\t"))

configurations = set()
iterations = 0

while len(configurations) == 0 or len(configurations)==iterations:
# while iterations < 7:
    configurations.add(hash(tuple(banks)))
    iterations += 1

    # print banks
    # print hash(tuple(banks))
    # print len(configurations)
    # print iterations

    largest_bank = 0
    for i in range(0, len(banks)):
        if banks[i] > banks[largest_bank]:
            largest_bank = i

    largest_bank_size = banks[largest_bank]
    banks[largest_bank] = 0

    # distribute values in whole array
    for i in range(0, len(banks)):
        banks[i] += largest_bank_size/len(banks)

    # distribute the rest
    for i in range(0, largest_bank_size%len(banks)):
        index = (largest_bank + i + 1)% len(banks)
        banks[index] += 1

print len(configurations)



with open('inputs/06.txt') as f:
    banks = map(int, f.readline().strip().split("\t"))

configurations = list()
current_hash = hash(tuple(banks))
# configurations.append(current_hash)

while current_hash not in configurations:
# while iterations < 7:

    configurations.append(current_hash)
    # iterations += 1

    # print banks
    # print hash(tuple(banks))
    # print len(configurations)
    # print iterations

    largest_bank = 0
    for i in range(0, len(banks)):
        if banks[i] > banks[largest_bank]:
            largest_bank = i

    largest_bank_size = banks[largest_bank]
    banks[largest_bank] = 0

    # distribute values in whole array
    for i in range(0, len(banks)):
        banks[i] += largest_bank_size/len(banks)

    # distribute the rest
    for i in range(0, largest_bank_size%len(banks)):
        index = (largest_bank + i + 1)% len(banks)
        banks[index] += 1

    current_hash = hash(tuple(banks))

print len(configurations)

