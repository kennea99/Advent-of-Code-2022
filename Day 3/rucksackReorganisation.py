# https://adventofcode.com/2022/day/3


import math

def partOne(priorities):

    with open('input.txt', 'r') as file:
        for line in file:
            currentLine = line.strip()
            l = len(currentLine)-1
            compartment1 = currentLine[:math.ceil(l/2)]
            compartment2 = currentLine[math.ceil(l/2):]
            for ch in compartment1:
                if ch in compartment2:
                    if ch.islower():
                        priorities.append(ord(ch) - 96)  # Convert Unicode value to priorty values
                        break
                    
                    else:
                        priorities.append(ord(ch) - 38)  # Convert Unicode value to priorty values
                        break

    print(f'Total for Part 1: {sum(priorities)}')

def partTwo(priorities):
    badges = []


    with open('input.txt', 'r') as file:
        for line in file:
            badges.append(line.strip())

        for i in range(0, len(badges), 3):
            for ch in badges[i]:
                if ch in badges[i+1] and ch in badges[i+2]:
                    if ch.islower():
                        priorities.append(ord(ch) - 96)
                        break
                    
                    else:
                        priorities.append(ord(ch) - 38)
                        break
                    
        print(f'Total for Part 2: {sum(priorities)}')


def main():
    prioritiesPart1 = []
    partOne(prioritiesPart1)

    prioritiesPart2 = []
    partTwo(prioritiesPart2)








if __name__ == '__main__':
    main()