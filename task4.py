n = int(input())
x = 0
y = 0
for i in range(n):
    commands = input()
    if commands.split(' ')[0] == 'север':
        x += int(commands.split(' ')[1])
    elif commands.split(' ')[0] == 'восток':
        y += int(commands.split(' ')[1])
    elif commands.split(' ')[0] == 'юг':
        x -= int(commands.split(' ')[1])
    else:
        y -= int(commands.split(' ')[1])
print(y, x)
