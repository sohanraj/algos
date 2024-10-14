# A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

# For example, in array A such that:

#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the elements at indexes 0 and 2 have value 9,
# the elements at indexes 1 and 3 have value 3,
# the elements at indexes 4 and 6 have value 9,
# the element at index 5 has value 7 and is unpaired.

array = [9, 3, 9, 3, 9, 7, 9]


# time complaxity O(N**2)
def odd_in_array(array: list) -> int:
    element_count = []
    if len(array) % 2 != 0:
        for val in array:
            if val in element_count:
                element_count.remove(val)
            else:
                element_count.append(val)
        if len(element_count) == 1:
            return element_count[0]


# time complaxity O(N)
def odd_in_array2(array: list) -> int:
    result = 0
    for val in array:
        result ^= val
        print(result)
    return result


print(odd_in_array2(array))
