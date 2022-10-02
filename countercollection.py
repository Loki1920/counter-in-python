# Counter 
from collections import Counter
l = [4, 6, 5, 3, 3, 1]

arr = Counter(l)

print(arr)

for i in range(5):
    print(arr[i],arr[i+1])
