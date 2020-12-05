with open("day4.txt") as f:
    lines = f.read().splitlines()

passport = list()
a = list()

count = 0
c = 0
c7 = 0


for line in lines:
    if(line != ""):
        a = line.split(" ")
        for i in a:
            passport.append(i)
    if(line == ""):
        if(len(passport) == 8):
            count += 1
        elif(len(passport) == 7):
            c7 += 1
            for i in passport:
                if "cid:" in i:
                    print(i, c)
                    c += 1

        passport = list()

count = count + (c7-c)

print(count)


passport = list()
a = list()

count = 0
c = 0
c7 = 0


for line in lines:
    if(line != ""):
        a = line.split(" ")

        for i in a:
            passport.append(i)
    if(line == ""):
        if(len(passport) == 8):
            
            count += 1
        elif(len(passport) == 7):
            c7 += 1
            for i in passport:
                if "cid:" in i:
                    print(i, c)
                    c += 1

        passport = list()

count = count + (c7-c)

print(count)
