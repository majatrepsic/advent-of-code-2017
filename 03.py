import math
inputs = [10, 11, 19, 23, 31, 32, 1024, 361527]
#inputs = [1, 12, 23, 1024]
#n = 19

#1 - 0
# 10 -3
# 11 - 2
#12 -3
#23 - 2
# 31
# 32 - 5
#1024 - 31

for n in inputs:
    print 'n: ' + str(n)
    next_root = math.ceil(math.sqrt(n))
    next_odd_root = 0
    if next_odd_root%2 != 0:
        next_odd_root = next_root
    else:
        next_odd_root = next_root +1
    print 'next odd root: ' + str(next_odd_root)


    last_in_square = next_odd_root*next_odd_root
    print 'last_in_square: ' + str(last_in_square)
    distance_from_last_in_square = last_in_square-n
    print 'distance_from_last_in_square: ' + str(distance_from_last_in_square)

    min_circle_value = math.floor(next_odd_root/2)
    print 'min_circle_value: ' + str(min_circle_value)

    distance_from_corner = distance_from_last_in_square % (next_odd_root-1)
    print 'distance_from_corner: ' + str(distance_from_corner)

    if distance_from_corner > next_odd_root/2:
        distance_from_corner = next_odd_root-1 - distance_from_corner
        print 'distance_from_corner: ' + str(distance_from_corner)

    solution = next_odd_root-1-distance_from_corner

    print 'solution: ' + str(solution)
    print '------------------------'