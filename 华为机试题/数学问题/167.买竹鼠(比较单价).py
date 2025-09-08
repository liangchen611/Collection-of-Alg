import sys

abx = sys.stdin.readline().strip().split()
a,b,x = int(abx[0]),int(abx[1]),int(abx[2])

singleb = b/3

AB = 1 if singleb<a else 0
less_cost = 0

if AB==0:
    less_cost = x*a
if AB==1:
    mod = x%3
    B = x//3
    if mod*a<b:
        less_cost = B*b + mod*a
    elif mod*a>=b:
        less_cost = (B+1)*b

print(less_cost)

#——————————
#1.比较二者的单价，哪个更便宜，就尽量用对应的方案买
#当某一方案的数量不能和买的数量凑够整数时，考虑：剩下的是用另一方案补齐，还是再买一组当前的方案，比较价格