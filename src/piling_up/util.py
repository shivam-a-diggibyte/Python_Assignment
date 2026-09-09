def can_stack(blocks):
    left = 0
    right = len(blocks) - 1
    previous = float("inf")

    while left <= right:
        if blocks[left] >= blocks[right]:
            current = blocks[left]
            left += 1
        else:
            current = blocks[right]
            right -= 1

        if current > previous:
            return "No"

        previous = current

    return "Yes"