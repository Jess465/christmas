with open("day2_1.txt") as f:
    lines = f.read().splitlines()

sum = 0

#Exercise1
for line in lines:
    num, char, pwd = line.split()
    char = char.replace(":", "")
    pwd_char = list(pwd)
    count = 0
    for i in pwd_char:
        if(i == char):
            count += 1
    down, up = num.split("-")
    down = int(down)
    up = int(up)
    if(count >= down and count <= up):
        sum += 1
print(sum)

#Exercise2
sum = 0

for line in lines:
    num, char, pwd = line.split()
    char = char.replace(":", "")
    pwd_char = list(pwd)
    count = 0
    first, last = num.split("-")
    first = int(first)
    last = int(last)
    if(bool(pwd_char[first-1] == char)^ bool(pwd_char[last-1] == char)):
        sum += 1
print(sum)
