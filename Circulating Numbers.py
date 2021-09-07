'''no_of_terms = int(input("Enter number of values : "))
list1 = []
for val in range(0,no_of_terms,1):
    ele = int(input("Enter integer : "))
    list1.append(ele)

print("Circulating the elements of list ", list1)
   
for val in range(0,no_of_terms,1):
    ele = list1.pop(0)
    list1.append(ele)
    print(list1)'''
def Circulate(num1,num2,num3):
    num1,num2,num3=num3,num2,num1
    num3,num2,num1=num2,num1,num3
    num2,num1,num3=num2,num3,num1
    print(num1,num2,num3)
    print(num3,num2,num1)
    print(num2,num1,num3)
number1=1
number2=2
number3=3
Circulate(number1,number2,number3)
