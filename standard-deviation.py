import math

n = int(input())
a = list(map(int, input().split(' ')))
mean = sum(a)/n

mu = sum(list(map(lambda i: (i-mean)**2, a)))
sd = math.sqrt(mu/n)
print(sd)
