import csv

checksum = 0
with open('inputs/02.csv', 'rb') as csvfile:
    input_reader = csv.reader(csvfile, delimiter='\t')
    for row in input_reader:
        min = int(row[0])
        max = int(row[0])
        for cell in row:
            #print cell
            if int(cell) < min:
                min = int(cell)
            if int(cell) > max:
                max = int(cell)
        checksum += int(max-min)
#print checksum

div_checksum = 0
with open('inputs/02.csv', 'rb') as csvfile:
    input_reader = csv.reader(csvfile, delimiter='\t')
    for row in input_reader:
        for i in range(0, len(row)):
            for j in range(0, len(row)):
                # print 'inspecting ' + str(i) + ' / ' + str(j)
                if i != j and int(row[i])%int(row[j]) == 0:
                    print 'divisible ' + row[i] + ' / ' + row[j]
                    div_checksum += int(row[i])/int(row[j])

print div_checksum

