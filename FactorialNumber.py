#Factorial Of a Number
def Factorial(num):
    fact = 1
#Iteration of Loop  
    for i in range(1,num+1): 
        fact = fact * i 
      
    print ("The factorial of",num," is : ",end="") 
    print (fact)
