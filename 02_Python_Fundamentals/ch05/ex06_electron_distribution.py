'''
You are a mad scientist, and you have decided to play with electron distribution among atom shells.
The basic idea of electron distribution is that electrons should fill a shell until it holds the maximum number of electrons.
You will receive a single integer - the number of electrons. Your task is to fill shells until there are no more electrons left.
The rules for electron distribution are as follows:
•	The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1). For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
•	You should start filling the shells from the first one at the first position.
•	If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and so on.
In the end, print a list with the filled shells.
'''

def fill_shell(electrons, shell):
    capacity = 2*(shell**2)
    return min(electrons, capacity)

remaining_electrons = int(input())
shell_counter = 0
filled_shells = []
while remaining_electrons > 0:
    shell_counter += 1

    current_electrons = fill_shell(remaining_electrons, shell_counter)
    filled_shells.append(current_electrons)
    remaining_electrons -= current_electrons

print(filled_shells)
