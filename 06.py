with open('inputs/06_test.txt') as f:
    banks = map(int, f.readline().strip().split("\t"))

configurations = set()
iterations = 0

while len(configurations) == 0 or len(configurations)==iterations:
# while iterations < 7:
    configurations.add(hash(tuple(banks)))
    iterations += 1

    print banks
    print hash(tuple(banks))
    # print len(configurations)
    # print iterations

    largest_bank = 0
    for i in range(0, len(banks)):
        if banks[i] > banks[largest_bank]:
            largest_bank = i


    # print largest_bank

    largest_bank_size = banks[largest_bank]
    banks[largest_bank] = 0

    # print largest_bank_size%len(banks)

    for i in range(0, len(banks)):
        banks[i] += largest_bank_size/len(banks)
        # print (largest_bank + i) % len(banks)
        if largest_bank_size%len(banks) != 0 \
                and i != largest_bank \
                and (largest_bank+i) % len(banks) <= largest_bank_size % len(banks):
            banks[i] += 1

print len(configurations)




# print hash(tuple([9, 12, 11, 8, 7, 6, 0, 3, 11, 1, 6, 15, 5, 13, 4, 1]))
# print hash(tuple([9, 12, 11, 8, 8, 6, 0, 3, 11, 1, 6, 14, 5, 13, 4, 1]))
