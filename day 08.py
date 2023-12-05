import os
def check_from_left(field,trees, range_row):
    
    for line in range(len(field)):
        last = None
        for row in range_row:
            if last==None or int(field[line][row]) > last:
                trees[line][row] = True
                last = int(field[line][row])
def init_distance():
    return [0 for _ in range(10)]
def modify_distance(distance,tree_height):
    for i in range(tree_height+1):
        distance[i] = 1
    for i in range(tree_height+1,10):
        distance[i] += 1
def check_from_left_2(field,trees, range_row, index):
    
    for line in range(len(field)):
        distance = init_distance()
        for row in range_row:
            trees[line][row][index] = distance[int(field[line][row])]
            modify_distance(distance,int(field[line][row]))
def check_from_top_2(field,trees,range_line, index ):
    
    for row in range(len(field)):
        distance = init_distance()
        for line in range_line:
            trees[line][row][index]
            distance[int(field[line][row])]
            trees[line][row][index] = distance[int(field[line][row])]
            modify_distance(distance,int(field[line][row]))
                
            
            
def check_from_top(field,trees,range_line ):
    
    for row in range(len(field)):
        last = None
        for line in range_line:
            if last==None or int(field[line][row]) > last:
                trees[line][row] = True
                last = int(field[line][row])
def find_best_tree(trees):
    best = 1
    for i,rows in enumerate(trees):
        for j,field in enumerate(rows):
            value = 1
            for direction in field:
                value *=direction
            if value > best:
                print(f'Best tree so far: i={i},j={j}, value={value}, directions={field}')
                best = value
    return best
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
            #print(line)
            
            
    trees = []
    trees2 = []
    for radek in range(len(field)):
        trees.append([])
        trees2.append([])
        for sloupec in range(len(field[0])):
            trees[-1].append(False)
            trees2[-1].append([0,0,0,0])
    check_from_left(field,trees,range(len(field)))
    check_from_top(field,trees, range(len(field)))
    check_from_left(field,trees,range(len(field)-1,0,-1))
    check_from_top(field,trees,range(len(field)-1,0,-1))
    print(count_trees(trees))
    check_from_left_2(field,trees2,range(len(field)),0)
    check_from_top_2(field,trees2, range(len(field)),1)
    check_from_left_2(field,trees2,range(len(field)-1,0,-1),2)
    check_from_top_2(field,trees2, range(len(field)-1,0,-1),3)
    print(find_best_tree(trees2))
    ""
    
if __name__ == '__main__':
    main()