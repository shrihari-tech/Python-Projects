#FINDING THE LARGEST NUMBER IN LIST
listlen=int(input("Enter the List Size:"))
list=[]
maximum=0
count=0
#Loop
while (count<listlen):
    num=int(input("Enter a Number:"))
    list.append(num)
    count=count+1
#Displaying List
print(list)
maximum=list[0]
position=1
#Finding the Largest Number
while (position<listlen):
    if maximum<list[position]:
        maximum=list[position]
    position=position+1
#Displaying the Maximum Number
print("The Largest Number of List is:",maximum)

 

