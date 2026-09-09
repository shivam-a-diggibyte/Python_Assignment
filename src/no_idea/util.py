def calculate_happiness(array, liked, disliked):
    happiness = 0

    for number in array:
        if number in liked:
            happiness += 1
        elif number in disliked:
            happiness -= 1

    return happiness