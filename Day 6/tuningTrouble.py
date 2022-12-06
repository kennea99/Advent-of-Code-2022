# https://adventofcode.com/2022/day/6


def main():

    testString = 'nppdvjthqldpwncqszvftbrmjlhg'

    textFile = open('input.txt', 'r')
    data = textFile.read()
    textFile.close()

    marker = set()
    markerIndex = 0



# PART ONE
    # for ch in data:
    #     if len(marker) == 4:
    #         break
    #     if ch in marker:
    #         marker.clear()
    #         marker.add(ch)
    #         markerIndex += 1
        
    #     else:
    #         marker.add(ch)
    #         markerIndex += 1

    # print(markerIndex)

# PART TWO
    for ch in data:
        if len(marker) == 14:
            break
        if ch in marker:
            marker.clear()
            marker.add(ch)
            markerIndex += 1
        
        else:
            marker.add(ch)
            markerIndex += 1

    print(markerIndex-1)




            


if __name__ == '__main__':
    main()