def solution(N):
    # Implement your solution here
    if N % 2 == 0:
        for i in range(N):
            k = N - i
            if N % (2**k) == 0:
                return k
            i = i + 1


if __name__ == "__main__":
    c = solution(24)
    print(c)
