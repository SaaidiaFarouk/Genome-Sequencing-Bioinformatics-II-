def circularString(lastpoint):
    lastpointZero = lastpoint[1:k] + '0'
    if lastpointZero not in partString:
        partString.append(lastpointZero)
        totalString.append(0)
        circularString(lastpointZero)
    lastpointOne = lastpoint[1:k] + '1'
    if lastpointOne not in partString:
        partString.append(lastpointOne)
        totalString.append(1)
        circularString(lastpointOne)
    if len(partString)==2**k:
        return totalString
    else:
        totalString.pop()
 
print('k : ',end='')
k = 8
totalString = []
partString = []
partString.append(k*'0')
for i in range(k):
    totalString.append(0)
lastpoint = partString[0]
ans=format(k),circularString(lastpoint)
stri=''
for i in ans :
    stri=stri+str(i)
print(stri)