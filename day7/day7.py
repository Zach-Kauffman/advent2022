pc = {}
path = []
pwd = ''

def getDirInfo(lines, index):
    dirs = []
    size = 0
    for i in range(index, len(lines)):
        cmd = lines[i].split(' ')
        if cmd[0] == 'dir':
            dirs.append(pwd + cmd[1][0:-1] + '/')
        elif cmd[0].isnumeric():
            size += int(cmd[0])
        else:
            return [size, dirs, False]
    # handle final command
    return [size, dirs, False]

def getDirSize(dir):
    size = int(pc[dir][0])
    if not pc[dir][2]:          # if dir hasn't already been visited
        if not pc[dir][1]:      # if there are no subdirs, we can just return the size of all files
            pc[dir][2] = True
        else:                   # if there are subdirs, we need to get all their respective sizes
            for subDir in pc[dir][1]:
                size += getDirSize(dir+subDir)
            pc[dir][0] = size   # set dir size equal to total size of subdirs plus its own files
            pc[dir][2] = True
    return size

def main():
    f = open('./input.txt', 'r')
    lines = f.readlines()
    maxSize = 100000
    total = 0

    for i in range(len(lines)):
        cmd = lines[i].split(' ')
        if cmd[1] == 'cd':
            if cmd[2] == '..\n':
                path.pop(-1)
            else:
                path.append(cmd[2][0:-1])
        elif cmd[1] == 'ls\n':
            pwd = ''
            for dir in path:
                pwd += dir + '/'
            pc[pwd] = getDirInfo(lines, i + 1)
    
    for dir in pc:
        getDirSize(dir)
        if pc[dir][0] <= maxSize:
            total += pc[dir][0]

    print(total)

main()