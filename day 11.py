import os
from collections import deque
import math
import logging
from typing import List, Dict, Type
import sys
#sys.set_int_max_str_digits(0)
#l = deque(['a', 'b', 'c', 'd'])
#l.popleft()
from dataclasses import dataclass,field

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}
        
@dataclass
class opice_v_lese_class:
    stado_opic: List[Type["opice_class"]] = field(default_factory=list)
    global_modulo: int = 1
    def parse_line(self,line:str):
        if line.startswith('Monkey'):
            self.stado_opic.append(opice_class(self))
            logging.info(f"Zalozena opice {len(self.stado_opic)}")
        elif line.startswith("Operation:"):
            self.stado_opic[-1].operace = line.split('= ')[1]
            logging.info(f"Pridana operace {self.stado_opic[-1].operace}")
        elif line.startswith("Test:"):
            self.stado_opic[-1].test_deleni = int(line.split(' by ')[1])
            logging.info(f"Pridan test deleni {self.stado_opic[-1].test_deleni}")
        elif line.startswith("If true:"):
            self.stado_opic[-1].dalsi_opice[True] = int(line.split(' monkey ')[1])
            logging.info(f"Pridana dalsi opice pro TRUE {self.stado_opic[-1].dalsi_opice[True]}")
        elif line.startswith("If false:"):
            self.stado_opic[-1].dalsi_opice[False] = int(line.split(' monkey ')[1])
            logging.info(f"Pridana dalsi opice pro FALSE {self.stado_opic[-1].dalsi_opice[True]}")
        elif line.startswith("Starting items:"):
            self.stado_opic[-1].veci = [int(element.strip()) for element in line.split(' items: ')[1].split(',')]
            logging.info(f"Pridane veci pro opici {self.stado_opic[-1].veci}")
        else:
            logging.error(line)
    def ochrana_pred_chocholouskem(self):
        for id,opice in enumerate(self.stado_opic):
            self.global_modulo *= opice.test_deleni
    def hrajeme(self, game_type='Part 1'):
        
        for id,opice in enumerate(self.stado_opic):
            logging.warning(f"Monkey {id}:")
            opice.zahraj_si(game_type)
            
        
@dataclass
class opice_class:
    muj_les: opice_v_lese_class
    veci: List[int] = field(default_factory=list)
    operace: str = ''
    test_deleni: int = 0
    dalsi_opice: Dict[bool,int] = field(default_factory= lambda: { True:0, False:0})
    pocet_prohlidnutych_veci: int = 0
    def nahrad_promenne(self,promenna,hodnota):
        if promenna == 'old':
            return hodnota
        else:
            return int(promenna)
    def zahraj_si(self, game_type):
        
        logging.warning(f"Opice ma na zacatku veci: {self.veci} a operaci {self.operace}")
        
        for vec in self.veci:
        
            logging.error('  '*1 + f"Monkey inspects an item with a worry level of {vec}. (Inspected {self.pocet_prohlidnutych_veci} -> {self.pocet_prohlidnutych_veci+1})")
            self.pocet_prohlidnutych_veci += 1
            
            instrukce = self.operace.split(' ')
            nova_vec = operators[instrukce[1]](self.nahrad_promenne(instrukce[0], vec), self.nahrad_promenne(instrukce[2], vec))
        
            logging.error('  '*2 + f"Worry level is multiplied by {self.nahrad_promenne(instrukce[2], vec)} to {nova_vec}.")
            if game_type == 'Part 1':
                nova_vec = math.floor(nova_vec/3)
                logging.error('  '*2 + f"Monkey gets bored with item. Worry level is divided by 3 to {nova_vec}.")
            if nova_vec % self.muj_les.global_modulo != nova_vec:
                logging.info('*'*4 + f"Ochrana pred vesmirnymi cisly")
                nova_vec = nova_vec % self.muj_les.global_modulo
            if nova_vec % self.test_deleni == 0:
                logging.error('  '*2 + f"Current worry level is divisible by {self.test_deleni}.")
                self.muj_les.stado_opic[self.dalsi_opice[True]].veci.append(nova_vec)
            else:
                logging.error('  '*2 + f"Current worry level is NOT divisible by {self.test_deleni}.")
                self.muj_les.stado_opic[self.dalsi_opice[False]].veci.append(nova_vec)
        self.veci = []
            
        

def main():
    logging.basicConfig(level=logging.CRITICAL, format='%(funcName)s (%(lineno)d): %(message)s')
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    opice_v_lese = opice_v_lese_class()
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line == '#':
                break
            
            if line == '':
                continue
            opice_v_lese.parse_line(line)
    opice_v_lese.ochrana_pred_chocholouskem()
    game_type = 'Part 2'
    rounds = {
        'Part 1': 20,
        'Part 2': 10000
    }
    for round in range(rounds[game_type]):
        if round > 0 and round % 100 == 0:
            print(f'=== ROUND {round}')
            for id_opice,opice in enumerate(opice_v_lese.stado_opic):
                print(f'Monkey {id_opice} inspected items {opice.pocet_prohlidnutych_veci} times.')
        if round % 1000 == 0:
            logging.getLogger().setLevel(logging.DEBUG)
        else:
            logging.getLogger().setLevel(logging.CRITICAL)
                
        opice_v_lese.hrajeme(game_type)
    result = []
    global_modulo = 1
    for id_opice,opice in enumerate(opice_v_lese.stado_opic):
        print(f'Monkey {id_opice} inspected items {opice.pocet_prohlidnutych_veci} times.')
        global_modulo *= opice.test_deleni
        result.append(opice.pocet_prohlidnutych_veci)
    result.sort(reverse=True)
    print(f'monkey business: {result[0]*result[1]}, global modulo: {global_modulo}')
        
if __name__ == '__main__':
    main()