"""
class ANIMAL(object):
    species='Animal'
    
    def __init__(self, name):
        self.name=name
        self.attributes=[]
        
    def add_atrutesib(self, attributes):
        self.attributes.extend(attributes)
        if type(attributes)==list:
            pass
        else:
            self.attributes.append(attributes)
            
    def __str__(self):
         return self.name +"is type of" + self.species +"and has attributes:" + str(self.attributes)
     
a1=ANIMAL('zebra')
a1.add_atrutesib(['run', 'eats', 'wild'])     
print(str(a1))
"""
numbers=[1,2,3,4,5]
def generate_squares(numbers):
    for number in numbers:
        yield number * number
gen_obj=generate_squares(numbers)
gen_obj
for item in gen_obj:
    print(item)        