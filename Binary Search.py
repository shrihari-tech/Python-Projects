#BINARY SEARCH
email=["ajeetha.r2020@kgkite.ac.in","akash.s2020@kgkite.ac.in","akasthiyan.r2020@kgkite.ac.in","anishkumar.a2020@kgkite.ac.in","anisha.s2020@kgkite.ac.in",
       "aruna.g2020@kgkite.ac.in","balaji.v2020@kgkite.ac.in","daniel.at2020@kgkite.ac.in","danush.s2020@kgkite.ac.in","ganesh.s2020@kgkite.ac.in","deeksha.d2020@kgkite.ac.in","gayathri.p2020@kgkite.ac.in",
       "gayathri.s2020@kgkite.ac.in","govarthini.p2020@kgkite.ac.in","hamasavrdhini.k2020@kgkite.ac.in","harikrishnan.t2020@kgkite.ac.in","harisankar.b2020@kgkite.ac.in","harithamonshe.e2020@kgkite.ac.in","kanishka.p2020@kgkite.ac.in",
       "kanithra.p2020@kgkite.ac.in","kathirvelan.a2020@kgkite.ac.in","keerthana.r2020@kgkite.ac.in","lokeshkumar.l2020@kgkite.ac.in","madhusuriya.s2020@kgkite.ac.in","manikandan.r2020@kgkite.ac.in","meghasari.r2020@kgkite.ac.in","miruthubashini.a2020@kgkite.ac.in",
       "muraliprasath.a2020@kgkite.ac.in","narmatha.d2020@kgkite.ac.in","naveen.r2020@kgkite.ac.in","navin.m2020@kgkite.ac.in","niranjana.k2020@kgkite.ac.in","nowsathbegam.m2020@kgkite.ac.in","pavithran.r2020@kgkite.ac.in","ponezhil.r2020@kgkite.ac.in","prathap.r2020@kgkite.ac.in",
       "priyadharshini.g2020@kgkite.ac.in","rashikaroshini.r2020@kgkite.ac.in","rithika.m2020@kgkite.ac.in","sadhana.r2020@kgkite.ac.in","sandeep.r2020@kgkite.ac.in","sangamithraa.v2020@kgkite.ac.in","sanjana.r2020@kgkite.ac.in","santhiya.k2020@kgkite.ac.in","shalini.s2020@kgkite.ac.in",
       "shrihari.b2020@kgkite.ac.in","sridharan.s2020@kgkite.ac.in","subasini.j2020@kgkite.ac.in","suruthi.d2020@kgkite.ac.in","swedha.m2020@kgkite.ac.in","swethapalpandian2020@kgkite.ac.in","thejaskumar.b2020@kgkite.ac.in","uditpranav.s2020@kgkite.ac.in","yuvasri.s2020@kgkite.ac.in"]
length=len(email)
print(length)
#email.sort()
#print(email)
ID=input("Enter the Student Email ID:")
def student(ID):
    index0=0
    indexl=length-1
#Iteration of Loop    
    while index0<indexl:
        index=(index0+indexl)//2
        if ID==email[index]:
            print("The Student Belongs to IT Department")
            break
        elif ID<email[index]:
            indexl=index-1
        elif ID>email[index]:
            index0=index+1
    else:
            print("The Student Does not Belongs to IT Department")
        
            
student(ID)

