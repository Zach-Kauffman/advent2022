def hasDupes(set):
    for i in range(len(set)):
        if set[i] in set[i+1:len(set)]:
            return True

def main():
    f = open('./day6input.txt', 'r')
    lines = f.readlines()
    line = lines[0]
    prev13 = [
        line[0],
        line[1],
        line[2],
        line[3],
        line[4],
        line[5],
        line[6],
        line[7],
        line[8],
        line[9],
        line[10],
        line[11],
        line[12],
    ]
    for i in range(13, len(line)):
        prev13.append(line[i])
        if hasDupes(prev13):
            prev13.pop(0)
        else: 
            print(prev13, "is valid after", i + 1, "characters")
            break

main()