import os
from dataclasses import dataclass, field
@dataclass
class computer:
    X: int = 1
    cycle: int = 0
    results: list = field(default_factory=list)
    interesting_cycles: list = field(default_factory=lambda: [20,60,100,140,180,220])
    pixels: list = field(default_factory=lambda: ['.' for _ in range(240)])
    def print_pixels(self):
        pixels_per_line = 40
        for line_id in range(int(len(self.pixels)/pixels_per_line)):
            radek = ''
            for i in range(pixels_per_line):
                radek += self.pixels[line_id*pixels_per_line+i]
            print(radek)
    def process_pixel(self):
        if self.cycle%40 in range(self.X-1,self.X+2):
            self.pixels[self.cycle] = '#'
    def get_next_interesting_cycle(self):
        if len(self.results) == len(self.interesting_cycles):
            return self.cycle + 1000
        return self.interesting_cycles[len(self.results)]
    def is_important_cycle(self, cycle):
        return cycle == self.get_next_interesting_cycle()
    def tick(self):
        self.process_pixel()
        self.cycle += 1
        #print(f'TICK: {self.cycle}')
        if self.cycle == self.get_next_interesting_cycle():
            #print(f'Nasel jsem interesting cycle {self.cycle}, X:{self.X}')
            self.results.append(self.X)
    def noop(self):
        self.tick()
        
        
    def addx(self, argument):
        self.tick()
        self.tick()
        self.X += argument
        
        #print(f'X jsem zvetsil na {self.X}')
        
    def result(self):
        result = 0
        for (a,b) in zip(self.results,self.interesting_cycles):
            result += a*b
        return result
        
            
def main():
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    my_computer = computer()
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line == '#':
                break
            
            
            #print(line)
            if line.startswith('addx'):
                my_computer.addx(int(line.split(' ')[1]))
            else:
                my_computer.noop()
    print("Part 1:",my_computer.result())
    my_computer.print_pixels()
if __name__ == '__main__':
    main()