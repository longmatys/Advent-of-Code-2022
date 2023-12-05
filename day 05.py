import os
def reverse_stacks(stacks_reversed):
    stacks = [[] for _ in range(len(stacks_reversed))]
    for i in range(len(stacks_reversed)):
        while len(stacks_reversed[i]):
            stacks[i].append(stacks_reversed[i].pop())
    return stacks
def move_crates(crates,count,start,end):
    for _ in range(count):
        a = crates[start-1].pop()
        crates[end-1].append(a)
def move_crates_9001(crates,count,start,end):
    temp_stack = []
    for _ in range(count):
        a = crates[start-1].pop()
        temp_stack.append(a)
    for _ in range(count):
        a = temp_stack.pop()
        crates[end-1].append(a)
def main():
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    stacks_reversed = [[] for _ in range(9)]
    stacks = None
    with open(input_file) as f:
        for line in f.readlines():
            if line.find('[')>=0:
                for i in range(len(stacks_reversed)):
                    if line[i*3+1+i] != ' ':
                        stacks_reversed[i].append(line[i*3+1+i])
                continue
            
            line = line.strip()
            if line.startswith('#'):
                break
            if line == '':
                stacks = reverse_stacks(stacks_reversed)
            if line.startswith('move'):
                line_a = line.split(' ')
                move_crates_9001(stacks,int(line_a[1]),int(line_a[3]),int(line_a[5]))
            print(line)
    for stack in stacks:
        print(f'{stack.pop()}',end='')
    print('')
if __name__ == '__main__':
    main()