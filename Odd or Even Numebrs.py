#TO CHECK THE BETWEEN NUMBERS OF ODD OR EVEN NUMBERS

start=1
end=int(input("Enter a Number:"))
  
# iterating each number in list 
for num in range(start, end + 1): 
      
# checking condition 
    if num % 2 == 0: 
        print(num, end = " ")
    elif num % 2 != 1:
          print(num, end =" ")
