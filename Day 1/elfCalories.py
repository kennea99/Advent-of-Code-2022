# https://adventofcode.com/2022/day/1

def main():
    sumCalories = []

    elf = []

    with open('input.txt', 'r') as file:
        for line in file:
            if line != '\n':
                elf.append(int(line.strip()))


            else:
                ans = sum(elf)
                sumCalories.append(ans)
                elf = []

    # PART 1. Getting the elf with the most calories
    # print(max(sumCalories))


    # PART 2. Getting the top three elves with the most calories and their sum.
    topThree = []
    for i in range(0, 3):
        idx = sumCalories.index(max(sumCalories))
        highest = max(sumCalories)
        topThree.append(highest)

        sumCalories.pop(idx)

    print(sum(topThree))



if __name__ == '__main__':
    main()