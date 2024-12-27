import sys

string = input()
record = {}

for i in range(0,len(string)):
    char = string[i]
    if char in record:
        continue
    else:
        record[char]=1

print(len(record))