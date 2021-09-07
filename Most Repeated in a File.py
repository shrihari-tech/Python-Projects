#FILE HANDELLING
file=open("Python.txt",'r')
text=file.read()
text=text.upper()
text=text.split()
print(text)
frequent={}
#SPLITING OF WORDS
for word in text:
    if word not in frequent:
        frequent[word]=1
    else:
        frequent[word]+=1
print("\n\n",frequent)        
#FINDING THE REPEATED STI=RING IN THE TEXT
maximum=0
for each_word in frequent.keys():
    if maximum<frequent[each_word]:
        maximum=frequent[each_word]
        word=each_word
print("\n\nThe Word",word,"Returns",maximum,"Number of Times")        
