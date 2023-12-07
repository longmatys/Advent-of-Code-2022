import os
import json
import logging
import math
import functools
def porovnej_pole(dvojice,indent=1):
    logging.debug(' '*indent + f"Porovnavam {dvojice}")
    try:
        navrat = None
        for (prvek_1,prvek_2) in zip(dvojice[0],dvojice[1],strict=True ):
            if type(prvek_1).__name__ == 'int':
                if type(prvek_2).__name__ == 'int':
                    if prvek_1 != prvek_2:
                        navrat = prvek_1 < prvek_2
                    else:
                        navrat = None
                else:
                    navrat = porovnej_pole([[prvek_1],prvek_2], indent+1)
            else:
                if type(prvek_2).__name__ == 'int':
                    navrat = porovnej_pole([prvek_1,[prvek_2]], indent+1)
                else:
                    navrat = porovnej_pole([prvek_1,prvek_2], indent+1)
            if navrat is not None:
                break
        logging.debug(' '*indent + f"Porovnani {dvojice} dopadlo {navrat}")
        return navrat
    
    except ValueError:
        navrat = len(dvojice[0]) < len(dvojice[1])
        logging.debug(' '*indent + f"Porovnani {dvojice} dopadlo {navrat}, protoze je jedno kratsi")
        return navrat
def moje_rovnani(x,y):
    ret = porovnej_pole([x,y])
    if ret:
        return 1
    return -1
    
                
def main():
    logging.basicConfig(level=logging.DEBUG, format='%(funcName)s (%(lineno)d): %(message)s')
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    with open(input_file) as f:
        lines = f.readlines()
        policka = []
        policka_part2 = []
        for i in range(math.ceil(len(lines)/3)):
            pole_1 = json.loads(lines[i*3])
            pole_2 = json.loads(lines[i*3+1])
            policka_part2.append(pole_1)
            policka_part2.append(pole_2)
            policka.append([pole_1,pole_2])
    logging.debug(policka)
    
    porovnej_pole([[9], [8, 7, 6]])
    counter = 0
    for pozice,dvojice in enumerate(policka):
        vysledek = porovnej_pole(dvojice)
        if vysledek:
            counter += pozice + 1
        logging.info(f'Porovnani {dvojice} dopadlo {vysledek}')
    (start_id, end_id) = (0,0)
    for i, t in enumerate(sorted(policka_part2,key=functools.cmp_to_key(moje_rovnani),reverse=True)):
        if t == [[2]]:
            start_id = i+1
        if t == [[6]]:
            end_id = i+1
        logging.debug(t)
    print(f"soucet pozic je {counter}, dekoder je {start_id*end_id}")
if __name__ == '__main__':
    main()