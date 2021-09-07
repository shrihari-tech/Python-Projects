start=1
end=int(input("Enter a Number:"))
# checking condition 
if end % 2 == 0:
    for  num in range(start,end+1):
         print(num, end = " ")
else:
        if end % 2 !=0:
            for num in range(start,end+2):
                    print(num, end =" ")  

      

