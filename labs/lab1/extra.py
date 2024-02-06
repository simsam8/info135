# Task 1


def my_function(some_list):
    for item1 in some_list:
        for item2 in some_list:
            print(item1, item2)


# Has time complexity O(N^2)


# Task 2


class StringReverser:
    @staticmethod
    def reverse_string(string: str):
        list_string = string.split(" ")
        list_string.reverse()
        return str.join(" ", list_string)


pre = "I am a programmer"

reverse = StringReverser.reverse_string(pre)

print(pre)
print(reverse)
