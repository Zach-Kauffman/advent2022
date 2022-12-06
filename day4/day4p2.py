def overlaps(elf1, elf2):
    elf1min = int(elf1[0])
    elf1max = int(elf1[1])

    elf2min = int(elf2[0])
    elf2max = int(elf2[1])

    for i in range(elf1min, elf1max + 1):
        if i >= elf2min and i <= elf2max:
            return True
    return False

def main():
    f = open('./day4input.txt', 'r')
    lines = f.readlines()

    total = 0
    for line in lines:
        pairs = line.split(',')
        elf1 = pairs[0].split('-')
        elf2 = pairs[1].split('-')

        if overlaps(elf1, elf2): 
            total += 1

    print(total)

main()