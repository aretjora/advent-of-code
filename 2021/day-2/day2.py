def part1(input):
    horizontal = 0
    depth = 0
    for row in input:
        parse = row.strip().split(" ")
        direction = parse[0]
        value = int(parse[1])
        if direction == "forward":
            horizontal += value
        elif direction == "up":
            depth -= value
        elif direction == "down":
            depth += value
        
    return horizontal * depth

def part2(input):
    horizontal = 0
    depth = 0
    aim = 0
    for row in input:
        parse = row.strip().split(" ")
        direction = parse[0]
        value = int(parse[1])
        if direction == "forward":
            horizontal += value
            depth += aim * value
        elif direction == "up":
            aim -= value
        elif direction == "down":
            aim += value
    
    return horizontal * depth

input = open("input.txt").readlines()

print("The part1 value is: " + str(part1(input)))

print("The part2 value is: " + str(part2(input)))