def process_command(numbers, command):
    parts = command.split()
    operation = parts[0]

    if operation == "insert":
        numbers.insert(int(parts[1]), int(parts[2]))
    elif operation == "remove":
        numbers.remove(int(parts[1]))
    elif operation == "append":
        numbers.append(int(parts[1]))
    elif operation == "sort":
        numbers.sort()
    elif operation == "pop":
        numbers.pop()
    elif operation == "reverse":
        numbers.reverse()
    elif operation == "print":
        return numbers.copy()