# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Your goal is to find that missing element.

A = [2, 3, 1, 4, 5]
B = []
C = [0]


def find_missing_value(A: list) -> int:
    if A:
        A.sort()
        a_sort = A.copy()
        # print(a_sort)
        if len(a_sort) > 0:
            for idx, val in enumerate(a_sort):
                if (idx > 0) and val != (a_sort[idx - 1] + 1):
                    return a_sort[idx - 1] + 1
        if a_sort[0] == 1:
            return max(a_sort) + 1
        return 1
    return 1


print(find_missing_value(B))
