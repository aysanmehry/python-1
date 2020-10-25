"""
var='spem'
if var=='spam':
    print('spam')
var2='girl'
if var2=='girl':
    print("Girl")
elif var=='boy':
    print("Boy") 
else:
    print("hello")    

#------------------------
numbers=range(0,10)
for number in numbers:
  if number<3:
      print(number)
  else:
      break
else:
    print("Loop exited normally")
#-------------------------
number=5
while number>0:
    print(number)
    number-=
#-------------------------    

shopinglist=['eggs','ham','bacon']
try:
    print(shopinglist[3])
except IndexError as e:
    print('Exception:' + str(e) + 'has occured')
else:
    print('no Exceptions occured')
finally:
    print('I will always execute no matter what')    
#----------------------------------
"""   
shopinglist=['eggs','ham','bacon']
try:
    print(shopinglist[2])
except IndexError as e:
    print('Exception:' + str(e) + 'has occured')
else:
    print('no Exceptions occured')
finally:
    print('I will always execute no matter what')        
    
    
    
    
    