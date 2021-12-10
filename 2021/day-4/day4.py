with open("input-small.txt") as file:
    input = file.readlines()
    input = [line.rstrip() for line in input]

numbers = [int(num) for num in input[0].split(",")]
boards = []
flags = []

def populateBoards(boards, flags):
    pointer = 2

    while pointer + 5 <= len(input):
        boards.append([[int(cell) for cell in row.split()] for row in input[pointer:pointer+5]])
        flags.append([[0 for cell in row.split()] for row in input[pointer:pointer+5]])
        pointer += 6

def isBingo(board):
    for row in board:
        if row.count(1) == 5:
            return True
    for i in range(0, 5):
        if [row[i] for row in board].count(1) == 5:
            return True
    return False

def calculateScore(board, flag):
    score = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if flag[i][j] == 0:
                score += board[i][j]
    return score

def processNumbers(numbers):
    winners = {}
    for num in numbers:
        for i in range(len(boards)):
            for row in range(5):
                for col in range(5):
                    if boards[i][row][col] == num:
                        flags[i][row][col] = 1
            if isBingo(flags[i]) and i not in winners:
                winners[i] = calculateScore(boards[i], flags[i]) * num
    return winners

populateBoards(boards, flags)

print("The winners are: " + str(processNumbers(numbers)))