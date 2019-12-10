'''input
3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
'''
import itertools
from collections import deque

OP_ADD = '01'
OP_MULT = '02'
OP_INPUT = '03'
OP_OUTPUT = '04'
OP_JMP_IF_TRUE = '05'
OP_JMP_IF_FALSE = '06'
OP_LESS = '07'
OP_EQ = '08'
OP_HALT = '99'

HALT = -1
OK = 0

def run_program(amplifier):

	def step():
		amplifier.ip = amplifier.ip+1
		return amplifier.ip

	def program_set(ip, value):
		amplifier.program[ip] = str(value)

	program_get_char = lambda ip: amplifier.program[ip]
	program_get_int = lambda ip: int(program_get_char(ip))
	program_get_addr = lambda ip: program_get_int(program_get_int(ip))
	get_input_value = lambda is_positional: program_get_addr(step()) if is_positional else program_get_int(step())

	while amplifier.ip < len(amplifier.program):
		op = program_get_char(amplifier.ip)

		tmp = list("{:05d}".format(int(op)))
		A,B,C,D,E = tmp
		op = D+E

		did_change_ip = False

		if op == OP_ADD or op == OP_MULT:
			op1 = get_input_value(C == '0')
			op2 = get_input_value(B == '0')
			out = program_get_int(step())
			result = op1 + op2 if op == OP_ADD else op1 * op2
			out_idx = out if A == '0' else amplifier.ip
			program_set(out_idx, str(result))

		elif op == OP_INPUT:
			out = program_get_int(step())
			out_idx = out if C == '0' else amplifier.ip
			program_set(out_idx, amplifier.inputs.popleft())

		elif op == OP_OUTPUT:
			op1 = get_input_value(C == '0')
			amplifier.output = int(op1)
			step()
			return OK

		elif op == OP_JMP_IF_TRUE or op == OP_JMP_IF_FALSE:
			op1 = get_input_value(C == '0')
			op2 = get_input_value(B == '0')
			result = op1 != 0 if op == OP_JMP_IF_TRUE else op1 == 0
			if result:
				amplifier.ip = op2
				did_change_ip = True

		elif op == OP_LESS or op == OP_EQ:
			op1 = get_input_value(C == '0')
			op2 = get_input_value(B == '0')
			out = program_get_int(step())
			is_true = op1 < op2 if op == OP_LESS else op1 == op2
			out_idx = out if A == '0' else amplifier.ip
			program_set(out_idx, '1' if is_true else '0')

		elif op == OP_HALT:
			return HALT

		if not did_change_ip:
			step()

	return HALT


program = input().split(',')

class Amplifier():
	def __init__(self, program):
		self.program = program
		self.inputs = deque()
		self.ip = 0
		self.output = None

	def add_input(self, input):
		self.inputs.append(input)
		return self

max_signal = 0
for perm in itertools.permutations([5,6,7,8,9]):
	a,b,c,d,e = map(str, perm)

	amplifiers = [Amplifier(list(program)) for _ in range(5)]

	amplifiers[0].add_input(a).add_input('0')
	amplifiers[1].add_input(b)
	amplifiers[2].add_input(c)
	amplifiers[3].add_input(d)
	amplifiers[4].add_input(e)

	while True:
		run_program(amplifiers[0])
		amplifiers[1].add_input(amplifiers[0].output)
		
		status = run_program(amplifiers[1])
		amplifiers[2].add_input(amplifiers[1].output)
		
		status = run_program(amplifiers[2])
		amplifiers[3].add_input(amplifiers[2].output)
		
		status = run_program(amplifiers[3])
		amplifiers[4].add_input(amplifiers[3].output)
		
		status = run_program(amplifiers[4])
		amplifiers[0].add_input(amplifiers[4].output)

		if status == HALT:
			break

	max_signal = max(max_signal, amplifiers[4].output)

print(max_signal)