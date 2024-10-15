# A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

# Count the minimal number of jumps that the small frog must perform to reach its target.

# Write a function:


def frogjump(x: float, y: float, d: float) -> int:
    frequec: float = (y - x) / d if (y - x) % d == 0 else ((y - x) // d) + 1
    return int(frequec)


print(frogjump(10, 85.5, 30.4))
