with open('input.txt', 'r') as f:
    sum = 0
    for game in f.read().splitlines():
        gameId, displays = game.split( ":")
        gameId = gameId.split(" ")[1]
        possible = True
        for display in displays.split(";"):
            for sets in display.split(", "):
                count, color = sets.strip().split(" ")
                count = int(count)
                if (color == "red" and count > 12) or (color == "green" and count > 13) or (color == "blue" and count > 14):
                    possible = False
                    break

            if possible == False:
                break

        if possible:
           sum += int(gameId)

    print(sum)
