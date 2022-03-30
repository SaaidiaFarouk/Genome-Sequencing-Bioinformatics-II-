def compositiongraph(list1):
    k=len(list1[0])
    list2=list()
    for i in range(len(list1)-1):
        prefix=list1[i][0:k-1]
        suffix=list1[i][1:k]
        x=(prefix,suffix)
        list2.append(x)
        list2.sort()
    return list2

f=open("dataset.txt","r")
str=f.read()
list1=str.split(' ')
print(compositiongraph(list1))
f.close
