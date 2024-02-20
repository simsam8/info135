class Fridge:
    def __init__(self) -> None:
        self.temperature = 0
        self.open = False
        self.items = []

    def open_fridge(self):
        if self.open:
            print("Fridge already open.")
        else:
            print("Opening fridge...")
            self.open = True

    def close_fridge(self):
        if not self.open:
            print("Fridge is already closed.")
        else:
            print("")
            self.open = False

    def add_item(self, fridge_item):
        if self.open:
            print(f"Adding {fridge_item} to fridge")
            self.items.append(fridge_item)
        else:
            print("Fridge not open")

    def remove_item(self, fridge_item):
        if self.open:
            print(f"Removing {fridge_item} from fridge")
            self.items.remove(fridge_item)
        else:
            print("Fridge not open")

    def decrease_temperature(self):
        self.temperature -= 1
        print(f"Temperature decreased to {self.temperature}")

    def increase_temperature(self):
        self.temperature += 1
        print(f"Temperature increased to {self.temperature}")


class FridgeItem:
    def __init__(self, name, expiration_date) -> None:
        self.name = name
        self.expiration_date = expiration_date

    def __str__(self) -> str:
        return self.name


if __name__ == "__main__":
    fridge = Fridge()
    milk = FridgeItem("milk", "today")
    cheese = FridgeItem("cheese", "tomorrow")
    fridge.close_fridge()
    fridge.add_item(milk)

    fridge.open_fridge()
    fridge.add_item(milk)
    fridge.decrease_temperature()

