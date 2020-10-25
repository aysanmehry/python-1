"""
def myFunction(number):
    return number*number

print(myFunction(10))

#----------------------

def moreArgument(*args):
    squared_args=[]
    for item in args:
        squared_args.append(item*item)
        return squared_args
    print(moreArgument(1,2,3,4))
#----------------------------------    
def person_details(**kwargs):
    for key, value in kwargs.items():
        print(key, '---->', value)
        
person_details(ame='aysan mehry' , Alias='elin', Jom='student

#------------------------
numbers=range(5)
def recursive_squares(numbers):
    if not numbers:
          return []
    else:
        return [numbers[0]*numbers[0]] + recursive_squares(numbers[1:])
print(recursive_squares(numbers))    
#-------------------------------------
lambda_square=lambda n: n*n
print(lambda_square(6)) 

#-----------------------------------------
numbers=range(9)
print(numbers)

print([num* num for num in numbers])
#------------------------------------------
"""
numbers=range(9)
numbers

print([num%2 for num in numbers])

print(set(num%2 for num in numbers))
print({num: num* num for num in numbers})

print([{'Number': num, 'square':num*num , 'type':'even' 
        if num%2==0 else 'odd'} for num in numbers])








            