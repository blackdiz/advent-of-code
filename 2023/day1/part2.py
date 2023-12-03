with open('input.txt', 'r') as f:
    targets = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    mapping = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    sum = 0
    for calibration in f.read().splitlines():
        min = 10**5
        max = -1
        minDigit = ""
        maxDigit = ""
        for target in targets:
            idx = calibration.find(target)
            if idx != -1 and idx < min:
                min = idx
                minDigit = target
            idx = calibration.rfind(target)
            if idx != -1 and idx > max:
                max = idx
                maxDigit = target

        try:
            sum += (mapping.index(minDigit) + 1) * 10
        except ValueError:
            sum = sum + int(minDigit) * 10

        try:
            sum += (mapping.index(maxDigit) + 1)
        except ValueError:
            sum += int(maxDigit)

    print(sum)