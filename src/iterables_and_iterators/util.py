from itertools import combinations

def calculate_probability(letters, k):
    total = 0
    contains_a = 0

    for indexes in combinations(range(len(letters)), k):
        total += 1

        for index in indexes:
            if letters[index] == 'a':
                contains_a += 1
                break

    return contains_a / total