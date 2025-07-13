import sys

cards = sys.stdin.readline().strip().split(" ")

pts=[]
for i in range(len(cards)):
    if cards[i]=="A":pts.append(1)
    if cards[i]=="J":pts.append(11)
    if cards[i]=="Q":pts.append(12)
    if cards[i]=="K":pts.append(13)
    if cards[i] not in ["A","J","Q","K","joker","JOKER"]:
        pts.append(int(cards[i]))

ops = []

def cal(k,n1,n2):
    if k==0:return n1+n2
    if k==1:return n1*n2
    if k==2:return n1-n2
    if k==3:
        if abs(n2)<1e-6:return None
        else: return n1/n2

def enum(nums,op,start):
    if start == len(nums):
        for i in range(0,4):
            for j in range(0,4):
                for k in range(0,4):
                    a = nums[0]
                    b = cal(i,a,nums[1])
                    if b==None:continue

                    c = cal(j,b,nums[2])
                    if c==None:continue

                    d = cal(k,c,nums[3])
                    if d==None:continue
                    elif abs(d-24)<1e-6:
                        op.append(i)
                        op.append(j)
                        op.append(k)
                        return True
        return False

    for s in range(start, len(nums)):
        nums[start], nums[s] = nums[s], nums[start]
        if enum(nums,op,start + 1):
            return True
        nums[start], nums[s] = nums[s], nums[start]
    return False


if "joker" in cards or "JOKER" in cards:
    print("ERROR")
else:
    print(enum(pts,ops))
    