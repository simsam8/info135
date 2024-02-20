class MiniBank:
    def __init__(self, balance=0, bills=None) -> None:
        self.balance = balance
        self.bills = {} if bills is None else self.format_bills(bills)


    def format_bills(self, bills: list):
        return {bill[0]: bill[1] for bill in bills}

    def deposit(self, amount: int):
        if amount > 0:
            self.balance += amount
            print(f"An amount of {amount} was deposited.")
            print(f"New balance: {self.balance}")
        else:
            print(f"Invalid amount {amount}")

    def withdraw(self, amount: int):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"An amount of {amount} was withdrawed.")
            print(f"New balance: {self.balance}")
        else:
            print(f"Invalid amount {amount}")


    def sort_bills(self, bills: dict):
        sorted_bills = dict(sorted(bills.items(), key=lambda x: x[1], reverse=True))
        return sorted_bills

    def display_bills(self):
        self.bills = self.sort_bills(self.bills)
        print(f"---- All bills ----")
        for bill, amount in self.bills.items():
            print(f"{bill}: {amount}")



if __name__ == "__main__":
    bills = [("electric", 5000), ("water", 2200), ("wolfram alpha", 150)]
    mini_bank = MiniBank(0, bills)
    mini_bank.display_bills()

