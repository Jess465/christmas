with open("day7.txt") as f:
    lines = f.read().splitlines()

count = 0
innerbags = list()
outerbags = list()

for row in lines:
    words = row.split(" ")
    bags = row.split(",")
    #print(bags[0])
    bag = words[0] + " " + words[1]
    # print(bag)
    for i in bags:
        if("shiny gold" in i and not "shiny gold bags contain" in row):
            count += 1
            innerbags.append(bag)

for innerbag in innerbags:
    for row in lines:
        words = row.split(" ")
        bags = row.split(",")
        #print(bags[0])
        bag = words[0] + " " + words[1]
        # print(bag)
        for j in bags:
            if(innerbag in j and bag not in innerbags):
                #print(innerbag, "in", bag)
                outerbags.append(bag)
                innerbags.append(bag)
                count += 1



print(count)

# Exercise 2
with open("day7_t2.txt") as f:
    lines = f.read().splitlines()

for row in lines:
    words = row.split(" ")
    bags = row.split(",")
    #print(bags[0])
    bag = words[0] + " " + words[1]
    # print(bag)
    for i in bags:
        if("shiny gold bags contain" in row):
            if("shiny gold bags contain" in i):
                gold, other = i.split("contain ")
                print(other)
                words = other.split(" ")
                bag = words[1] + " " + words[2]
                num = words[0]
                print(bag)
                innerbags.append(bag)
