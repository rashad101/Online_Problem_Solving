
n= "00000000000000000000000000001011"

count = 0
for i in range(len(n)):
    if n[i]=="1":
        count+=1

print(count)