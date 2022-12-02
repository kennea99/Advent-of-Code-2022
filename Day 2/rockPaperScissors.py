# https://adventofcode.com/2022/day/2


def partOne(totalScore):

########################################################
# A -> Elf chooses ROCK      # X -> You choose ROCK
# B -> Elf chooses PAPER     # Y -> You choose Paper
# C -> Elf chooses SCISSORS  # Z -> You choose SCISSORS
########################################################

    playerMove = {
        'X' : 1,
        'Y' : 2,
        'Z' : 3,
    }

    winningOutcomes = {
        'A Y': 6,
        'B Z': 6,
        'C X': 6,
    }

    drawOutcomes = {
        'A X': 3,
        'B Y': 3,
        'C Z': 3,
    }

    win = 6
    draw = 3
    lose = 0

    totalScore = 0

    with open('input.txt', 'r') as file:
        for line in file:
            if winningOutcomes.get(line.strip()):
                totalScore += win + playerMove[line.strip()[-1]]
            
            elif drawOutcomes.get(line.strip()):
                totalScore += draw + playerMove[line.strip()[-1]]

            else:
                totalScore += lose + playerMove[line.strip()[-1]]

    print(f'Total Score Part One: {totalScore}')



def partTwo(totalScores):

########################################################
# A -> Elf chooses ROCK      # X -> You Lose
# B -> Elf chooses PAPER     # Y -> You Draw
# C -> Elf chooses SCISSORS  # Z -> You Win
########################################################

    rock = 1
    paper = 2
    scissors = 3

    winningOutcomes = {
        'A Z': 6 + paper,
        'B Z': 6 + scissors,
        'C Z': 6 + rock,
    }

    drawOutcomes = {
        'A Y': 3 + rock,
        'B Y': 3 + paper,
        'C Y': 3 + scissors,
    }

    losingOutcomes = {
        'A X': 0 + scissors,
        'B X': 0 + rock,
        'C X': 0 + paper,
    }


    with open('input.txt', 'r') as file:
        for line in file:
            newLine = line.strip()
            if winningOutcomes.get(newLine):
                totalScores += winningOutcomes[newLine]
            
            elif drawOutcomes.get(newLine):
                totalScores += drawOutcomes[newLine]
            
            else:
                totalScores += losingOutcomes[newLine]
    
    print(f'Total Scores Part Two: {totalScores}')



def main():

# PART 1
    totalScoresPartOne = 0
    partOne(totalScoresPartOne)





# PART 2
    totalScoresPartTwo = 0
    partTwo(totalScoresPartTwo)






if __name__ == '__main__':
    main()