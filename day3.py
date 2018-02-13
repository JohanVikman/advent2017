"""You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

Your puzzle input is 361527.
"""
import math

def main():
    n = 361527
    m = 1
    ring = 1
    while (m ** 2) < n:
        m += 2
        ring += 1
    print("Largest odd m is {} ring is {}".format(m, ring))
    ring_size = ring * 2 - 1
    start_n = ((m-2) ** 2) + 1
    print("Ring size is {} start_n is {}".format(ring_size, start_n))
    # Find which side the value is on
    # \ 1 /
    # 2 X 0
    # / 3 \
    dist = 0
    side_start = start_n
    side_mid = 0
    for i in range(0,4):
        side_max = side_start + ring_size - 2
        print("Checking if n is less than or equal to {}".format(side_max))
        if n <= side_max:
            side = i
            print("Hit on side {}".format(side))
            side_mid = (side_max + side_start) // 2
            dist = math.fabs(side_mid - n)
            print("Distance from {} to {} is {}".format(side_mid, n, dist))
            break

        side_start = side_max + 1
    print("side_mid {} side_start {}".format(side_mid, side_start))
    print("Side Dist is {}".format(dist))
    print("Dist is {}".format(dist + ring - 1))
    return dist + ring - 1

if __name__ == "__main__":
    main()

# 577 too high
# 276 too low