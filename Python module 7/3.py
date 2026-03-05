class MachineNetwork:
    def __init__(self):
        self.machine_links = {}

    def add_machine(self, machine):
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        self.add_machine(m1)
        self.add_machine(m2)

        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)

        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def bfs(self, start):
        if start not in self.machine_links:
            print("Error: Machine not found.")
            return []

        visited = []
        queue = [start]

        while queue:
            current = queue.pop(0)

            if current not in visited:
                visited.append(current)
                for neighbor in self.machine_links[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return visited

    def dfs(self, start):
        if start not in self.machine_links:
            print("Error: Machine not found.")
            return []

        visited = []
        stack = [start]

        while stack:
            current = stack.pop()

            if current not in visited:
                visited.append(current)
                for neighbor in self.machine_links[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited


network = MachineNetwork()

network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

print(network.dfs("Machine_A"))