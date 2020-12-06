import re

PassportRequirements = [
    ("byr", lambda x: 1920 <= int(x) <= 2002),
    ("iyr", lambda x: 2010 <= int(x) <= 2020),
    ("eyr", lambda x: 2020 <= int(x) <= 2030),
    ("hgt", lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76)),
    ("hcl", lambda x: re.fullmatch(r"#[0-9a-f]{6}", x)),
    ("ecl", lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
    ("pid", lambda x: re.fullmatch(r"[0-9]{9}", x)),
]

part1 = 0
part2 = 0


for i in open("day4.input", "r").read().split('\n\n'):
    i = i.split('\n')
    i = " ".join(i)
    temp = (dict((x.strip(), y.strip())
        for x, y in (element.split(':')
            for element in i.split(' '))))

    valid1 = valid2 = True

    for key, val in PassportRequirements:
        if key not in temp:
            valid1 = False
            break
        if not val(temp[key]):
            valid2 = False
    if valid1:
        part1 += 1
        part2 += valid2

print(part1)
print(part2)

