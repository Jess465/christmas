with open("day1_1.txt") as f:
    lines = f.read().splitlines()

for num1 in lines:
    for num2 in lines:
        for num3 in lines:
            num1 = int(num1)
            num2 = int(num2)
            num3 = int(num3)
            sum = num1 + num2 + num3
            if sum == 2020:
                print(num1 + num2 + num3)
                print(num1 * num2 * num3)
