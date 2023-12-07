import os
import sys
sys. setrecursionlimit(100000)
pohyby = {
    '^': (-1,0),
    'V': (1,0),
    '<': (0,-1),
    '>': (0,1)
}
def preloz_radku(line):
    radka = []
    for znak in line:
        if znak == 'S':
            radka.append(ord('a'))  
        elif znak == 'E':
            radka.append(ord('z'))
        else:
            radka.append(ord(znak))
    return radka
def init_navstivenou_mapu(mapa):
    mapa_navstivena = []
    for _ in mapa:
        mapa_navstivena.append([])
        for _ in mapa[0]:
            mapa_navstivena[-1].append(len(mapa)*len(mapa[0]))
    return mapa_navstivena
def chci_sem_jit(mapa,mapa_navstivena,pozice,delka,vyska):
    #Mimo mapu
    if pozice[0] < 0 or pozice[1] < 0 or pozice[0] >=len(mapa_navstivena) or pozice[1] >= len(mapa_navstivena[0]):
        return False
    #Dostal jsem se sem uz i kratsi cestou
    if mapa_navstivena[pozice[0]][pozice[1]] <= delka:
        return False
    #Je to uz konec!
    #if (mapa[pozice[0]][pozice[1]] == 'E' and vyska in [ord('y'),ord('z')]) or mapa[pozice[0]][pozice[1]] == 'S' or not vyska or chr(vyska) == 'S':
    if (mapa[pozice[0]][pozice[1]] == ord('a') and vyska in [ord('a'),ord('b')]) or not vyska:
        return True
    #Je to maximalne o jeden vyssi?
    #if not vyska or mapa[pozice[0]][pozice[1]] in range(vyska+2):
    if not vyska or vyska in range(mapa[pozice[0]][pozice[1]]+2):
        return True
    return False
def tiskni_mapu(mapa_navstivena):
    for line in mapa_navstivena:
        for znak in line:
            print(chr(znak),end='')
        print('')
    print()
def projdi_mapu(mapa,mapa_navstivena,pozice,delka,vyska):
    if not chci_sem_jit(mapa, mapa_navstivena, pozice, delka, vyska):
        return None
    #Kdyz je konec, tak se vracim
    if mapa[pozice[0]][pozice[1]] == ord('a'):
        return [delka,[pozice]]
    mapa_navstivena[pozice[0]][pozice[1]] = delka
    vyska = mapa[pozice[0]][pozice[1]]
    #if delka > 14:
    #tiskni_mapu(mapa_navstivena)
    
    
    best_delka = None
    for pohyb,smer in pohyby.items():
        nova_pozice = [pozice[0]+smer[0],pozice[1]+smer[1]]
        delka_kandidat = projdi_mapu(mapa,mapa_navstivena,nova_pozice,delka+1,vyska)
        if delka_kandidat and (not best_delka or best_delka[0] > delka_kandidat[0]):
            best_delka = delka_kandidat
    if best_delka:
        return [best_delka[0],best_delka[1]+[pozice]]
    else:
        return None
def visualize_walk(mapa,path):
    for step in path:
        tiskni_mapu(mapa)
        mapa[step[0]][step[1]] = ord(' ')
def main():
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    mapa = []
    start_pozice = [0,None]
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line == '#':
                break
            mapa.append(preloz_radku(line))
            if line.find('E') >= 0:
                start_pozice[1] = line.find('E')
                
                
            if start_pozice[1] is None:
                start_pozice[0] +=1
                
            
    a = 1
    mapa_navstivena = init_navstivenou_mapu(mapa)
    
    vysledek = projdi_mapu(mapa,mapa_navstivena,start_pozice,1,None)
    visualize_walk(mapa,vysledek[1])
    print(vysledek[0] - 1)
    #245 is too low
    
if __name__ == '__main__':
    main()