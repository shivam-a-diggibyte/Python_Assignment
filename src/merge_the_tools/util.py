def create_unique_part(part):
    result = ""

    for char in part:
        if char not in result:
            result += char

    return result


def merge_the_tools(string, k):
    for start in range(0, len(string), k):
        part = string[start:start + k]
        print(create_unique_part(part))