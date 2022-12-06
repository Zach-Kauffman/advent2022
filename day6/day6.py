def hasDupes(set):
    for i in range(len(set)):
        if set[i] in set[i+1:len(set)]:
            return True

def main():
    f = open('./day6input.txt', 'r')
    lines = f.readlines()
    line = lines[0]
    prev3 = [
        line[0],
        line[1],
        line[2]
    ]
    for i in range(3, len(line)):
        prev3.append(line[i])
        if hasDupes(prev3):
            prev3.pop(0)
        else: 
            print(prev3, "is valid after", i + 1, "characters")
            print(i + 1)
            break

main()