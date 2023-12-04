#!/usr/bin/env python3

import re

NUMS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def replace_nums(text):
    for word, num in NUMS.items():
        text = re.sub(word, str(num), text)
    return text

def main():
    file_path = 'input.txt'

    running_total = 0
    line_nums = []
    with open(file_path, 'r') as file:
        for line in file:

            replaced_line = replace_nums(line)
            # print(replaced_line)
            nums = []
            for char in replaced_line:
                if char.isdigit():
                    nums.append(char)
            line_nums.append(nums)

    for line in line_nums:
        first = line[0]
        last = line[-1]
        total = first + last
        # print(total)
        running_total += int(total)

    # print(line_nums)
    print(running_total)

if __name__ == "__main__":
    main()
