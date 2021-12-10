def part1(input):
    counter = 0
    lastValue = 0
    for row in input:
        value = int(row)
        if value > lastValue and lastValue != 0:
            counter += 1
        lastValue = value
    return counter

def part2(input):
    counter = 0
    lastValue = 0
    for i in range(len(input) - 2):
        rangeValue = int(input[i]) + int(input[i + 1]) + int(input[i + 2])
        if lastValue != 0 and rangeValue > lastValue:
            counter += 1
        lastValue = rangeValue
    return counter

input = open("input.txt").readlines()

print("The part1 value is: " + str(part1(input)))

print("The part2 value is: " + str(part2(input)))