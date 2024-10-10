# Reverse the integer without using reverse method for integer even if negative.abs


def reverse_integer(n: int) -> int:

    # converting value to absolute value
    positive_int = abs(n)

    # setting up variable to store reverse numbers
    reverse_num = 0

    # loop starts
    while positive_int != 0:

        # extract last digit from the number
        digit = positive_int % 10

        # algorithm to add last digit
        reverse_num = reverse_num * 10 + digit

        # removing processed last digit
        positive_int = positive_int // 10

    # Handling negative sign here
    return -reverse_num if n < 0 else reverse_num


if __name__ == "__main__":
    num = -123456
    print(reverse_integer(num))
