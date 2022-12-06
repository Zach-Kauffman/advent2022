def isContainedBy(elf1, elf2):
    return (int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])) or (int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1]))

def main():
    f = open('./day4input.txt', 'r')
    lines = f.readlines()

    total = 0
    for line in lines:
        pairs = line.split(',')
        elf1 = pairs[0].split('-')
        elf2 = pairs[1].split('-')

        if isContainedBy(elf1, elf2): 
            total += 1

    print(total)

main()