def main():
    f = open('./day5input.txt', 'r')
    lines = f.readlines()
    height = 0
    rawdata = []
    data = []
    filling = True
    for line in lines:        
        if filling: 
            rawdata.append(line)
            height += 1
        else:
            instruction = line.split(' ')
            count = int(instruction[1])
            location = int(instruction[3]) - 1
            destination = int(instruction[5]) - 1
            for i in range(count):
                data[destination].insert(0, data[location].pop(0))

        # populate data structure
        if line == '\n' and filling: 
            filling = False
            rawdata.remove('\n')
            height -= 2
            idx = []
            for i in range(len(rawdata[-1])):
                if rawdata[-1][i].isnumeric(): idx.append(i)
            for i in idx:
                column = []
                for j in range(height):
                    if rawdata[j][i].isalpha():
                        column.append(rawdata[j][i])
                data.append(column)
            print("Before moves")
            for row in data:
                print(row)
    
    print("After moves")
    for row in data:
        print(row)
    print("Solution:")
    for row in data:
        print(row[0], end="")
    print()

main()