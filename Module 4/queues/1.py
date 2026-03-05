from collections import deque

def reverse_first_k(q, k=3):
    s = []
    for _ in range(min(k, len(q))):
        s.append(q.popleft())
    while s:
        q.appendleft(s.pop())
    for _ in range(len(q) - min(k, len(q))):
        q.append(q.popleft())
    return q

q = deque([1, 2, 3, 4, 5])
print("Input queue: ", list(q))
reverse_first_k(q, 3)
print("Output queue:", list(q))