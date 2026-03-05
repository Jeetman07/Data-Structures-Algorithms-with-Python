from collections import deque

q = deque()

while True:
    s = input("Enter number (empty to stop): ").strip()
    if s == "":
        break
    n = int(s)
    q.append(n)
    if len(q) > 5:
        q.popleft()

print("Final queue (last 5):", list(q))