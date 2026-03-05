actions = ["open", "edit", "save", "close"]
n = 2

print("Actions stack (start):", actions)

undone = []
for _ in range(n):
    if not actions:
        break
    undone.append(actions.pop())

print("Undone:", undone)
print("Left in stack:", actions)