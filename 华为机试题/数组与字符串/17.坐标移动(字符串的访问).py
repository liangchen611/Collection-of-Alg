import sys

actions = input().split(";")
direction = {"W", "A", "S", "D"}
number = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
X = 0
Y = 0
for i in range(0, len(actions)):
    charlen = len(actions[i])
    if charlen == 0 or charlen == 1:
        continue
    if charlen > 3:
        continue
    if actions[i][0] in direction == False:
        continue
    if charlen <= 3:
        if actions[i][1] in number == False:
            continue
        if (charlen == 3) and (actions[i][2] not in number):
            continue

    if actions[i][0] == "W" and charlen == 2:
        Y += int(actions[i][1])
    if actions[i][0] == "W" and charlen == 3:
        Y += int(actions[i][1]) * 10 + int(actions[i][2])

    if actions[i][0] == "A" and charlen == 2:
        X -= int(actions[i][1])
    if actions[i][0] == "A" and charlen == 3:
        X -= int(actions[i][1]) * 10 + int(actions[i][2])

    if actions[i][0] == "S" and charlen == 2:
        Y -= int(actions[i][1])
    if actions[i][0] == "S" and charlen == 3:
        Y -= int(actions[i][1]) * 10 + int(actions[i][2])

    if actions[i][0] == "D" and charlen == 2:
        X += int(actions[i][1])
    if actions[i][0] == "D" and charlen == 3:
        X += int(actions[i][1]) * 10 + int(actions[i][2])

print(X, end=",")
print(Y)

# 字符串中的数字，数值类型仍为字符串
# 定义一个集合，用not in可以检测值是否处于集合中
# 对字符串本身，也能用[i]访问具体的字符
