mylist=[1,2,99.5,[44,444],"hello"]
print(mylist)

print(len(mylist))
print(mylist[4])
print(mylist[2:4])

for item in mylist:
    print(item)
    
print(mylist[3] [1])
print(mylist[3] [0])
#------------------------------------------
    
mylist2=[3,2,99.5,[44,444],"student"]
mylist2.append(99)
mylist2.insert(0,"hello")
print(mylist2)

mylist2.remove(99)
del(mylist2[0])
print(mylist2)

#------------------------------------------

mylist3=[3,2,99.5,[44,444],"student"]
print(mylist3)
mylist3.append(mylist3)
print(mylist3[5][5])

#---------------------------------------------

mylist4=[3,2,99.6,7,1,10]
mylist4.sort()
print(mylist4)
mylist4.reverse()
print(mylist4)