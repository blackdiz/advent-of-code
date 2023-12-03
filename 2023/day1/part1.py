with open('input.txt', 'r') as f:
    sum = 0
    for calibration in f.read().splitlines():
        r = 0
        l = len(calibration) - 1
        while r < l:
            if calibration[r].isdigit():
                sum += int(calibration[r]) * 10
                break
            else:
                r += 1

        while l >= 0:
            if calibration[l].isdigit():
                sum += int(calibration[l])
                break
            else:
                l -= 1

    print(sum)
