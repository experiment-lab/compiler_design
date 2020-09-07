import re
string = input("Enter sentence : ") 
pattern = re.compile('\w+')
cnt = 0
s = pattern.findall(string)

for i in s :
    cnt+=1
print(cnt)
