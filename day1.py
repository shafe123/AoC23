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



lines: list[str] = read_file("day1.txt")
total_sum = 0
vals = []
digits = { "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
for line in lines:
    line = replace_digits(line)
    print(line)
    indices = []
    line_total = 0
    for char in line:
        if char.isnumeric():
            line_total += 10 * int(char)
            break
    for char in line[::-1]:
        if char.isnumeric():
            line_total += int(char)
            break
    vals.append(line_total)
    
total_sum = sum(vals)
print(total_sum)