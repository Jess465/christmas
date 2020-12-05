with open("day3.txt") as f:
    lines = f.read().splitlines()

#Exercise 1
count = 0
tree = 0
i = 0


for line in lines:
    lines[i] = line*200
    if(lines[i][count] == "#"):
        tree += 1
        #print(i, count)
    i += 1
    count += 3

#Exercise 2
print("3,1:", tree)
multipl = tree

count = 0
tree = 0
i = 0

for line in lines:
    if(lines[i][count] == "#"):
        tree += 1
        #print(i, count)
    i += 1
    count += 1

print("1,1:",tree)
multipl *= tree
print(multipl)

count = 0
tree = 0
i = 0

for line in lines:
    if(lines[i][count] == "#"):
        tree += 1
        #print(i, count)
    i += 1
    count += 5

print("5,1:",tree)
multipl *= tree
print(multipl)

count = 0
tree = 0
i = 0

for line in lines:
    if(lines[i][count] == "#"):
        tree += 1
        #print(i, count)
    i += 1
    count += 7

print("7,1:",tree)
multipl *=tree
print(multipl)


count = 0
tree = 0
i = 0

for i in range(0,322,2):
    print(i, count)
    if(lines[i][count] == "#"):

        # if(i % 2 == 1):
        tree += 1

    #i += 2
    count += 1


print("1,2:",tree)
multipl *= (tree)

print(multipl)
