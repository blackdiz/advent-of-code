with open('input.txt', 'r') as f:
    left = []
    right = []
    for line in f.readlines():
        line = line.replace('\n', '')
        left.append(line.split('   ')[0])
        right.append(line.split('   ')[1])

    left.sort()
    right.sort()

    sum = 0
    for x, y in zip(left, right):
        sum += abs(int(x) - int(y))

    print(sum)