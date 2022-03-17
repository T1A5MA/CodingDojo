# 1. 
from re import I


def biggieSize(x):
    for i in range(len(x)):
        if x[i] > 0:
            x[i] = "big"
    return x

print(biggieSize([-1, 3, 5, -5]))

# 2. 
def countPositives(x):
    count = 0
    for i in x:
        if i > 0:
            count+=1
    x[len(x)-1] = count
    return x

print(countPositives([-1, 1, 1, 1]))
print(countPositives([1, 6, -4, -2, -7, -2]))

# 3. 
def sumTotal(x):
    sum = 0
    for i in x:
        sum = sum + i
    return sum

print(sumTotal([1, 2, 3, 4]))
print(sumTotal([6, 3, -2]))

# 4.
def average(x):
    sum = 0
    length = 0
    for i in x:
        sum = sum + i
        length += 1
    return sum / length

print(average([1, 2, 3, 4]))

# 5.
def length(x):
    count = 0
    for i in x:
        count +=1
    return count

print(length([37, 2, 1 ,-9]))
print(length([]))

# 6. 
def minimum(x):
    count = 0
    for i in x:
        count +=1
    if count == 0:
        return False
    
    min = x[0]
    for i in x:
        if i < min:
            min = i
    return min

print(minimum([37, 2, 1 ,-9]))
print(minimum([]))

# 7.
def maximum(x):
    count = 0
    for i in x:
        count +=1
    if count == 0:
        return False
    
    max = x[0]
    for i in x:
        if i > max:
            max = i
    return max

print(maximum([37, 2, 1 ,-9]))
print(maximum([]))

# 8.
def ultimateAnalysis(x):
    return {
    "sumTotal" : sumTotal(x),
    "average" : average(x),
    "minimum" : minimum(x),
    "maximum" : maximum(x),
    "length" : length(x)
    }

print(ultimateAnalysis([37, 2, 1 ,-9]))

# 9.
def reverseList(x):
    return x[::-1]

print(reverseList([37, 2, 1 ,-9]))

def reverseList2(x):
    for i in range(len(x) // 2):
        x[i], x[- 1 - i] = x[- 1 - i], x[i]
    return x

print(reverseList2([37, 2, 1 ,-9]))
    
