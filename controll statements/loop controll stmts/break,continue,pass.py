#break, continue,pass
for i in 'good morning':
    if i=='r':
        break
    print(i,end='')
print('\n__________________________________')
for i in 'good morning':
    if i=='r':
        continue
    print(i,end='')
print('\n__________________________________')
for i in [20,24,26]:
    pass
