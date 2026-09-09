from src.validate_email.util import fun

def main():
    n = int(input())
    emails = []

    for _ in range(n):
        email = input().strip()

        if fun(email):
            emails.append(email)

    emails.sort()

    print(emails)


if __name__ == "__main__":
    main()