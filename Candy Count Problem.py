#CANDY COUNT PROBLEM
money=int(input("Enter How Much Money did Ryan had :"))
candy=money/0.25
print("Ryan had got",candy,"Candy by using Money")
wrapper=candy/3
print("Ryan had got",wrapper,"wrappers")
total=wrapper+candy%3
print("Ryan Has",total,"Candyes")
result=total+candy
print("Finally Ryan had got",result,"Candyes")
