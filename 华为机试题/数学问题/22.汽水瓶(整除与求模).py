from operator import mod
import sys

for line in sys.stdin:
    emp_coke = int(line)
    if emp_coke == 0:
        break
    if emp_coke==1:
        print(0)
    have_drinked = 0
    while emp_coke>1:
        if emp_coke <=3:
            have_drinked+=1
            break
        else:
            drink = emp_coke//3
            rst = emp_coke%3
            have_drinked += drink
            emp_coke = drink+rst

    print(have_drinked)