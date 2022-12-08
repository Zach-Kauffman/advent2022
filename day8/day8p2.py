def main():
    f = open('input.txt', 'r')
    lines = f.readlines()
    best = 0
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[0])-2):
            height = lines[i][j]
            vis = [1, 1, 1, 1]
            # left
            for x in range(j-1, 0, -1):
                if lines[i][x] < height:
                    vis[0] += 1
                else: break
            # right
            for x in range(j+1, len(lines)-1):
                if lines[i][x] < height:
                    vis[1] += 1
                else: break
            # up
            for y in range(i-1, 0, -1):
                if lines[y][j] < height:
                    vis[2] += 1
                else: break
            # down
            for y in range(i+1, len(lines[0])-2):
                if lines[y][j] < height:
                    vis[3] += 1
                else: break
            
            scenicScore = vis[0] * vis[1] * vis[2] * vis[3]
            if scenicScore >= best:
                best = scenicScore
    print(best)
    return

main()