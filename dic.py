 
d1={'eggs':20, 'milk':3, 'spam':30, 'apple':15}
print(d1.get('milk'))
print(d1['eggs'])
d1['orange']=25
print(d1)
d2=dict({'girll':10, 'girl2':5})
d1.update(d2)
print('\n',d1)
d3={'k1':5, 'k2':[1,2,3,4], 'k3':{'a':1, 'b':2, 'c':[4,5,6]}}
print(d3.get('k3'))
print(d3.get('k3').get('c'))
