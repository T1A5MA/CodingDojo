# 1. 
for i in range(151):
    print(i)

# 2. 
for i in range(5,1000, 5):
    print(i)

# 3.
for i in range(1, 100):
    if i % 5 != 0 and i % 10 != 0:
        print(i)

    elif i % 5 == 0 and i % 10 != 0:
        print("Coding")

    elif i % 10 == 0:
        print("Coding Dojo")

# 4.
sum = 0

for i in range(500000):
    if i % 2 != 0:
        sum = sum + i
print(sum)

# 5.
for i in range(2018, 0, -4):
    print(i)

# 6.
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)
