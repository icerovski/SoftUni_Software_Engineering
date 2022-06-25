'''
You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. On the first line, you will receive a sequence of targets with their integer values, split by a single space.
Then, you will start receiving commands for manipulating the targets until the "End" command. The commands are the following:
•	"Shoot {index} {power}"
o	Shoot the target at the index if it exists by reducing its value by the given power (integer value). 
o	Remove the target if it is shot. A target is considered shot when its value reaches 0.
•	"Add {index} {value}"
o	Insert a target with the received value at the received index if it exists. 
o	If not, print: "Invalid placement!"
•	"Strike {index} {radius}"
o	Remove the target at the given index and the ones before and after it depending on the radius.
o	If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
 Example:  "Strike 2 2"
	{radius}	{radius}	{strikeIndex}	{radius}	{radius}		

•	"End"
o	Print the sequence with targets in the following format and end the program:
"{target1}|{target2}…|{targetn}"
Input / Constraints
•	On the first line, you will receive the sequence of targets – integer values [1-10000].
•	On the following lines, until the "End" will be receiving the command described above – strings.
•	There will never be a case when the "Strike" command would empty the whole sequence.
Output
•	Print the appropriate message in case of any command if necessary.
•	In the end, print the sequence of targets in the format described above.
'''

def shoot(index, power, sequence):
	if 0 <= index < len(sequence):
		sequence[index] -= power
		if sequence[index] <= 0:
			sequence.pop(index)
	return sequence

def add(index, value, sequence):
	if 0 <= index < len(sequence):
		return sequence.insert(index, value)
	print('Invalid placement!')

def strike(index, radius, sequence):
	if 0 <= index < len(sequence):
		if radius <= index < len(sequence) - radius:
			start = index - radius
			index_range = 2 * radius + 1
			result = list(filter(lambda i: sequence.pop(start), range(index_range)))
			return result
	print('Strike missed!')

def command_func(lst, sequence):
	index = int(lst[1])
	action = int(lst[2])
	if lst[0] == 'Shoot':
		result = shoot(index, action, sequence)
	elif lst[0] == 'Add':
		result = add(index, action, sequence)
	elif lst[0] == 'Strike':
		result = strike(index, action, sequence)
	return result


targets = list(map(int, input().split(' ')))
while True:
	command_str = input()
	if command_str == 'End':
		targets_str = list(map(str, targets))
		print('|'.join(targets_str))
		break

	command_func(command_str.split(' '), targets)

