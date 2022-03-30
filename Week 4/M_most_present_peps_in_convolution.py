def convolution(spectrum,m):
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

    

with open("dataset.txt","r") as f : 
    data=f.read()
    data=data.replace("\n","")
    spectrum=data.split( )

with open("answear.txt","w") as d :
    stro=''
    for part in convolution(spectrum,10):
        stro+=part+" "
    sti=stro[:len(stro)-1]
    d.write(sti)
