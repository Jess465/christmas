with open("day5_t.txt") as f:
    lines = f.read().splitlines()

nums = 1
numb = 127

for row in lines:
    nums = 1
    numb = 127
    for i in range(7):
        print(row[i])
        if(row[i] == "F" and i == 0):
            # numb = float(numb/2) - 0.5
            numb = (numb - nums)/2
            print(nums, numb)
        if(row[i] == "F" and i != 0):
            numb = (numb - nums)/2 + nums -0.5
            print(nums, numb)
        if(row[i] == "B" and i == 0):
            nums = (numb - nums)/2 + 1
            #numb = numb
            print(nums, numb)
        if(row[i] == "B"):
            nums = numb - ((numb-nums)/2)
            nums = round(nums)
            print(nums, numb)


print(nums, numb)
            
#manage if starts with B