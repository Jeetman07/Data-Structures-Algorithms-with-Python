def check_balance(text):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    open_brackets = set(pairs.values())
    close_brackets = set(pairs.keys())

    count = 0

    for i, char in enumerate(text):
        if char in open_brackets:
            stack.push((char, i))

        elif char in close_brackets:
            top = stack.pop()
            if top is None or top[0] != pairs[char]:
                return f"Match error at position {i}"
            count += 1

    if len(stack) != 0:
        # Unmatched opening bracket remains
        _, pos = stack.pop()
        return f"Match error at position {pos}"

    return f"Ok - {count}"
