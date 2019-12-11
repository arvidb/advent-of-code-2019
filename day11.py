'''input
3,8,1005,8,290,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,28,1006,0,59,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,53,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,76,1006,0,81,1,1005,2,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,105,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,126,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,148,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,171,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,193,1,1008,8,10,1,106,3,10,1006,0,18,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,225,1,1009,9,10,1006,0,92,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,254,2,1001,8,10,1,106,11,10,2,102,13,10,1006,0,78,101,1,9,9,1007,9,987,10,1005,10,15,99,109,612,104,0,104,1,21102,1,825594852136,1,21101,0,307,0,1106,0,411,21101,0,825326580628,1,21101,0,318,0,1105,1,411,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,179557207043,1,1,21101,0,365,0,1106,0,411,21101,0,46213012483,1,21102,376,1,0,1106,0,411,3,10,104,0,104,0,3,10,104,0,104,0,21101,988648727316,0,1,21102,399,1,0,1105,1,411,21102,988224959252,1,1,21101,0,410,0,1106,0,411,99,109,2,21201,-1,0,1,21101,0,40,2,21102,1,442,3,21101,432,0,0,1105,1,475,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,437,438,453,4,0,1001,437,1,437,108,4,437,10,1006,10,469,1102,0,1,437,109,-2,2105,1,0,0,109,4,2102,1,-1,474,1207,-3,0,10,1006,10,492,21101,0,0,-3,21202,-3,1,1,22102,1,-2,2,21101,0,1,3,21102,511,1,0,1105,1,516,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,539,2207,-4,-2,10,1006,10,539,21201,-4,0,-4,1106,0,607,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21101,558,0,0,1106,0,516,22101,0,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,577,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,599,21201,-1,0,1,21101,0,599,0,105,1,474,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0
'''
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
                self.program_set(out, self.inputs.popleft())            
      
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
computer = Computer(list(program))

dirs = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

def turn_right(direction):
    return (direction + 1) % 4

def turn_left(direction):
    return direction - 1 if direction > 0 else 3

COLOR_BLACK = 0
COLOR_WHITE = 1

cur_dir = 0
cur_pos = (0,0)
floor = {}
is_moving = False

computer.add_input(COLOR_WHITE)
for output in computer.run_program():
    if is_moving:
        cur_dir = turn_right(cur_dir) if output else turn_left(cur_dir)
        cur_pos = tuple(map(operator.add, cur_pos, dirs[cur_dir]))
        is_moving = False

        computer.add_input(floor.get(cur_pos, COLOR_BLACK))
    else:
        floor[cur_pos] = output
        is_moving = True

print('Paint count:', len(floor))

x_values, y_values = zip(*floor.keys())
min_x, max_x = (min(x_values), max(x_values))
min_y, max_y = (min(y_values), max(y_values))
print('Painting:')
for y in range(max_y, min_y-1, -1):
    print(''.join(
        ['$' if floor.get((x, y)) else ' ' for x in range(min_x, max_x + 1)])
    )