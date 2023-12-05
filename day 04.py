import os
def zkontroluj_podmnozinu(elf1,elf2):
    if elf1[0] <= elf2[0] and elf1[1]>= elf2[1]:
        return True
    if elf2[0] <= elf1[0] and elf2[1]>= elf1[1]:
        return True
    return False
def zkontroluj_prunik(elf1,elf2):
    if elf1[1] >= elf2[0] and elf1[0] <= elf2[1]:
        return True
    if elf2[1] >= elf1[0] and elf2[0] <= elf1[1]:
        return True
    
    return False
def main():
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    counter = 0
    counter2 = 0
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line == '#':
                break
            print(line)
            (elf1,elf2) = line.split(',')
            elf1 = [int(z) for z in elf1.split('-')]
            elf2 = [int(z) for z in elf2.split('-')]
            if zkontroluj_podmnozinu(elf1,elf2):
                counter+=1
            if zkontroluj_prunik(elf1,elf2):
                counter2+=1
    print("Part1: ",counter)
    print("Part2: ",counter2)
if __name__ == '__main__':
    main()