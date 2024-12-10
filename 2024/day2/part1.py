with open('input.txt', 'r') as f:
    safeCount = 0
    for line in f.readlines():
        line = line.replace('\n', '')
        levels = [int(item) for item in line.split(' ')]
        count = 0
        diff = 0
        safe = True
        while count < len(levels) - 1:
            currentDiff = levels[count] - levels[count + 1]
            if abs(currentDiff) > 3 or abs(currentDiff) < 1:
                safe = False
                break

            if currentDiff < 0 and diff > 0:
                safe = False
                break

            if currentDiff > 0 and diff < 0:
                safe = False
                break

            diff = currentDiff
            count += 1

        if safe:
            safeCount += 1

    print(safeCount)

