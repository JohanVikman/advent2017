"""--- Day 6: Memory Reallocation ---
A debugger program here is having an issue: it is trying to repair a memory reallocation routine, but it keeps getting
stuck in an infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold any number of blocks. The goal of the
reallocation routine is to balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks (ties won by
the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this, it removes all of the
blocks from the selected bank, then moves to the next (by index) memory bank and inserts one of the blocks. It continues
 doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is produced
that has been seen before.

For example, imagine a scenario with only four memory banks:

The banks start with 0, 2, 7, and 0 blocks. The third bank has the most blocks, so it is chosen for redistribution.
Starting with the next bank (the fourth bank) and then continuing to the first bank, the second bank, and so on, the 7
blocks are spread out over the memory banks. The fourth, first, and second banks get two blocks each, and the third bank
 gets one back. The final result looks like this: 2 4 1 2.
Next, the second bank is chosen because it contains the most blocks (four). Because there are four memory banks, each
gets one block. The result is: 3 1 2 3.
Now, there is a tie between the first and fourth memory banks, both of which have three blocks. The first bank wins the
tie, and its three blocks are distributed evenly over the other three banks, leaving it with none: 0 2 3 4.
The fourth bank is chosen, and its four blocks are distributed such that each of the four banks receives one: 1 3 4 1.
The third bank is chosen, and the same thing happens: 2 4 1 2.
At this point, we've reached a state we've seen before: 2 4 1 2 was already seen. The infinite loop is detected after
the fifth block redistribution cycle, and so the answer in this example is 5.

Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a
configuration is produced that has been seen before?
"""

def get_banks():
    banks = []
    for line in open("day6_input.txt"):
        banks = [int(elem) for elem in line.split()]
    return banks

def first_part():
    bank_dict = {}
    iterations = 0
    banks = get_banks()
    try:
        while True:
            print(f"banks is {banks}")
            most_block_bank = 0
            max = banks[0]
            i = 0
            for item in banks:
                if item > max:
                    most_block_bank = i
                    max = item
                i += 1
            print(f"Bank {most_block_bank} is our candidate with {max} blocks")
            print(f"Redistributing {max % 16} blocks")
            banks[most_block_bank] = 0
            while max > 0:
                banks[(most_block_bank + 1)%len(banks)] += 1
                most_block_bank += 1
                max -= 1
            print(f"New banks {banks}")
            string_banks = " ".join([str(item) for item in banks])
            iterations += 1
            if bank_dict.get(string_banks):
                last_time = bank_dict.get(string_banks)
                print(f"Finishing up at {iterations}")
                print(f"The loop was {iterations - last_time} big")
                raise Exception("Finished!")
            else:
                print(f"Saving new string_banks {string_banks}")
                bank_dict[string_banks] = iterations
    except Exception as e:
        print(f"Caught exception {e}")

def second_part():
    """--- Part Two ---
    Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1.
    Otherwise, increase it by 1 as before.

    Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit
    are left as 2 3 2 3 -1.

    How many steps does it now take to reach the exit?
    """
    instructions = get_instructions()
    index = 0
    steps_taken = 0
    number_of_instructions = len(instructions)
    try:
        while 0 <= index <= number_of_instructions:
            next_index = instructions[index]
            if next_index >= 3:
                instructions[index] = (next_index - 1)
            else:
                instructions[index] = (next_index + 1)
            index += next_index
            steps_taken += 1
        steps_taken -= 1
    except IndexError as ie:
        print("Caught index exception {}".format(ie))
    print(f"Steps taken {steps_taken} {index}")




if __name__ == "__main__":
    first_part()