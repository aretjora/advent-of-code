def part1(input):
    data = {}
    for row in input:
        explode = list(row.strip())
        for index, element in enumerate(explode):
            if index in data.keys():
                data[index] += int(element)
            else:
                data[index] = int(element) 

    gamma = ""
    epsilon = ""
    for item in data:
        gamma += str(int((data[item] / len(input)) > 0.5))
        epsilon += str(int((data[item] / len(input)) < 0.5))
    return int(gamma, 2) * int(epsilon, 2)

def part2(input):
    return findValue(input, 'o2') * findValue(input, 'co2')

def findValue(input, rating):
    index = 0
    while len(input) > 1:
        ones = []
        zeros = []
        for row in input:
            row = row.strip()
            if row[index] == '1':
                ones.append(row)
            else:
                zeros.append(row)
        index += 1
        bySize = sorted((zeros, ones), key=len)
        input = bySize[1] if rating == 'o2' else bySize[0]
    return int(input[0], 2)

input = open("input.txt").readlines()

print("The part1 value is: " + str(part1(input)))

print("The part2 value is: " + str(part2(input)))