import hashlib as hl
import random
# Task 1

def hash_function(key: int, m: int) -> int:
    return key % m


keys_task_1 = [27, 130]

print("Task 1")
print("Answer: ", end="")
[print(hash_function(key, 13), end=" ") for key in keys_task_1]
print()


# Task 2

print("\nTask 2")
keys_task_2 = [11, 12, 14, 17, 18, 19, 20, 21, 25]

print(f"Load factor after insertion: {len(keys_task_2)}/11")

hash_table = [None for _ in range(11)]
# hashed_keys = [hash_function(key, 11) for key in keys_task_2]

for key in keys_task_2:
    hashed_key = hash_function(key, 11)
    if hash_table[hashed_key] is None:
        hash_table[hashed_key] = key
    else:
        i = hashed_key
        while hash_table[i] is not None:
            i+=1
        hash_table[i] = key

print("Hash table insertion with Linear Probing:")
print(hash_table)


# Task 3

class HashClass:
    def __init__(self, id: int) -> None:
        self.id = id

    def hash_it(self) -> str:
        salted_id = str(self.id + random.randint(1,1000))
        hash_id = hl.sha1(salted_id.encode()).hexdigest()
        return hash_id

    def print_it(self) -> None:
        print("Generated hash number: ")
        print(self.hash_it())


print("\nTask 3")
my_hash = HashClass(11011999)
my_hash.print_it()

# Task 4

def most_frequent_integer(numbers: list[int]) -> int:
    frequency_table = {}
    for n in numbers:
        if n in frequency_table.keys():
            frequency_table[n] += 1
        else:
            frequency_table.update({n:1})

    return max(frequency_table, key= lambda n: frequency_table[n])

numbers = [10, 2, 5, 2, 3, 5, 6, 8, 5, 10]
result = most_frequent_integer(numbers)

print("\nTask 4")
print(f"Most frequent number: {result}")
