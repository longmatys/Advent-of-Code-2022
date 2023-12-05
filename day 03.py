import os
def najdi_chybu(line):
    for i in range(int(len(line)/2)):
        if line[i] in line[int(len(line)/2):]:
            return line[i]
def ziskej_hodnotu(znak):
    base = ord('A')
    if ord(znak) >= ord('a'):
        return ord(znak) - ord('a') +1
    return ord(znak) - ord('A') + 27
        
    
def eval_line(line):
    err_item = najdi_chybu(line)
    err_value = ziskej_hodnotu(err_item)
    return err_value
    
def main():
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    suma = 0
    lines = []
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line == '#':
                break
            lines.append(line)
            suma+=eval_line(line)
    print("Part 1:",suma)
    suma2 = 0
    for i in range(int(len(lines)/3)):
        for znak in list(range(ord('a'),ord('z')+1)) + list(range(ord('A'),ord('Z')+1)):
            counter = 0
            for line in lines[i*3:i*3+3]:
                if chr(znak) in line:
                    
                    counter+=1
            if counter==3:
                #print(f'Nasel jsem {i} skupinu se znakem {chr(znak)}')
                suma2+= ziskej_hodnotu(chr(znak))
    print("Part 2:",suma2)
            
if __name__ == '__main__':
    main()