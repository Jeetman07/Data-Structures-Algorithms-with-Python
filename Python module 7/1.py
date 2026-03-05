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

    def print_network(self):
        print("Machine Network:")
        for machine, neighbors in self.machine_links.items():
            print(machine, "->", neighbors)

    def print_connected_machines(self, machine):
        if machine in self.machine_links:
            print("Machines connected to", machine, ":", self.machine_links[machine])
        else:
            print(machine, "is not in the network.")


network = MachineNetwork()

network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

network.print_network()
network.print_connected_machines("Machine_C")