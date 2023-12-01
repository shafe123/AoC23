from utilities import read_file

def replace_digits(line: str) -> str:
    result = ""
    digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    while line != "":
        if line[0].isnumeric():
            result += line[0]
        else:
            for digit, value in digits.items():
                if line[:len(digit)] == digit:
                    result += str(value)
        line = line[1:]

    return result


def calculate_line(line: str) -> int:
    line_total = 0
    for char in line:
        if char.isnumeric():
            line_total += 10 * int(char)
            break
    for char in line[::-1]:
        if char.isnumeric():
            line_total += int(char)
            break
    return line_total

def day1_part2(input_file: str="day1_sample.txt") -> int:
    lines: list[str] = read_file(input_file)
    total_sum = 0
    vals = []

    for line in lines:
        line = replace_digits(line)
        line_total = calculate_line(line)
        vals.append(line_total)
        
    total_sum = sum(vals)
    return total_sum

print(day1_part2())