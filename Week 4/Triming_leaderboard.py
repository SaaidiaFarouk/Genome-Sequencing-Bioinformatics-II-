def linearspectrum(peptid,aas,aasmass):
    prefixmass=list()
    prefixmass.append(0)
    for i in range(0,len(peptid)):
        for aa in aas:
            if aa == peptid[i]:
                p=aas.index(aa)
                somme=prefixmass[i]+int(aasmass[p])
                prefixmass.append(somme)
    linearspectrum=list()
    linearspectrum.append(0)
    for i in range(0,len(peptid)+1):
        for j in range(i+1,len(peptid)+1):
            somm=prefixmass[j]-prefixmass[i]
            linearspectrum.append(somm)
    linearspectrum.sort()
    for i in range(len(linearspectrum)):
        linearspectrum[i]=str(linearspectrum[i])
    return linearspectrum


def cyclicscore(spectrum1,experimentalspectrum):
    score=0
    for element in experimentalspectrum:
        if element in spectrum1:
            score+=1
            spectrum1.remove(element)
    return score


def Trim(leaderboard,experimentalspectrum,n,aas,aasmass):
    linearscores=list()
    for i in range(len(leaderboard)):
        peptid=leaderboard[i]
        linearspect=linearspectrum(peptid,aas,aasmass)
        score=cyclicscore(linearspect,experimentalspectrum)
        linearscores.append(score)
    linearscores, leaderboard = (list(t) for t in zip(*sorted(zip(linearscores, leaderboard))))
    leaderboard.reverse()
    linearscores.reverse()
    auxleaderboard=leaderboard.copy()
    for i in range(n+1,len(leaderboard)):
        if linearscores[i]<linearscores[n]:
            for j in range(i-1,len(leaderboard)):
                auxleaderboard.pop()
            return auxleaderboard
    return auxleaderboard   
                



with open("dataset.txt","r") as f : 
    lst=f.readlines()
    for i in range(len(lst)):
        lst[i]=lst[i].replace("\n","")
    leaderboard=lst[0].split(" ")
    experimentalspectrum=lst[1].split(" ")
    n=int(lst[2])


aas=list()
aasmass=list()
with open("Mass.txt","r") as v :
    lst=v.readlines()
    for line in lst:
        line=line.replace("\n","")
        lst1=line.split(" ")
        aas.append(lst1[0])
        aasmass.append(lst1[1])
    
ans=Trim(leaderboard,experimentalspectrum,n,aas,aasmass)
print(ans)
with open("answear.txt","w") as d:
    for a in ans:
        d.write(a+" ")