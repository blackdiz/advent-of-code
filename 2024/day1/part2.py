from collections import Counter

with open('input.txt', 'r') as f:
    left = []
    right = []
    for line in f.readlines():
        line = line.replace('\n', '')
        left.append(line.split('   ')[0])
        right.append(line.split('   ')[1])

    counter = Counter(right)
    sum = 0
    for num in left:
        if counter.get(num):
            sum += counter.get(num) * int(num)

    print(sum)