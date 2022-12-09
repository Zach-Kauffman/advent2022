def printRope(rope):
    for y in range(25):
        for x in range(25):
            p = True
            for r in range(len(rope)):
                if rope[r][0] + 12 == x and rope[r][1] + 12 == y and p:
                    print(r, end=" ")
                    p = False
            if x == 12 and y == 12 and p: 
                print('s ', end='')
                p = False
            if p: print('. ', end='')
        print()
    print()

def main():
    f = open('./input.txt', 'r')
    lines = f.readlines()
    r = [
        [0, 0],
        [0, 0]
    ]
    visited = []
    directions = {
        'R': [1, 0],
        'L': [-1, 0],
        'U': [0, -1],
        'D': [0, 1],
    }

    for line in lines:
        d, l = line.split(' ')
        print(line)
        for _ in range(int(l)):
            r[0][0] += directions[d][0]
            r[0][1] += directions[d][1]
            for i in range(1, len(r)):
                xdist = r[i-1][0] - r[i][0]
                ydist = r[i-1][1] - r[i][1]
                if abs(xdist) > 1 or abs(ydist) > 1:
                    if abs(xdist) + abs(ydist) > 2:
                        r[i][0] += xdist // abs(xdist)
                        r[i][1] += ydist // abs(ydist)
                    elif abs(xdist) > 1:
                        if xdist < 0: r[i][0] -= 1
                        else: r[i][0] += 1
                    elif abs(ydist) > 1:
                        if ydist < 0: r[i][1] -= 1
                        else: r[i][1] += 1
            t = tuple(r[-1])
            if t not in visited:
                visited.append(t)
        # printRope(r)

    print(len(visited))
    return


main()
