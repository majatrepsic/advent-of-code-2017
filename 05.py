# Part 1
with open('inputs/05.txt') as f:
    maze = map(int, f.read().splitlines())

position = next_position = 0
steps = 0
while next_position >= 0 and next_position < len(maze):
    current_value = maze[position]
    next_position = position + current_value
    maze[position] += 1
    position = next_position
    steps += 1
print steps

# Part 2
with open('inputs/05.txt') as f:
    maze = map(int, f.read().splitlines())

position = next_position = 0
steps = 0
while next_position >= 0 and next_position < len(maze):
    current_value = maze[position]
    next_position = position + current_value
    if current_value >= 3:
        maze[position] -= 1
    else:
        maze[position] += 1
    position = next_position
    steps += 1
print steps