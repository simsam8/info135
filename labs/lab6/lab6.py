from hashlib import sha1

# Exercise 1


def recur_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recur_factorial(n - 1)


# Exercise 2


def truncation_hash(key):
    key = str(key)
    hash_val = ""
    two_count = 1
    five_count = 1
    for k in key:
        if two_count == 3:
            hash_val += k
            two_count = 0
        if five_count == 5:
            hash_val += k
            five_count = 0
        two_count += 1
        five_count += 1
    return hash_val


def string_hash(key):
    product = 1
    for k in key:
        product *= ord(k)
    return product


# Exercise 3


class PasswordDatabase:
    def __init__(self) -> None:
        self.passwords = {}

    def prompt_credentials(self):
        username = input("Input username: ")
        password = input("Input password: ")
        return username, password

    def create_user(self):
        print("Create or update user")
        usr, pasw = self.prompt_credentials()
        pasw = sha1(pasw.encode()).hexdigest()
        if usr in self.passwords:
            self.passwords[usr] = pasw
        else:
            self.passwords.update({usr: pasw})

    def check_password(self):
        print("Check password")
        usr, pasw = self.prompt_credentials()
        return self.passwords[usr] == sha1(pasw.encode()).hexdigest()

    def update_password(self):
        if self.check_password():
            self.create_user()
        else:
            print("Invalid credentials")


if __name__ == "__main__":
    print("Exercise 1")
    print(recur_factorial(10))

    print("\nExercise 2")
    int_hashed = truncation_hash(94283641911)
    print(int_hashed)
    string_hashed = string_hash("simon")
    print(string_hashed)

    print("\nExercise 3")
    pdb = PasswordDatabase()
    print("\nCreate user")
    pdb.create_user()
    print(pdb.passwords)
    print("\nCheck password")
    matching = pdb.check_password()
    print(matching)

    print("\nUpdate password")
    pdb.update_password()
    print(pdb.passwords)
