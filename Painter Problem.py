#PAINTERS ARTHMETIC (GCD CALCULATION)
alice_houses=int(input("enter the number of house count of z-colony:"))
bob_houses=int(input("enter the number of house count of t-colony:"))
painting_wage_per_day_alex=int(input("enter the daily painting wage of alex:"))
painting_wage_per_day_bob=int(input("enter the daily painting wage of bob:"))
if alice_houses>bob_houses:
    largest_colony=alice_houses
    smallest_colony=bob_houses
else:
     smallest_colony=alice_houses
     largest_colony=bob_houses
remiander=largest_colony%smallest_colony
if remiander ==0:
     largest_colony= smallest_colony
     smallest_colony= largest_colony
remainder=largest_colony%smallest_colony
maximum_houses=smallest_colony
largest_colony=bob_house_count
alice_daily_wage=painting_wage_per_day_alex*maximum_houses
alice_painting_days=alice_houses/maximum_houses
alice_total_wages=alice_painting_days*alice_daily_wage
print("total wages of alice:",alice_total_wages)
bob_daily_wage=painting_wage_per_day_bob*maximum_houses
bob_painting_days=bob_house_count/maximum_houses
bob_total_wages=bob_painting_days*bob_daily_wage
print("total wages of bob:",bob_total_wages)
    
    
    
          
