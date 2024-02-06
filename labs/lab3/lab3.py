from large_list import liste
from collections import Counter


def selection_sort_one_pass(l: list):
    print(l)
    lowest_idx = 0
    for i in range(len(l)):
        if l[i] < l[lowest_idx]:
            lowest_idx = i

    l[0], l[lowest_idx] = l[lowest_idx], l[0]
    print(l)


def selection_sort(iterable):
    for i in range(len(iterable)):
        low_idx = i
        for j in range(i + 1, len(iterable)):
            if iterable[j] < iterable[low_idx]:
                low_idx = j

        iterable[i], iterable[low_idx] = iterable[low_idx], iterable[i]

    return iterable

# selection_sort_one_pass([3, 7, 1, 9, 5, 6])


def filter_tuples(tuples: list[tuple]):
    out = []
    for tup in tuples:
        if tup[0] + tup[1] == tup[2]:
            out.append(tup)

    return out


def selection_sort_tuples(tuples: list[tuple]):
    for i in range(len(tuples)):
        low_idx = i
        for j in range(i + 1, len(tuples)):
            if tuples[j][2] < tuples[low_idx][2]:
                low_idx = j

        tuples[i], tuples[low_idx] = tuples[low_idx], tuples[i]

    return tuples


filtered_tups = filter_tuples(liste)
print(selection_sort_tuples(filtered_tups))


def is_anagram_with_counter(a: str, b: str):
    a, b = a.lower(), b.lower()
    a_count = Counter(a)
    b_count = Counter(b)
    return a_count == b_count


def is_anagram(a: str, b: str):
    a, b = a.lower().strip(), b.lower().strip()
    a, b = selection_sort([s for s in a]), selection_sort([s for s in b])
    return a == b


# print(is_anagram("yeh", "Hey"))
# print(is_anagram_with_counter("test", "ett"))
