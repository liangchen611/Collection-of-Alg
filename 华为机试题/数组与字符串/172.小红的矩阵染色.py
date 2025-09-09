import sys

nmk = sys.stdin.readline().strip().split()
nmk = [int(NMK) for NMK in nmk]
n,m,k=nmk[0],nmk[1],nmk[2]

M = [[""]*nmk[1] for _ in range(0,nmk[0])]

for i in range(0,n):
    line = sys.stdin.readline().strip()
    for j in range(0,m):
        M[i][j] = line[j]

blank = []

for j in range(0,m):
    count = -1
    column_blank = []
    # 遍历全部黑色位置，作差，记录所有长度在2以上的空白格
    for i in range(0,n):
        # 黑色开头
        if M[i][j]=="*" and count==-1:
            count=i
            if i==0:continue
            if i!=0 and i>1:
                column_blank.append(i)

        # 非开头
        if M[i][j]=="*" and count!=-1:
            if i-count-1>1:
                column_blank.append(i-count-1)
            count=i

    # 最后一个黑色不是末尾
    if count<n-1 and count!=-1:
        if n-1-count>=2:
            column_blank.append(n-1-count)
    
    # 整列全部为空白
    if count==-1:column_blank.append(n)

    if len(column_blank)!=0:
        blank.append(column_blank)

# 计算能得到的最大分数
max_score = 0
if len(blank)==0:
    print(0)
    sys.exit()
if len(blank)!=0:
    blank = [item for sublist in blank for item in sublist]
    blank.sort(reverse=True)
    BL = 0
    while k>=2:
        if BL>=len(blank):break
        if blank[BL]>=k:
            max_score+=k-1
            k-=blank[BL]
        if blank[BL]<k:
            max_score+=blank[BL]-1
            k-=blank[BL]
        BL+=1
    print(max_score)

