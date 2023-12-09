import os
import logging
import re
import itertools

map_coord = {
    0: 'x',
    1: 'y'
}
def get_corners(a,b):
    min_x = min([a[0]],b[0])
    min_y = min([a[1]],b[1])
    max_x = max([a[0]],b[0])
    max_y = max([a[1]],b[1])
    return [min_x, min_y, max_x, max_y]
def get_nonbeacon_positions(sensors, focus_y):
    sensors_and_distances = [[sensor[0],abs(sensor[0][0]-sensor[1][0])+abs(sensor[0][1]-sensor[1][1])] for sensor in sensors]
    #beacons = [[sensor[0][0]+sensor[1][0],sensor[0][1]+sensor[1][1]] for sensor in sensors]
    field = {}
    for coord in range(2):
        for op in [min,max]:
            field_key = f'{op.__name__}_{map_coord[coord]}'
            field_value = op(op(sensor[0][coord],sensor[1][coord]) for sensor in sensors)
            field[field_key] = field_value
    candidates = [[sd[0][0] - (sd[1] - abs(focus_y-sd[0][1])), sd[0][0] + (sd[1] - abs(focus_y-sd[0][1])), sd]   for sd in sensors_and_distances if (abs(focus_y-sd[0][1]) < sd[1] )]
    ranges = None
    for a in sorted(candidates,key=lambda x: x[0]):
        if not ranges:
            ranges = [a]
        if ranges[-1][1] >= a[0]:
            
            ranges[-1][1] = max(ranges[-1][1],a[1])
        else:
            ranges.append(a)
    return ranges
    
    #beacons_and_sensors_rectangles = [ get_corners(bac[0],bac[1]) for bac in sensors]
    
    
def main():
# Get the name of the Python script
    logging.basicConfig(level=logging.DEBUG, format='%(funcName)s (%(lineno)d): %(message)s')
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    sensors = []
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line == '#':
                break
            print(line)
            m = re.search('x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)',line)
            if m:
               sensors.append([[int(m.group(1)),int(m.group(2))],[int(m.group(3)),int(m.group(4))]]) 
            else:
                logging.debug(f'Nepodarilo se mi rozpoznat souradnice')
    ranges = get_nonbeacon_positions(sensors, 2000000)
    
    print(ranges[0][1] - ranges[0][0])
    #for i in range(3409989):
    for i in [2836447,2836448]:
        
        logging.debug(f'Prochazim {i} kolo - {len(ranges)} = {ranges}')
        ranges = get_nonbeacon_positions(sensors, i)
        if len(ranges)>1:
            logging.debug(f'Prochazim {i} kolo - {len(ranges)} = {ranges}')
        if ranges[0][0] < 0 or ranges[0][1] > 4000000:
            continue
        else:
            logging.debug(f'Kandidat {i} kolo - {len(ranges)} = {ranges}')
        
    
    #5667228 is too high
    #11345799409990 is too low
if __name__ == '__main__':
    main()