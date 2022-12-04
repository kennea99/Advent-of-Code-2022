
# https://adventofcode.com/2022/day/4

def main():
    p1 = 0
    l = []

    overLapCount = 0
    overLapCount2 = 0

    with open('input.txt', 'r') as file:
        for line in file:
            currentLine = line.strip()
            l.append(currentLine.split(','))



        for i in range(len(l)):
            startTime1 = l[i][0][:2].replace('-', '')
            endTime1 = l[i][0][2:].replace('-', '')
            startTime2 = l[i][1][:2].replace('-', '')
            endTime2 = l[i][1][2:].replace('-', '')
            
            if int(startTime1) <= int(startTime2) and int(endTime2) <= int(endTime1) or int(startTime2) <= int(startTime1) and int(endTime1) <= int(endTime2):
                overLapCount += 1

            if not (int(endTime1) < int(startTime2) or int(startTime1) > int(endTime2)):
                overLapCount2 += 1

    print(overLapCount) # part one

    print(overLapCount2) # part two
            







        # print(l)


                


if __name__ == '__main__':
    main()