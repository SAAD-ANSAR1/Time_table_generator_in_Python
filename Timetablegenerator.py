import numpy as np

#each hall has a time slot of 6 hours and each T is 2 hours long

def sett_population(co,b,d):
  c=[]
  counter=0
  #print(co)
  for i in range(len(co)):
    c.append(co[i]+","+b[np.random.randint(len(b))]+","+d[np.random.randint(len(d))])
    counter=counter+1
  return c

def fitness_function(pop,com):
  fitness=[] 
  counter=1
  for i in range(len(pop)):
    conflict = 0
    #counter=counter+1
    for j in range(len(pop)-counter):
      #if(j<4):
      #print(pop[i][6])
      if((pop[i][4]==pop[i+j+1][4]) and (pop[i][7]==pop[i+j+1][7])):
        conflict=conflict+1
        # print(pop[i] + " " + pop[i+j+1])

    for n in range(len(pop)):
       if(pop[i][7]==pop[n][7]):
        temp = pop[i][0:2]+','+pop[n][0:2]
        
        for k in range(len(com)):
          if(temp==com[k]):
            print("temp is : " + temp)
            # print("HEYYY")
            conflict = conflict+1 
    counter=counter+1
    fitness.append(conflict)
  return fitness

flag=True

def terminate_condition(pop,fit):
  f=[]
  counter = 0
  for i in range(len(fit)):
    if(fit[i]==0):  
      f.append(pop[i])
      counter=counter+1
  if(counter==5):
    flag=False        
  return f


course = ['C1','C2','C3','C4','C5']
halls = ['H1','H2']
times = ['T1','T2','T3']
common = ['C1,C2','C1,C4','C2,C5','C3,C4','C4,C5']
pop = sett_population(course,halls,times)
print(pop)
fit=fitness_function(pop,common)
print(fit)
succ = terminate_condition(pop,fit)
print(succ)
sc = 0 
while flag is True:
  for i in range(len(succ)):
   pop.remove(succ[i])
  print(pop)
  course=[]
  for i in range(len(pop)):
   course.append(pop[i][0:2])
  temppop=sett_population(course,halls,times)
  print(course)
  print(temppop)
  pop=succ+temppop
  print(pop)
  sc=sc+1
  fit = fitness_function(pop,common)
  print(fit)
  nut=[0,0,0,0,0]
  if(fit==nut):
      flag=False
  succ=terminate_condition(pop,fit)
print(succ)
print("fitness score = " + str(sc))