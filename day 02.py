import os
names = {
    'A': {'name': 'kamen', 'value': 1},
    'B': {'name': 'papir', 'value': 2},
    'C': {'name': 'nuzky', 'value': 3},
    'X': {'name': 'kamen', 'value': 1},
    'Y': {'name': 'papir', 'value': 2},
    'Z': {'name': 'nuzky', 'value': 3},
    1: {'name': 'vyhra', 'value': 6},
    0: {'name': 'vyhra', 'value': 3},
    -1: {'name': 'vyhra', 'value': 0}
}
combos = {
    'A': {
        'X': 0,
        'Y': 1,
        'Z': -1
    },
    'B': {
        'X': -1,
        'Y': 0,
        'Z': 1
    },
    'C': {
        'X': 1,
        'Y': -1,
        'Z': 0
    }    
}
translate = {
    'X': -1,
    'Y': 0,
    'Z': 1
}
combos2 = {}
def enrich_combos():
    for elf,item in combos.items():
        for me, result in item.items():
            if not combos2.get(elf):
                combos2[elf]={}
            combos2[elf][result] = me
            
def vyhodnot2(line_a):
    real_choice = combos2[line_a[0]][translate[line_a[1]]]
    res = combos[line_a[0]][real_choice]
    return names[res]['value'] + names[real_choice]['value']
    ""
def vyhodnot(line_a):
    res = combos[line_a[0]][line_a[1]]
    return names[res]['value'] + names[line_a[1]]['value']
def main():
    # Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    enrich_combos()
    counter = 0
    counter2 = 0
    with open(input_file) as f:
        for line in f.readlines():
            line_a = line.strip().split(' ')
            counter+= vyhodnot(line_a)
            counter2+= vyhodnot2(line_a)

            #print(line)
    print(counter, counter2)
if __name__ == '__main__':
    main()