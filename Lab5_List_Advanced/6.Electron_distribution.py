num_electrons = int(input())
initial_num = num_electrons
n = 1
shell = []
while not initial_num == sum(shell):
    single_shell = 2*(n**2)
    if num_electrons < single_shell:
        shell.append(num_electrons)
        break
    shell.append(single_shell)
    num_electrons -= single_shell
    n += 1


print(shell)
