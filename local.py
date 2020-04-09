def change():
    global a                                                               
    a = 90   
    print(a) 
a = 9        
print("before the function call ", a)
print("inside change function ", end =' ')
change()     
print("after the function call ", a)

