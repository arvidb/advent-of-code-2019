'''input
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
computer = Computer(list(program))

tiles = [' ', '$', '#', '-', 'O',]

STATE_READ_X = 0
STATE_READ_Y = 1
STATE_READ_TILE = 2

screen = {}
state = STATE_READ_X

current_position = [0,0]
for output in computer.run_program():

    if state == STATE_READ_X:
        current_position[0] = int(output)
    elif state == STATE_READ_Y:
        current_position[1] = int(output)
    elif state == STATE_READ_TILE:
        screen[tuple(current_position)] = tiles[int(output)]

    state = (state+1) % 3

print('Part 1:', sum([tile == '#' for tile in screen.values()]))

def draw_screen(screen):
    for y in range(0, 22):
        print(''.join([screen.get((x, y), '?') for x in range(37)]))

computer = Computer(list(program))
computer.program[0] = '2'
state = STATE_READ_X

ball_position = None
paddle_position = None
score = 0
screen = {}
for output in computer.run_program():

    if output == WAIT_FOR_INPUT:
        move = 1 if ball_position[0] > paddle_position[0] else -1 if ball_position[0] < paddle_position[0] else 0
        computer.add_input(move)
        #draw_screen(screen)
        continue

    if state == STATE_READ_X:
        current_position[0] = int(output)
    elif state == STATE_READ_Y:
        current_position[1] = int(output)
    elif state == STATE_READ_TILE:
        if current_position == [-1, 0]:
            score = int(output)
        else:
            if int(output) == 4:
                ball_position = tuple(current_position)
            elif int(output) == 3:
                paddle_position = tuple(current_position)
            screen[tuple(current_position)] = tiles[int(output)]

    state = (state+1) % 3

print('Part 2:', score)
