# An array A consisting of N integers is given. Rotation of the array means that each element is
#  shifted right by one index, and the last element of the array is moved to the first place.
# For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
# (elements are shifted right by one index and 6 is moved to the first place).
# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

A = [3, 8, 9, -7, 6]


def rotate_array(input_array: list[int], times: int) -> list[int]:
    if (len(input_array) == 1) or (times == 0):
        print(input_array)
        return input_array
    tt_list = []
    while times != 0:
        temp = []
        if len(tt_list) == 0:
            tt_list = input_array.copy()
        n = 0

        for i in range(-1, len(tt_list) - 1, 1):
            temp.insert(n, tt_list[i])
            n = n + 1
        times = times - 1
        tt_list = temp.copy()
        temp = []
        print(tt_list)
        n = 0
    return tt_list


rotate_array(A, 15)
# # print(len(A) - 2)
# for i in range(len(A) - 1):

#     print(i)
