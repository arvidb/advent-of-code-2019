import operator
from collections import deque
  
OP_ADD = '01'
OP_MULT = '02'
OP_INPUT = '03'
OP_OUTPUT = '04'
OP_JMP_IF_TRUE = '05'
OP_JMP_IF_FALSE = '06'
OP_LESS = '07'
OP_EQ = '08'
OP_ADJ_BASE = '09'
OP_HALT = '99'

WAIT_FOR_INPUT = "WAIT_FOR_INPUT"
HALT = -1
OK = 0

class Computer():
    def __init__(self, program):
        self.program = program
        self.inputs = deque()
        self.output = None
        self.reset()

    def reset(self):
        self.ip = 0
        self.base = 0
        self.output = None
        self.inputs.clear()

    def add_input(self, input):
        self.inputs.append(str(input))
        return self

    def step(self):
        self.ip = self.ip+1
        return self.ip

    def expand_memory_if_needed(self, ip):
        if ip >= len(self.program):
            self.program += ['0']*(ip-len(self.program)+10)

    def program_set(self, ip, value):
        self.expand_memory_if_needed(ip)       
        self.program[ip] = str(value)
  
    def program_get_char(self, ip):
        self.expand_memory_if_needed(ip) 
        return self.program[ip]

    def program_get_int(self, ip):
        return int(self.program_get_char(ip))

    def program_get_addr(self, ip):
        return self.program_get_int(self.program_get_int(ip))
  
    def get_input_value(self, mode):
        if mode == '0':
            # position mode, value at address X
            return self.program_get_addr(self.step())
        elif mode == '1':
            # imeediate mode, value is X
            return self.program_get_int(self.step())
        elif mode == '2':
            offs = self.program_get_int(self.step())
            addr = self.base + offs
            return self.program_get_int(addr)
        else:
            print('error')
 
    def get_output_index(self, mode):
        if mode == '0' or mode == '1':
            return self.program_get_int(self.step())
        elif mode == '2':            
            return self.base + self.program_get_int(self.step())
        else:
            print('error') 

    def run_program(self):

        while self.ip < len(self.program):
            op = self.program_get_char(self.ip)
      
            tmp = list("{:05d}".format(int(op)))
            mode_3, mode_2, mode_1, D, E = tmp
            op = D+E
              
            did_change_ip = False
      
            if op == OP_ADD or op == OP_MULT:
                op1 = self.get_input_value(mode_1)
                op2 = self.get_input_value(mode_2)
                out = self.get_output_index(mode_3)

                result = op1 + op2 if op == OP_ADD else op1 * op2
                self.program_set(out, str(result))
      
            elif op == OP_INPUT:   
                out = self.get_output_index(mode_1)
                while True:
                    if len(self.inputs) > 0:
                        self.program_set(out, self.inputs.popleft())
                        break
                    else:
                        yield WAIT_FOR_INPUT
      
            elif op == OP_OUTPUT:
                op1 = self.get_input_value(mode_1)
                self.output = op1
                yield self.output
      
            elif op == OP_JMP_IF_TRUE or op == OP_JMP_IF_FALSE:            
                op1 = self.get_input_value(mode_1)
                op2 = self.get_input_value(mode_2)

                result = op1 != 0 if op == OP_JMP_IF_TRUE else op1 == 0
                if result:
                    self.ip = op2
                    did_change_ip = True
      
            elif op == OP_LESS or op == OP_EQ:
                op1 = self.get_input_value(mode_1)
                op2 = self.get_input_value(mode_2)
                out = self.get_output_index(mode_3)

                is_true = op1 < op2 if op == OP_LESS else op1 == op2    
                self.program_set(out, '1' if is_true else '0')
      
            elif op == OP_ADJ_BASE:
                op1 = self.get_input_value(mode_1)
                self.base += op1
      
            elif op == OP_HALT:            
                break
      
            if not did_change_ip:
                self.step()


program = input().split(',')
computer = Computer(program)

script = """\
OR A J
AND C J
NOT J J
AND D J
WALK
"""

def get_input():
    for c in script:
        yield ord(c)

input_gen = get_input()
for output in computer.run_program():
    if output == WAIT_FOR_INPUT:
        computer.add_input(next(input_gen))
        continue
    if output > 128:
        print('Damage', outout)
    else:
        print(chr(output), end='')
