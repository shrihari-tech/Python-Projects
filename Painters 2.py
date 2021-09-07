#PAINTERS ARTHMETIC (GCD CALCULATION)

#initilize 
alice_houses=int(input("Enter Alice House Count of a Colony:"))
bob_houses=int(input("Enter Bob House Count of a Colony:"))

#Providing Wages
painting_wage_per_day_alice=int(input("Enter the daily  Wages of Alice:"))
painting_wage_per_day_bob=int(input("Enter the daily Wage of Bob:"))

#Largest Colony Checking Condition
if alice_houses>bob_houses:
    largest_colony=alice_houses
    smallest_colony=bob_houses
else:
     smallest_colony=alice_houses 
     largest_colony=bob_houses
balance=largest_colony%smallest_colony
if balance ==0:
     largest_colony= smallest_colony
     smallest_colony= largest_colony
balance=largest_colony%smallest_colony
maximum_houses=smallest_colony
largest_colony=bob_houses

#Final Setelment of Alice
alice_daily_wage=painting_wage_per_day_alice*maximum_houses
alice_painting_days=alice_houses/maximum_houses
alice_total_wages=alice_painting_days*alice_daily_wage
print("Total Wages of Alice:",alice_total_wages)

#Final Setelment of Bob
bob_daily_wage=painting_wage_per_day_bob*maximum_houses
bob_painting_days=bob_houses/maximum_houses
bob_total_wages=bob_painting_days*bob_daily_wage
print("Total Wages of Bob:",bob_total_wages)
