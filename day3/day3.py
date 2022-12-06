def getPriority(val):
    val = ord(val)
    if val < 91:
        return val - 38
    return val - 96

def main():
    f = open('./day3input.txt', 'r')
    lines = f.readlines()
    total = 0
    for line in lines:
        length = len(line)
        length //= 2
        s1 = slice(0, length)
        s2 = slice(length, length * 2)
        comp1 = ''.join(set(line[s1]))
        comp2 = ''.join(set(line[s2]))

        for i in range(len(comp1)):
            if comp1[i] in comp2:
                total += getPriority(comp1[i])
                break
    print(total)
main()