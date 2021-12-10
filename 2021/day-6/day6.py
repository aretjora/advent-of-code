with open("input-small.txt") as file:
    input = file.readlines()
    input = [line.rstrip() for line in input]

def part1(input, cycles):
    fishes = [int(num) for num in input[0].split(",")]
    print("Initial state: " + str(len(fishes)))
    for day in range(cycles):
        for index, fish in enumerate(fishes):
            if fish > 0:
                fishes[index] -= 1
            elif fish == 0:
                fishes.append(9)
                fishes[index] = 6
        print("After " + str(day + 1) + " day(s): " + str(len(fishes)))
    return len(fishes)

def part2(input, cycles):
    fishes = [int(num) for num in input[0].split(",")]
    days = [0] * 9

    for fish in fishes:
        days[fish] += 1

    for i in range(cycles):
        today = i % len(days)

        # Add new babies
        days[(today + 7) % len(days)] += days[today]
    return sum(days)

print("The part1 value is: " + str(part1(input, 80)))

print("The part2 value is: " + str(part2(input, 256)))