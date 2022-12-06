def getPriority(val):
    val = ord(val)
    if val < 91:
        return val - 38
    return val - 96

def main():
    f = open('./day3input.txt', 'r')
    lines = f.readlines()
    total = 0
    for i in range(0, len(lines), 3):
        elf1 = lines[i]
        elf2 = lines[i + 1]
        elf3 = lines[i + 2]
        for i in range(len(elf1)):
            if elf1[i] in elf2 and elf1[i] in elf3:
                total += getPriority(elf1[i])
                break
    print(total)
main()


