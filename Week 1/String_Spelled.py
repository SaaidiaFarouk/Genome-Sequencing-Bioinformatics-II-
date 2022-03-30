def String_Spelled(list):
    string=''
    k=len(list[0])
    string=string+list[0]
    for i in range(1,len(list)):
        string=string+list[i][k-1]
    return(string)
f=open("dataset.txt","r")
str=f.read()
list=str.split(' ')
print(String_Spelled(list))