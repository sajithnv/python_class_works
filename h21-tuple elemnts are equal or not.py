t=(10,10,10,20)
s=0
for i in t:
    if t[0]==i:
        s+=1
print(t)
print(f'there are {s} same elemets')
if len(t)==s:
    print('All elements are same')
else:
    print('not same')
        

