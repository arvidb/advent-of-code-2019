'''input
3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,102,1,1034,1039,1002,1036,1,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,102,1,1034,1039,101,0,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1105,1,124,1001,1034,-1,1039,1008,1036,0,1041,101,0,1035,1040,1001,1038,0,1043,101,0,1037,1042,1105,1,124,1001,1034,1,1039,1008,1036,0,1041,101,0,1035,1040,101,0,1038,1043,101,0,1037,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,5,1032,1006,1032,165,1008,1040,9,1032,1006,1032,165,1102,1,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1105,1,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,73,1044,1106,0,224,1101,0,0,1044,1106,0,224,1006,1044,247,101,0,1039,1034,1002,1040,1,1035,1002,1041,1,1036,1002,1043,1,1038,101,0,1042,1037,4,1044,1105,1,0,43,57,94,36,95,30,10,40,88,72,99,97,53,21,87,48,77,40,75,69,46,98,78,22,21,38,17,12,96,34,94,81,18,49,92,1,26,67,48,15,80,51,60,92,9,77,89,64,15,85,53,94,84,99,70,7,8,69,79,79,41,62,98,22,94,92,69,97,65,96,47,99,71,4,75,10,89,85,13,89,93,93,33,46,80,61,80,75,47,99,54,63,54,57,99,80,97,77,48,33,97,95,92,20,75,3,90,84,1,50,15,94,80,95,93,70,22,3,74,69,27,99,91,66,99,1,67,12,94,31,78,83,51,97,25,4,92,85,3,96,60,5,98,69,23,95,70,92,99,1,5,84,51,87,60,67,56,98,44,80,71,81,59,58,97,82,48,87,4,76,87,45,23,75,62,89,29,37,83,22,89,81,48,64,92,30,13,90,89,83,50,49,14,89,2,34,39,84,88,21,1,81,41,74,95,89,37,82,30,87,11,93,78,67,99,8,95,84,26,93,9,95,7,18,93,94,55,96,50,92,97,43,88,53,22,91,91,35,5,79,34,66,56,24,95,49,86,72,98,52,19,81,10,90,78,12,76,8,37,87,62,80,98,52,19,40,97,83,70,18,94,77,62,87,13,35,90,35,78,68,84,89,77,13,71,19,81,54,96,88,22,40,99,24,62,85,37,95,97,89,64,30,18,98,95,9,27,76,85,49,99,31,55,71,89,95,86,94,69,24,98,32,84,99,72,82,89,61,75,30,90,74,10,71,14,80,55,68,61,99,54,84,49,17,74,83,79,38,25,90,38,99,36,89,14,38,80,71,92,10,4,65,35,78,95,40,36,78,13,39,83,76,82,64,16,96,95,31,75,95,79,2,89,38,36,87,36,76,81,38,42,92,38,7,83,87,83,87,54,96,99,78,50,43,94,96,41,87,77,8,90,78,72,79,49,82,82,56,13,94,34,90,44,82,22,60,96,48,97,2,88,87,47,92,40,91,4,58,93,29,61,83,98,99,7,8,91,30,15,88,20,90,79,10,93,31,41,95,94,56,94,95,70,93,50,94,40,37,42,84,45,35,59,27,75,80,52,90,93,15,21,92,18,52,96,83,1,90,86,12,79,21,38,98,13,74,99,40,85,41,60,94,54,44,98,83,35,57,76,66,94,94,59,82,62,77,76,22,87,39,95,98,5,90,60,88,46,91,23,58,16,83,79,7,99,11,53,76,12,88,96,88,35,58,63,81,12,26,79,89,79,26,28,23,5,90,1,76,85,55,74,44,42,88,78,36,83,61,86,92,37,62,82,80,60,46,78,32,76,20,56,77,81,9,40,45,81,85,46,7,65,96,90,19,83,16,78,66,25,24,87,80,55,93,71,84,21,86,38,79,80,94,11,42,81,89,56,18,81,33,86,72,48,86,90,59,10,92,35,77,39,94,58,97,36,5,90,96,87,40,21,22,74,80,42,32,59,60,96,25,26,95,54,90,54,15,18,98,61,91,58,84,2,19,83,36,87,60,99,63,34,79,84,92,25,74,62,6,76,84,33,80,54,91,84,3,83,95,34,22,92,88,6,88,93,17,87,59,95,17,98,65,24,20,90,95,31,74,93,30,66,80,79,72,98,7,74,34,87,77,3,24,4,82,93,42,53,90,47,82,65,65,16,75,91,79,20,93,77,54,71,81,47,82,18,78,94,92,63,75,36,87,34,87,31,92,29,98,22,80,95,91,17,97,35,79,87,87,61,93,93,99,63,95,36,90,78,77,61,83,0,0,21,21,1,10,1,0,0,0,0,0,0
'''
import operator
import random
from collections import deque
from random import randrange

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

def draw_floor(floor):
    if len(floor) == 0:
        return
    x_values, y_values = zip(*floor.keys())
    min_x, max_x = (min(x_values), max(x_values))
    min_y, max_y = (min(y_values), max(y_values))
    for y in range(max_y, min_y-1, -1):
        print(''.join(
            [floor.get((x, y), ' ') for x in range(min_x, max_x + 1)])
        )

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

program = input().split(',')
computer = Computer(list(program))

cur_dir = 0
cur_pos = (0,0)
floor = {}
next_move = 0

for output in computer.run_program():

    if output == WAIT_FOR_INPUT:
        computer.add_input(next_move+1)
        continue

    if output == 0:
        # Wall
        wall_pos = tuple(map(operator.add, cur_pos, dirs[next_move]))
        floor[wall_pos] = '#'
    elif output == 1:
        # Moved one
        floor[cur_pos] = '.'
        cur_pos = tuple(map(operator.add, cur_pos, dirs[next_move]))
        floor[cur_pos] = 'D'
    elif output == 2:
        # Moved + found oxygen
        floor[cur_pos] = '.'
        cur_pos = tuple(map(operator.add, cur_pos, dirs[cur_dir]))
        floor[cur_pos] = 'O'
        print('Found it at', cur_pos)
        break

    next_move = random.choice([x for x in range(4)])

draw_floor(floor)

def bfs(graph):
    visited = set()
    q = deque([((0,0), 0)])
    visited.add((0,0))
    while q: 
        coord, steps = q.popleft()
        if coord in graph:
            if graph[coord] == 'O':
                return steps
            elif graph[coord] == '#':
                visited.add(coord)
                continue
            else:
                for neighbour in [(-1,0), (1,0), (0,-1), (0,1)]:
                    neighbour = tuple(map(operator.add, coord, neighbour))
                    if neighbour not in visited: 
                        visited.add(neighbour)
                        q.append((neighbour, steps + 1))

print('Part 1', bfs(floor))