import os
import logging
corners = None
def udelej_offset_k_mape(offset,bod):
    return [bod[0],bod[1]-offset]
def draw_rocks(mapa,corners,start,end):
    logging.debug(f'Kreslim kamen z {start} do {end}')
    for x in range(min(start[0],end[0]),max(start[0],end[0])+1):
        for y in range(min(start[1],end[1]),max(start[1],end[1])+1):
            bod = udelej_offset_k_mape(corners[0][1],[x,y])
            mapa[bod[0]][bod[1]] = '#'
            tiskni_mapu(mapa)
            ""
def get_corners(line):
    y = [ int(souradnice.split(',')[0]) for souradnice in line.split(' -> ')]
    x = [ int(souradnice.split(',')[1]) for souradnice in line.split(' -> ')] + [0]
    z =1
    return [[min(x),min(y)], [max(x),max(y)]]
def tiskni_mapu(mapa):
    logging.debug('Aktualni mapa:')
    for line in mapa:
        logging.debug(''.join(line))
def get_dalsi_misto(mapa,bod):
    #pohyb dolu
    if len(mapa) == bod[0]:
        return [True, None]
    if mapa[bod[0]+1][bod[1]] == '.':
        return [False, [bod[0]+1,bod[1]]]
    
    #pohyb doleva dolu
    if bod[1] == 0:
        return [True, None]
    if mapa[bod[0]+1][bod[1]-1] == '.':
        return [False, [bod[0]+1,bod[1]-1]]
    
    #pohyb doprava dolu
    if bod[1] == len(mapa[0])-1:
        return [True, None]
    if mapa[bod[0]+1][bod[1]+1] == '.':
        return [False, [bod[0]+1,bod[1]+1]]
    return [True, bod]
def sypej(mapa,bod):
    mapa[bod[0]][bod[1]] = '+'
    tiskni_mapu(mapa)
    [je_konec,dalsi_misto] = get_dalsi_misto(mapa,bod)
    if je_konec:
        if dalsi_misto is None:
            mapa[bod[0]][bod[1]] = '.'
            return True
        else:
            mapa[bod[0]][bod[1]] = 'o'
            return False
    mapa[bod[0]][bod[1]] = '.'
    return sypej(mapa,dalsi_misto)

def main():
# Get the name of the Python script
    logging.basicConfig(level=logging.ERROR, format='%(funcName)s (%(lineno)d): %(message)s')
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    with open(input_file) as f:
        lines = f.readlines()
        corners = get_corners(' -> '.join(lines))
        logging.debug(f'Nasel jsem rohy: {corners}')
    mapa = [['.']*(corners[1][1] - corners[0][1]+1) for _ in range(corners[1][0] - corners[0][0]+1)]
    for line in lines:
        logging.debug(f'Zpracovavam kamenny segment {line}')
        start_bod = None
        for bod in [list(map(int, item.split(','))) for item in line.split(' -> ')]:
            
            if start_bod == None:
                start_bod = [ int(bod[1]) , int(bod[0]) ]
            else:
                end_bod = [ int(bod[1]) , int(bod[0]) ]
                draw_rocks(mapa,corners,start_bod,end_bod)
                start_bod = end_bod
    round = 0
    while not sypej(mapa,udelej_offset_k_mape(corners[0][1],[0,500])):
        round+=1
        if round % 100 == 0:
            logging.getLogger().setLevel(logging.DEBUG)
        else:
            logging.getLogger().setLevel(logging.CRITICAL)

    
    tiskni_mapu(mapa)
    print('Pocet kameni v jeskyni: ',sum(line.count('o') for line in mapa))
if __name__ == '__main__':
    main()
