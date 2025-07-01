import sys

T = int(input())
for i in range(0,T):
    S = sys.stdin.readline().strip()
    S_dict = {}
    for j in range(0,len(S)):
        S_dict[S[j]] = S_dict.setdefault(S[j],0)+1
    S_by_value = sorted(S_dict.items(),key=lambda x:x[1])[::-1]
    #S_list = sorted(S_dict,key=dict.items())
    charm = 26
    CHARM = 0
    for k in range(0,len(S_by_value)):
        CHARM += charm*S_by_value[k][1]
        charm -= 1
    print(CHARM)
    
#sorted排序(排序的依据，排序的函数：lambda简易函数)
# d = {'a': 3, 'b': 1, 'c': 2}
# sorted_items = sorted(d.items(), key=lambda x: x[1])