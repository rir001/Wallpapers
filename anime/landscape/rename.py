import os


get_cont = lambda num: '0'*(3-len(str(num))) + str(num)

cont = 1
for entry in os.scandir('.'):
    if entry.is_file() and entry.name != 'rename.py':
        try:
            os.rename(entry.name, get_cont(cont)+'.jpg')
            cont += 1
        except:
            pass