import re
import itertools

def getChecksum(rows):
    return 0

def test1():
    """
    5 1 9 5
    7 5 3
    2 4 6 8
    """

def getInput():
    lines = [re.findall('[0-9]+', line) for line in open("day2_input.txt")]
    lines = [[int(item) for item in line] for line in lines]
    return lines

def getInput2():
    lines = [re.findall('[0-9]+', line) for line in open("day2_input.txt")]
    lines = [[int(item) for item in line] for line in lines]
    return lines

def getMin(line):
    min = line[0]
    for item in line:
        if item < min:
            min = item
    return min

def getMax(line):
    max = line[0]
    for item in line:
        if item > max:
            max = item
    return max


def line_sum(line):
    for i in range(0, len(line) - 1):
        for item in line:
            if check_2(line[i], item):
                idiv = max_div(line[i], item)
                print("Found {} using {} {}".format(idiv, line[i], item))
                if idiv != 1:
                    return idiv
                else:
                    continue

def max_div(a,b ):
    if a > b:
        return a//b
    else:
        return b//a

def  check_2(a, b):
    if a == 0:
        return False
    elif b == 0:
        return False
    elif (a/b).is_integer():
        return True
    elif (b/a).is_integer():
        return True
    else:
        return False


def main():
    test = getInput()
    checksum = 0
    for line in test:
        min = getMin(line)
        max = getMax(line)
        print("Min {} max {}".format(min, max))
        checksum += max - min
    # Answer should be 36174
    print("Part one checksum is {}".format(checksum))
    checksum2 = 0

    test2 = getInput2()
    for line in test2:
        print("Looking at {}".format(line))
        checksum2 += int(line_sum(line))
    # Answer should be 244
    print("Part two checksum is {}".format(checksum2))

if __name__ == "__main__":
    main()