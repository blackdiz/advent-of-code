with open('input.txt', 'r') as f:
    sum = 0
    for game in f.read().splitlines():
        gameId, displays = game.split( ":")
        gameId = gameId.split(" ")[1]
        maxDic = {}
        for display in displays.split(";"):
            for sets in display.split(", "):
                count, color = sets.strip().split(" ")
                count = int(count)
                maxDic[color] = max(maxDic.get(color, 0), count)

        power = 1
        for count in maxDic.values():
            power *= count

        sum += power


    print(sum)
