"""

n = int(input())
tou = []
k = list(map(int, input().split()))[:n]
w = tuple(k)
print(hash(w))

How to input multiple values from user in tuple in python"""
m = str(input())
for i in range(0,len(m),1):
    if m[i] == ' ':
        m = m.replace(m[i], '-')
print(m)
