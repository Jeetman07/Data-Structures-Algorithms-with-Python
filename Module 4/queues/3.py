from collections import deque

def round_robin(tasks, quantum=2):
    q = deque(tasks)
    finished = []
    while q:
        name, time_needed = q.popleft()
        time_needed -= quantum
        if time_needed > 0:
            q.append((name, time_needed))
        else:
            finished.append(name)
    return finished

tasks = [("A", 3), ("B", 6), ("C", 1)]
print("Tasks:", tasks)
print("Completion order:", round_robin(tasks, 2))