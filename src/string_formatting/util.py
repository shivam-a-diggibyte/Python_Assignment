def format_numbers(number):
    width = len(bin(number)[2:])

    for value in range(1, number + 1):
        decimal = str(value)
        octal = oct(value)[2:]
        hexadecimal = hex(value)[2:].upper()
        binary = bin(value)[2:]

        print(
            decimal.rjust(width),
            octal.rjust(width),
            hexadecimal.rjust(width),
            binary.rjust(width)
        )