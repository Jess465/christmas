with open("day8_t.txt") as f:
    lines = f.read().splitlines()

acc = 0

for row in lines:
    if("acc" in row):
        a, num = row.split(" ")
        if("+" in num):
            num = num.replace("+", "")
            acc += int(num)
        elif("-" in num):
            num = int(num.replace("-", ""))
            acc -= num
    elif("nop" in row):
        pass

print(acc)
