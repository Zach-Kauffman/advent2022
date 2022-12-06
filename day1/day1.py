def main():
    f = open('./day1input.txt', 'r')
    lines = f.readlines()
    elves = []
    curr = 0
    for line in lines:
        if line == '\n': 
            elves.append(curr)
            curr = 0
        else:
            curr += int(line)
    f.close()
    elves.sort(reverse=True)
    maximum = elves[0] + elves[1] + elves[2]
    
    # part 1
    print(elves[0])
    
    # part 2
    print(maximum)

main()