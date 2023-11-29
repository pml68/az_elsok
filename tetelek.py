"""
A modul az alábbi programozási tételek implementációját tartalmazza:
- megszámlálás tétele
- összegzés tétele
- maximumkiválasztás tétele
- minimumkiválasztás tétele
- eldöntés tétele
- kiválogatás tétele
- lineáris keresés tétele
"""
# megszámlálás tétele - függvény
def megszamlalas(M, T):
    property = f'M[i]{T}'
    sum = 0;
    for i in range(len(M)):
        if(eval(property)):
            sum += 1
        else:
            continue

    return sum

# összegzés tétele - függvény
def osszegzes(T):
    sum = 0
    for i in T:
        sum += i

    return sum

# maximumkiválasztás tétele - függvény
def maxkivalaszt(T):
    temp = 0
    for i in T:
        for j in T:
            if j>i and j>temp:
                temp = j
    return temp

# minimum kiválasztás tétele - függvény
def minkivalaszt(T):
    temp = 0;
    for i in T:
        for j in T:
            if j<i and j<temp:
                temp = j
    return temp

# eldöntés tétele - függvény
def eldontes(M, T):
    property = f'M[i]{T}'
    alap = False
    for i in range(len(M)):
        if(eval(property)):
            alap = True
        else:
            continue

    return alap

# kiválogatás tétele - függvény
def kivalogat(M, T):
    property = f'M[i]{T}'
    val = list()
    for i in range(len(M)):
        if(eval(property)):
            val.append(M[i])
        else:
            continue

    return val
  

# lineáris keresés tétele - függvény
def keres(M, T):
    """
    Adott egy n elemű M sorozat és egy T tulajdonság.
    Megkeressük az első olyan elemét M-nek, amely rendelkezik a T tulajdonsággal,
    és megadjuk, hogy hányadik!
    A függvény visszatérési értéke adja meg ezt!
    """
    property = f'M[i]{T}'
    
    for i in range(len(M)):
        if(eval(property)):
            return i        
        else:
            continue
