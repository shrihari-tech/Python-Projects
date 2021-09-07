#MULTIPLAY MATRIX
alist=[[3,5,2,1],
       [4,6,9,2],
       [9,7,5,3]]
blist=[[6,9,2,6],
       [8,6,1,3],
       [9,6,5,3]]
result=[]
#ITERATION FOR A ROW
for i in range(3):
    empty=[]
#ITERATION FOR A COLOUMN    
    for j in range(3):
        sumM=0
#ITERATION FOR ONE MULTIPLICATION AND ADDITION OF ROW AND COLUMN        
        for x in range(3):
            sumM=sumM+alist[i][x]*blist[x][j]

        empty.append(sumM)
    result.append(empty)
#DISPLAYING THE OUTPUT    
for number in result:
    print(number)
