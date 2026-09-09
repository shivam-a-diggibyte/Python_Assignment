from src.word_order.util import count_words

def main():
    n = int(input())

    words = []

    for _ in range(n):
        words.append(input().strip())

    distinct_count, counts = count_words(words)

    print(distinct_count)
    print(*counts)

if __name__ == "__main__":
    main()