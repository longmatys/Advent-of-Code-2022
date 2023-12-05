import os
def check_from_left(field,trees, range_row):
    
    for line in range(len(field)):
        last = None
        for row in range_row:
            if last==None or int(field[line][row]) > last:
                trees[line][row] = True
                last = int(field[line][row])
            #if last == 9:
            #    break
        ""
def check_from_top(field,trees,range_line ):
    a=1
    for row in range(len(field)):
        last = None
        for line in range_line:
            if last==None or int(field[line][row]) > last:
                trees[line][row] = True
                last = int(field[line][row])
            #if last == 9:
            #    break
def count_trees(trees):
    counter=0
    for line in trees:
        for field in line:
            if field:
                counter+=1
    return counter
def main():
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    field = []
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line=='#':
                break
            field.append(line)
            print(line)
            
            
    trees = []
    for radek in range(len(field)):
        trees.append([])
        for sloupec in range(len(field[0])):
            trees[-1].append(False)
    check_from_left(field,trees,range(len(field)))
    check_from_top(field,trees, range(len(field)))
    check_from_left(field,trees,range(len(field)-1,0,-1))
    check_from_top(field,trees,range(len(field)-1,0,-1))
    print(count_trees(trees))
    ""
    
if __name__ == '__main__':
    main()