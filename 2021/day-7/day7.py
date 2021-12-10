with open("input.txt") as file:
    input = file.readlines()
    input = [line.rstrip() for line in input]
    input = [int(num) for num in input[0].split(",")]
    input.sort()

def part1(input):
    costMap = {}
    for currentPosition in range(input[0],input[-1]+1):
        costMap[currentPosition] = 0
        for position in input:
            costMap[currentPosition] += abs(position - currentPosition)
    return sorted(costMap.values())[0]

def part2(input):
    costMap = {}
    for currentPosition in range(input[0],input[-1]+1):
        costMap[currentPosition] = 0
        for position in input:
            delta = abs(position - currentPosition)
            fuel = int(delta * (delta + 1) / 2)
            costMap[currentPosition] += fuel
    return sorted(costMap.values())[0]

print("The part1 value is: " + str(part1(input)))

print("The part2 value is: " + str(part2(input)))