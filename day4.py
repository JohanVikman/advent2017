"""--- Day 4: High-Entropy Passphrases ---
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password.
A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
"""


def first_part():
    valid = 0
    for line in open("day4_testa.txt"):
        lsplit = line.split()
        word_dict = {}
        try:
            for item in lsplit:
                if word_dict.get(item):
                    raise Exception("Found a duplicate")
                else:
                    word_dict[item] = True
        except:
            continue
        valid += 1
    print("valid passphrases are {}".format(valid))
    return valid


def second_part():
    valid = 0
    for line in open("day4_testa.txt"):
        lsplit = line.split()
        word_dict = {}
        try:
            for item in lsplit:
                item_list = list(item)
                item_list.sort()
                sorted_item = ''.join(item_list)
                if word_dict.get(sorted_item):
                    raise Exception("Found a duplicate")
                else:
                    word_dict[sorted_item] = True
        except Exception as e:
            continue
        valid += 1
    print("valid passphrases are {}".format(valid))
    return valid


if __name__ == "__main__":
    first_part()
    second_part()