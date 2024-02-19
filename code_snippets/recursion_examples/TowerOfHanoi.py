class TowerOfHanoi:
    """
    Tower of Hanoi implementation
    """
    def __init__(self, height) -> None:
        """
        Initialize the tower with given height
        """
        self.height = height
        self.towers = {"A": [n for n in range(height, 0, -1)], "B":[], "C":[]}


    def move_tower(self, height, from_pole, with_pole, to_pole):
        """
        Moves the height number of disks from the from_pole to the to_pole, 
        using with_pole as an auxiliary
        """
        if height >= 1:
            self.move_tower(height - 1, from_pole, to_pole, with_pole)
            self.move_disk(from_pole, to_pole)
            self.move_tower(height - 1, with_pole, from_pole, to_pole)


    def move_disk(self, from_pole, to_pole):
        """
        Move a disk from the from_pole to the to_pole
        """
        print(f"Moving disk from {from_pole} to {to_pole}")
        disk = self.towers[from_pole].pop()
        self.towers[to_pole].append(disk)
        self.print_towers()


    def print_towers(self):
        for pole in self.towers:
            print(f"Tower {pole}: {self.towers[pole]}")
        print("-----------")

    def solve(self):
        self.print_towers()
        self.move_tower(self.height, "A", "B", "C")



if __name__ == "__main__":
    tof = TowerOfHanoi(4)
    tof.solve()
