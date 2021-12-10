with open("input.txt") as file:
    input = file.readlines()
    input = [line.rstrip() for line in input]

def processCellRange(cellRange):
    cells = []
    x1, y1 = tuple(int(x) for x in cellRange[0].split(","))
    x2, y2 = tuple(int(x) for x in cellRange[1].split(","))

    # Vertical/horizontal
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                cells.append((x ,y))

    # Diagonal
    else:
        xinc = 1 if x1 < x2 else -1
        yinc = 1 if y1 < y2 else -1
        y = y1
        for x in range(x1, x2 + xinc, xinc):
            cells.append((x, y))
            y += yinc
    return cells

def processGrid(input):
    grid = {}
    for line in input:
        cells = processCellRange(line.split(" -> "))
        for cell in cells:
            if cell in grid:
                grid[cell] += 1
            else:
                grid[cell] = 1

    counter = 0
    for index in grid:
        if grid[index] > 1:
            counter += 1
    return counter

print("The value is: " + str(processGrid(input)))