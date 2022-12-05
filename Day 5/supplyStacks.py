# https://adventofcode.com/2022/day/5


# [F]         [L]     [M]            
# [T]     [H] [V] [G] [V]            
# [N]     [T] [D] [R] [N]     [D]    
# [Z]     [B] [C] [P] [B] [R] [Z]    
# [M]     [J] [N] [M] [F] [M] [V] [H]
# [G] [J] [L] [J] [S] [C] [G] [M] [F]
# [H] [W] [V] [P] [W] [H] [H] [N] [N]
# [J] [V] [G] [B] [F] [G] [D] [H] [G]
#  1   2   3   4   5   6   7   8   9 

def main():

    l = []

    stack = []

    supplies = []

    with open('input.txt', 'r') as file:
        for line in file:
            if line != '\n':
                l.append(line)
            else: 
                break
        for s in l:
            row = []
            newString = s[1::4]
            for ch in newString:
                row.append(ch)
            stack.append(row)
        stack.pop()


        n = len(stack)
        for i in range(len(stack[n-1])):
            tmp = []
            for j in range(n-1, -1, -1):
                if stack[j][i] == ' ':
                    continue
                else:
                    tmp.append(stack[j][i])
            supplies.append(tmp)
        # print(supplies)

# PART ONE (COMMENT PART TWO TO RUN)
#     with open('input.txt', 'r') as file:
#         for line in file:
#             if 'move' not in line:
#                 continue
#             else:
#                 move, frm, to = [int(s) for s in line.split() if s.isdigit()]

#                 for i in range(move):
#                     tmp = supplies[frm-1].pop()
#                     supplies[to-1].append(tmp)

# PART TWO (COMMENT PART ONE TO RUN)
    with open('input.txt', 'r') as file:
        for line in file:
            if 'move' not in line:
                continue
            else:
                move, frm, to = [int(s) for s in line.split() if s.isdigit()]

                tmpList = []
                for i in range(move):
                    tmp = supplies[frm-1].pop()
                    tmpList.append(tmp)


                tmpList.reverse()
                for i in range(len(tmpList)):
                    supplies[to-1].append(tmpList[i])



    final = ''
    for i in range(len(supplies)):
        final += supplies[i][-1]

    print(final)


    




        





if __name__ == '__main__':
    main()