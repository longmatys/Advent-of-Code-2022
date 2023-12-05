import os
from dataclasses import dataclass, field
import uuid

@dataclass
class node:
    ID: str = field(default_factory=lambda: uuid.uuid4().hex)
    node_type: str = ''
    childs: list = field(default_factory=lambda: list())
    parent: str = ''
    node_name: str = ''
    def get_description(self):
        if self.node_type == 'dir':
            return self.node_type
        return f'file, size={self.node_type.split(" ")[0]}'
    
@dataclass
class filesystem:
    nodes: dict = field(default_factory=lambda: {})
    current: node = None
    root: node = None
    running_command: str = ''
    def get_child(self,name):
        for child in self.current.childs:
            if child.node_name == name:
                return child
        return None
    #def add_node(self,line):
    def add_child(self,definice):
        n = node(node_name=definice[1], node_type=definice[0], parent=self.current)
        self.current.childs.append(n)
        return(n)
        
    def cmd_ls_args(self,buffer):
        node = self.get_child(buffer.split(' ')[1])
        if not node:
            self.add_child(buffer.split(' '))
    def cmd_ls(self,buffer):
        self.running_command = 'ls'
        
    def cmd_cd(self,buffer):
        argument = buffer.split(' ')[2]
        if argument == '/':
            if self.root:
                self.current = self.root
            else:
                self.root = node(node_name='/', node_type='dir')
                self.current = self.root
        elif argument == '..':
            self.current = self.current.parent
        else:
            self.current = self.get_child(argument)
    def dump_n(self,n:node, indent:int = 0):
        local_size = 0
        ret_array = []
        if n.node_type.split(' ')[0].isnumeric():
            local_size += int(n.node_type.split(' ')[0])
        print(' '*indent*2+f'- {n.node_name} ({n.get_description()})')
        for child in n.childs:
            ret = self.dump_n(child,indent+1)
            if len(ret) and ret[0][0] == child.node_name:
                local_size+= ret[0][1]
                ret_array += ret
        
        return [[n.node_name,local_size,n.node_type]] + ret_array
        
                
            
        
        
    
    
def main():
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    fs = filesystem()
    
    
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line == '#':
                break
            print(line)
            if line.startswith('$ '):
                line_a = line.split(' ')
                getattr(fs, 'cmd_' + line_a[1])(line)
            else:
                getattr(fs, f'cmd_{fs.running_command}_args' )(line)
    dumped = fs.dump_n(fs.root,0)
    
    counter = 0
    for item in dumped:
        if item[1] <= 100000 and item[2]=='dir':
            counter+=item[1]
    
    print(counter)
    size_fs = 70000000
    size_needed = 30000000
    size_available = size_fs - dumped[0][1]
    size_to_free = size_needed - size_available
    
    candidate = None
    for item in sorted(dumped,key=lambda x: x[1], reverse=True):
        if item[1] > size_to_free:
            candidate = item
        else:
            print(candidate)
            break
    
if __name__ == '__main__':
    main()