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

    bestDirSize = pc['//'][0]
    bestDir = '/'
    remainingSpace = 70000000 - pc['//'][0]
    minSize = 30000000 - remainingSpace
    print('The total size of files is', pc['//'][0], 'which means we must delete at least', minSize)

    sizes = []
    for dir in pc:
        sizes.append(pc[dir][0])
        if pc[dir][0] >= minSize and pc[dir][0] <= bestDirSize:
            bestDirSize = pc[dir][0]
            bestDir = dir

    print('The optimal dir is', bestDir, 'with size', bestDirSize)

main()