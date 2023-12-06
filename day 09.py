import os
import math
from dataclasses import dataclass,field
moves = {
    'L': (-1,0),
    'R': (1,0),
    'U': (0,-1),
    'D': (0,1)
}
shorts={
    1: 0,
    0: 0,
    -1: 0,
    2: 1,
    -2: -1
}
@dataclass
class pole:
    x_head: int = 0
    y_head: int = 0
    tail_pole: list = field(default_factory=lambda: [[0,0] for _ in range(9)])
    x_tail: int = 0
    y_tail: int = 0
    visited: set = field(default_factory=lambda: {tuple([0,0])})
    visited2: set = field(default_factory=lambda: {tuple([0,0])})
    visited3: set = field(default_factory=lambda: {tuple([0,0])})
    
    def update_head(self,move):
        self.x_head+=move[0]
        self.y_head+=move[1]
    def get_new_position(self, head, tail):
        diff_x = head[0] - tail[0]
        diff_y = head[1] - tail[1]
        if abs(diff_x) <= 1 and abs(diff_y) <= 1:
            return None
        
        tail[0] += diff_x - shorts[diff_x]
        tail[1] += diff_y - shorts[diff_y]
        return tail
    def update_long_tail(self):
        last_node = [self.x_head,self.y_head]
        for node in self.tail_pole:
            ret = self.get_new_position(last_node,node)
            if ret:
                last_node = node
                
            else:
                break
        #Real tail
        self.visited2.add(tuple(self.tail_pole[-1]))
        #Just a first knot
        self.visited3.add(tuple(self.tail_pole[0]))
    def update_tail(self):
        ret = self.get_new_position([self.x_head,self.y_head],[self.x_tail,self.y_tail])
        if ret:
            [self.x_tail, self.y_tail] = ret
            self.visited.add(tuple(ret))    
        return
        
        
    def move(self,direction, count):
        for _ in range(count):
            move = moves[direction]
            self.update_head(move)
            self.update_tail()
            self.update_long_tail()
    
def main():
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    
    moje_pole = pole()
    
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line=='#':
                break
            print(line)
            
            line_a = line.split(' ')
            moje_pole.move(line_a[0],int(line_a[1]))
    #print(moje_pole.visited)
    print(len(moje_pole.visited), len(moje_pole.visited2), len(moje_pole.visited3))
if __name__ == '__main__':
    main()