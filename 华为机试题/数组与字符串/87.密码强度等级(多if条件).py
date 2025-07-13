import sys

pw = input().strip()
score = 0

if len(pw)<=4:score+=5
elif len(pw)<=7:score+=10
elif len(pw)>=8:score+=25

alpha = 0
num = 0
sign = 0

for i,p in enumerate(pw):
    if "A"<=p<="Z":
        if alpha == 2:alpha = 3
        if alpha == 3:continue
        else: alpha = 1
        
    if "a"<=p<="z":
        if alpha == 1:alpha = 3
        if alpha == 3:continue
        else: alpha = 2
    
    if "0"<=p<="9":
        if num==0: num=1
        elif num==1: num=2
    
    if 33<=ord(p)<=47 or 58<=ord(p)<=64 or 91<=ord(p)<=96 or 123<=ord(p)<=126:
        if sign==0: sign=1
        elif sign==1: sign=2

bonus = 0
if num>=1:
    if alpha==3 and sign>=1:bonus = 5
    elif 3>alpha>=1:
        if sign==0: bonus=2
        if sign>=1: bonus=3

if alpha==3:score+=20
if 0<alpha<3:score+=10

if num==2:score+=20
if num==1:score+=10

if sign==2:score+=25
if sign==1:score+=10

score+=bonus

if score>=90:print("VERY_SECURE")
elif score>=80:print("SECURE")
elif score>=70:print("VERY_STRONG")
elif score>=60:print("STRONG")
elif score>=50:print("AVERAGE")
elif score>=25:print("WEAK")
elif score>=0:print("VERY_WEAK")