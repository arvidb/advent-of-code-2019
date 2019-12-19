'''input
109,424,203,1,21102,11,1,0,1106,0,282,21101,18,0,0,1106,0,259,2101,0,1,221,203,1,21102,31,1,0,1106,0,282,21102,1,38,0,1105,1,259,20102,1,23,2,22101,0,1,3,21101,0,1,1,21101,0,57,0,1106,0,303,1202,1,1,222,21001,221,0,3,20102,1,221,2,21102,259,1,1,21101,80,0,0,1105,1,225,21102,1,149,2,21101,0,91,0,1105,1,303,1202,1,1,223,21002,222,1,4,21102,259,1,3,21102,225,1,2,21102,225,1,1,21101,118,0,0,1105,1,225,20102,1,222,3,21101,0,127,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1106,0,259,1201,1,0,223,21001,221,0,4,21002,222,1,3,21102,14,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,106,0,108,20207,1,223,2,20102,1,23,1,21101,0,-1,3,21102,214,1,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,22102,1,-3,1,21201,-2,0,2,21201,-1,0,3,21102,1,250,0,1105,1,225,22102,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21202,-2,1,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22101,0,-2,3,21101,343,0,0,1106,0,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22101,0,-4,1,21102,1,384,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22102,1,1,-4,109,-5,2106,0,0
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

def sweep(initial_pos, width, height):
	max_x = initial_pos[0] + width
	max_y = initial_pos[1] + height
	next_pos = initial_pos	
	points = 0
	while True:
		x, y = next_pos
		if y >= max_y:
			break

		computer = Computer(list(program))	
		for output in computer.run_program():		
			if output == WAIT_FOR_INPUT:			
				computer.add_input(x)
				computer.add_input(y)
				if x >= max_x:
					x, y = 0, y+1
				else:
					x += 1
			else:
				points += 1 if output else 0

		next_pos = (x, y)

	return points


print('Part 1', sweep((0,0), 50, 50))