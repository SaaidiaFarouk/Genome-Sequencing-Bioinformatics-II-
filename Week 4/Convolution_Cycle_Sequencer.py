def linearspectrum(peptid):
    prefixmass=list()
    prefixmass.append(0)
    for i in range(0,len(peptid)):
        for j in range(57,201):
            if int(peptid[i]) == j:
                somme=prefixmass[i]+j
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

def Trim(leaderboard,experimentalspectrum,n):
    if len(leaderboard)==0:
        return leaderboard
    auxleaderboard=list()
    linearscores=list()
    for i in range(len(leaderboard)):
        peptid=leaderboard[i]
        linearspect=linearspectrum(peptid)
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

def maxs(peptid):
    weight=0
    for pep in peptid:
        weight+=int(pep)
    return weight

def cyclicscore(spectrum,experimentalspectrum):
    score=0
    spectrum1=spectrum.copy()
    for element in experimentalspectrum:
        if element in spectrum1:
            score+=1
            spectrum1.remove(element)
    return score

def cyclicspectrum(peptid):
    prefixmass=list()
    prefixmass.append(0)
    for i in range(0,len(peptid)):
        for j in range(57,201):
            if int(peptid[i]) == j:
                somme=prefixmass[i]+j
                prefixmass.append(somme)
    peptidmass=prefixmass[len(prefixmass)-1]
    cyclicspectrum=list()
    cyclicspectrum.append(0)
    for i in range(0,len(peptid)):
        for j in range(i+1,len(peptid)+1):
            somm=prefixmass[j]-prefixmass[i]
            cyclicspectrum.append(somm)
            if i>0 and j<len(peptid):
                somm=peptidmass-somm
                cyclicspectrum.append(somm)
    cyclicspectrum.sort()
    for i in range(len(cyclicspectrum)):
        cyclicspectrum[i]=str(cyclicspectrum[i])
    return cyclicspectrum

def compositionfinder(spectrum,m):
    composition=list()
    part=0
    for element in spectrum:
        for elemnt in spectrum:
            part=int(elemnt)-int(element)
            if part  > 0 :
                composition.append(str(part))
    composition.sort()
    components=composition.copy()
    l= len(components)-1
    i= 0
    repetitions=list()
    while i < l :
        if components[i] == components[i+1]:
            components.pop(i+1)
            l-=1
            i-=1
        if int(components[i]) not in range(57,201):
            components.pop(i)
            l-=1
            i-=1
        i+=1
    for element in components:
        repetitions.append(composition.count(element))
    repetitions, components = (list(t) for t in zip(*sorted(zip(repetitions, components))))
    repetitions.reverse()
    components.reverse()
    finalcomponents=list()
    for i in range(len(components)):
        if len(finalcomponents) < m:
            finalcomponents.append(components[i])
            rep=repetitions[i]
        elif len(finalcomponents) >= m :
            if rep == repetitions[i]:
                finalcomponents.append(components[i])
    return finalcomponents

def expandefromcomponents(candidatepeptids,components):
    newcandidatepeptids=list()
    for cpeptid in candidatepeptids:
        for i in range(len(components)):
            newcpeptid=cpeptid.copy()
            newcpeptid.append(components[i])
            newcandidatepeptids.append(newcpeptid)
    return newcandidatepeptids

def convolutionsequencer(experimentalspectrum,m,n):
    components=compositionfinder(experimentalspectrum,m)
    leaderboard=[[]]
    leaderpeptid=list()
    parentmass=0
    leaderpeptids=list()
    leaderscores=list()
    for mass in experimentalspectrum:
        if int(mass) > parentmass:
            parentmass=int(mass)
    while len(leaderboard)!=0:
        newleaderboard=expandefromcomponents(leaderboard,components)
        leaderboard=newleaderboard.copy()
        l=len(leaderboard)
        i=0
        while i < l :
            peptid=leaderboard[i]
            spectrum=cyclicspectrum(peptid)
            score=cyclicscore(spectrum,experimentalspectrum)
            leaderspectrum=cyclicspectrum(leaderpeptid)
            leaderscore=cyclicscore(leaderspectrum,experimentalspectrum)
            if maxs(peptid) == parentmass:
                if score >= leaderscore:
                    leaderscores.append(score)
                    leaderpeptids.append(peptid)
                    leaderpeptid=peptid
            elif maxs(peptid) > parentmass :
                leaderboard.remove(peptid)
                i-=1
                l-=1
            i+=1
        leaderboard=Trim(leaderboard,experimentalspectrum,n)
    l=len(leaderscores)
    i=0
    while i < l :
        if leaderscores[i]!=leaderscore:
            leaderpeptids.remove(leaderpeptids[i])
            leaderscores.remove(leaderscores[i])
            l-=1
            i-=1
        i+=1
    return leaderpeptids




with open("dataset.txt","r") as f : 
    lst=f.readlines()
    for i in range(len(lst)):
        lst[i]=lst[i].replace("\n","")
    m=int(lst[0])
    n=int(lst[1])
    experimentalspectrum=lst[2].split(" ")

ans=convolutionsequencer(experimentalspectrum,m,n)

with open("answear.txt","w") as d: 
    stri=''
    for b in ans : 
        stri=""
        for a in b :
            stri+=a+"-"
        sto=stri[:len(stri)-1]
        d.write(sto+" ")