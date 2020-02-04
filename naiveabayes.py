import csv
import numpy as np
tot =[]
with open(r"C:\Users\SCC\PycharmProjects\rumorDetection\AI assignment\hu.csv","r") as c1:
    e = csv.reader(c1)

    for lines in e:
        #print(lines)
        if len(lines)>0:
          tot.append(lines)

yes =0
no =0
for i in range(len(tot)):
    if tot[i][4] == 'yes':
       yes+=1

    if tot[i][4] == 'no':
       no+=1


total= len(tot)-1

p_yes = yes/total
p_no = no/total

#print(p_yes)
#print(p_no)
'''
X = (age <=30, 
Income = medium
,
Student = yes
Credit_rating = fair)
'''



X = []
print("enter data for prediction: ")
for i in range(4):

  c = input()
  X.append(c)

#print(X)

p_x_yes_temp =[]
p_x_no_temp =[]

temp =[]

for i in range(len(tot)):


    for i1 in range(len(X)):


        if tot[i][4] == 'yes':
            if X[i1]==tot[i][i1]:
              #print(tot[i][4]+'  '+ tot[i][i1])
              temp.append(tot[i][4]+'  '+ tot[i][i1])

        elif tot[i][4] == 'no':
            if X[i1]==tot[i][i1]:
              #print(tot[i][4]+'  '+ tot[i][i1])
              temp.append(tot[i][4] + '  ' + tot[i][i1])


#print(temp)

t1= []
t2 = []
for i in range(len(temp)):

         if temp[i].find("yes")==0:
             t1.append(temp[i])

         if temp[i].find("no")==0:
             t2.append(temp[i])


for i in X:
    c1=0
    for g in range(len(t1)):
        r= t1[g]
        r1 =r[2:]
        if r1.find(i)!=-1:
          c1+=1

    p_x_yes_temp.append(c1/yes)


for i1 in X:
    c2=0
    for g1 in range(len(t2)):
        r= t2[g1]
        r1 =r[2:]
        if r1.find(i1)!=-1:
          c2+=1

    p_x_no_temp.append(c2/no)


#print(p_x_yes_temp)
#print(p_x_no_temp)


p_x_yes = np.array(p_x_yes_temp).prod() * p_yes
p_x_no =  np.array(p_x_no_temp).prod() * p_no
print(p_x_yes)
print(p_x_no)

if p_x_yes> p_x_no:
    print("yes!!")
else:
 print("no!")
















