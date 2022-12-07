# https://adventofcode.com/2022/day/7

def main():

    filePath = []


    with open('input.txt', 'r') as file:
        for line in file:
            words = line.strip().split()
            print(words)
            if words[1] == 'cd':
                if words[2] == '..':
                    filePath.pop()
                else:
                    filePath.append(words[2])
            


if __name__ == '__main__':
    main()