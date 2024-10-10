def solution(N):
    # Implement your solution here
    # checks if  number is divisible by 2
    if N % 2 == 0:
        # loop starts
        for i in range(N):
            # variable start from hight possible value
            k = N - i
            # checks highest power to 2 is divisible
            if N % (2**k) == 0:
                return k
            i = i + 1


if __name__ == "__main__":
    c = solution(24)
    print(c)
