#!/usr/bin/env python3

def main():
    file_path = 'input.txt'

    running_total = 0
    line_nums = []
    with open(file_path, 'r') as file:
        for line in file:
            nums = []
            for char in line:
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
