import os
def main():
    # Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    elves = [0]
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line == '':
                elves.append(0)
                continue
            elves[-1] += int(line)
            
            
            #print(line)
    group_counter = 0
    for group in range(3):
        print(f'{group}. elf nese:{max(elves)}')
        group_counter+=max(elves)
        elves.remove(max(elves))
    print(f'Skupina 3 elfu nese dohromady {group_counter}')
if __name__ == '__main__':
    main()