#FILE HANDLING
file=open("Python.txt",'r')
text=file.read()
text=text.split()
print(text)
frequent={}
#SPLITING THE WORDS
for word in text:
    if word not in frequent:
        frequent[word]=1
    else:
        frequent[word]+=1
print(frequent)
maximum=0
#FINDING THE MAXMUM NUMBER OF REPEATED WORDS
for each in frequent.keys():
    if maximum<frequent[each]:
        maximum=frequent[each]
        word=each
print("The Word %s Returns %d Number of Times"%(word,maximum))        
