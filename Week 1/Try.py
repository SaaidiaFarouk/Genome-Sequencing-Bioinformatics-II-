import os 
os.remove("answear.txt")
def deBruijn(k, text):

    k = k - 1

    adj = {}

    for i in range(len(text) - k + 1):

        kmer = text[i: i + k]

        if kmer not in adj: adj[kmer] = []

        patt = text[i + 1: i + k + 1]

 

        if len(patt) == k:

            adj[kmer].append(patt)

        else: del adj[kmer]

 

    adj = dict(sorted(adj.items()))

    formattedTxt = ""

    for key in adj:

        formattedTxt += key + ": " + " ".join(adj[key]) + "\n"

    return formattedTxt
###
f=open("dataset.txt",'r')
text=f.read()
d=open('answear.txt','a')
k=12
d.write(deBruijn(k,text))

f.close()
d.close()

