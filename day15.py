with open("day15_t.txt") as f:
    lines = f.read()

numbers = lines.split(",")
#print(numbers)

num2count = {}
i = 1

while i < 5:
    if(numbers[i-1] in num2count):
        print(num2count[numbers[i-1]])
        a = i - num2count[numbers[i-1]]
        print(a)
        numbers.append(num2count[numbers[i]])
    else:
        num2count[numbers[i]] = i
        numbers.append(num2count[numbers[i]])

    i += 1



print(numbers)

#add one to every key in dict that is not i