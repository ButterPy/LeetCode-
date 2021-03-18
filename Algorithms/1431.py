candies =  [2,3,5,1,3]
extra = 3
answer = [bool]
maximum = max(candies)

#Output: [true,true,true,false,true] 

for i in candies:
    if i + extra >= maximum:
        answer.append(True)
    else:
        answer.append(False)
print(answer)
