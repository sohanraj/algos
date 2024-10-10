# A binary gap within a positive integer N is any maximal sequence of consecutive zeros
# that is surrounded by ones at both ends in the binary representation of N.
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
# The number 20 has binary representation 10100 and contains one binary gap of length 1.
# The number 15 has binary representation 1111 and has no binary gaps.
# The number 32 has binary representation 100000 and has no binary gaps

num = 529529  # 10000001010001111001


def max_bin_gap(n: int) -> int:
    # Convert number to binary string
    bin_num = format(n, "b")
    print(f"binary number of {n} is {bin_num}")

    # algorithm to find bin gap
    prev_one = 0
    gap_counter = 0
    gap_list = []
    for idx, val in enumerate(bin_num):
        if val == "1":
            prev_one = 1
        if prev_one == 1 and val == "0":
            gap_counter = gap_counter + 1
        if gap_counter > 0 and val == "1":
            gap_list.append(gap_counter)
            gap_counter = 0

    return max(gap_list) if len(gap_list) > 0 else 0


max_bin_gap(15)
