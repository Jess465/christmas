import re

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
            #print(passport)
            for i in passport:
                if "cid:" in i:
                    #print(i, c)
                    #print(passport)
                    c7 -= 1

        passport = list()

count = count + c7

#print(count)



#Exercise 2
with open("day4.txt") as f:
    lines = f.read().splitlines()

passport = list()
a = list()
dict = {}

count = 0
c = 0
c7 = 0

for line in lines:
    if(line != ""):
        a = line.split(" ")
        for i in a:
            passport.append(i)
    if(line == ""):
        if(len(passport) == 8 or len(passport) == 7):
            for i in passport:
                a = i.split(":")
                dict[a[0]] = a[1]

            #keys = dict.keys()
            if("byr" in dict and len(dict["byr"]) == 4 and int(dict["byr"]) >= 1920 and int(dict["byr"]) <= 2002):
                if("iyr" in dict and len(dict["iyr"]) == 4 and int(dict["iyr"]) >= 2010 and int(dict["iyr"]) <= 2020):
                    if("eyr" in dict and len(dict["eyr"]) == 4 and int(dict["eyr"]) >= 2020 and int(dict["eyr"]) <= 2030):
                        if("hgt" in dict and "in" in dict["hgt"]):
                            dict["hgt"] = dict["hgt"].replace("in", "")
                            if(int(dict["hgt"]) >= 59 and int(dict["hgt"]) <= 76):
                                if("hcl" in dict and len(dict["hcl"]) == 7 and "#" in dict["hcl"]):
                                    #print(dict["hcl"])
                                    if("ecl" in dict and bool(dict["ecl"] == "amb") ^ bool(dict["ecl"] == "blu") ^ bool(dict["ecl"] == "brn") ^ bool(dict["ecl"] == "gry") ^ bool(dict["ecl"] == "grn") ^ bool(dict["ecl"] == "hzl") ^ bool(dict["ecl"] == "oth")):
                                        #print(dict["ecl"])
                                        if("pid" in dict and len(dict["pid"]) == 9 and re.search("^0", dict["pid"])):
                                            # p = re.search("^0", dict["pid"])
                                            # print(p)
                                            print(dict["pid"])
                                            count += 1

                        elif("hgt" in dict and "cm" in dict["hgt"]):
                            dict["hgt"] = dict["hgt"].replace("cm", "")
                            if("hgt" in dict and int(dict["hgt"]) >= 150 and int(dict["hgt"]) <= 193):
                                if("hcl" in dict and len(dict["hcl"]) == 7 and "#" in dict["hcl"]):
                                    #print(dict["hcl"])
                                    if("ecl" in dict and bool(dict["ecl"] == "amb") ^ bool(dict["ecl"] == "blu") ^ bool(dict["ecl"] == "brn") ^ bool(dict["ecl"] == "gry") ^ bool(dict["ecl"] == "grn") ^ bool(dict["ecl"] == "hzl") ^ bool(dict["ecl"] == "oth")):
                                        #print(dict["ecl"])
                                        if("pid" in dict and len(dict["pid"]) == 9 and re.search("^0", dict["pid"])):
                                            # p = re.search("^0", dict["pid"])
                                            # print(p)
                                            #print(dict["pid"])
                                            count += 1



        passport = list()
        dict = {}

print(count)
