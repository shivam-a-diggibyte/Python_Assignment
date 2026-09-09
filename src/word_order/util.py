def count_words(words):
    word_count = {}
    order = []

    for word in words:
        if word not in word_count:
            word_count[word] = 1
            order.append(word)
        else:
            word_count[word] += 1

    counts = [word_count[word] for word in order]

    return len(order), counts