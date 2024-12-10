with open('input.txt', 'r') as f:
    def check(levels: list[int]) -> bool:
        count = 0
        diff = 0
        while count < len(levels) - 1:
            currentDiff = levels[count] - levels[count + 1]
            if abs(currentDiff) > 3 or abs(currentDiff) < 1:
                return False
            if currentDiff < 0 and diff > 0:
                return False
            if currentDiff > 0 and diff < 0:
                return False

            diff = currentDiff
            count += 1

        return True

    safeCount = 0
    for line in f.readlines():
        line = line.replace('\n', '')
        levels = [int(item) for item in line.split(' ')]
        if check(levels):
            safeCount += 1
        else:




    print(safeCount)

