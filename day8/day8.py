def printVisibility(arr):
    str = "is visible from "
    if arr[0]: str += "left "
    if arr[1]: str += "right "
    if arr[2]: str += "up "
    if arr[3]: str += "down "
    return str

def main():
    f = open('input.txt', 'r')
    lines = f.readlines()
    perimiter = ( len(lines) * 4)  - 4
    total = 0
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[0])-2):
            height = lines[i][j]
            vis = [True, True, True, True]
            # left
            for x in range(0, j):
                if lines[i][x] >= height:
                    vis[0] = False
                    break
            # right
            for x in range(j+1, len(lines)):
                if lines[i][x] >= height:
                    vis[1] = False
                    break
            # up
            for y in range(0, i):
                if lines[y][j] >= height:
                    vis[2] = False
                    break
            # down
            for y in range(i+1, len(lines[0])-1):
                if lines[y][j] >= height:
                    vis[3] = False
                    break
            
            if True in vis:
                print("tree of height", height, "at", j, i, printVisibility(vis))
                total += 1
    total += perimiter
    print(total)
    return

main()