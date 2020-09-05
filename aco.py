import numpy as np
import random
import matplotlib.pyplot as plt

cities = ["Mugla", "Bursa", "Ankara", "Gaziantep",
          "Diyarbakir", "Hatay", "Adiyaman", "Kocaeli",
          "Istanbul", "Eskisehir"]

distances=np.array([[np.inf,543,619,1058,1371,1037,1181,671,782,499],
		   [543,np.inf,385,1026,1272,1033,1114,132,243,152],
		   [619,385,np.inf,655,901,683,742,342,453,233],
		   [1058,1026,655,np.inf,313,193,150,1000,1111,874],
		   [1371,1272,901,313,np.inf,506,207,1246,1357,1121],
		   [1037,1033,683,193,506,np.inf,316,1028,1139,881],
		   [1181,1114,742,150,207,316,np.inf,1087,1198,962],
		   [671,132,342,1000,1246,1028,1087,np.inf,111,214],
		   [782,243,453,1111,1357,1139,1198,111,np.inf,325],
		   [499,152,233,874,1121,881,962,214,324,np.inf]])

pheromone = np.ones((len(distances),len(distances)))
eta = 1/distances

best_distance = np.inf

evaporation_rate = 0.1
r_damp = 1
Q = 1
alfa = 1
beta = 1

nAnts  = 20
nIter = 100

best_array = []


for _ in range(nIter):
    for ant in range(nAnts):
        
        visited = []
        
        unvisited = list(range(0,len(cities)))
    
        start = cities.index("Mugla")
        
        visited.append(start)
        unvisited.remove(start)
        
        tour = [start]
        
        current_city = start
        
        distance = 0
        
        for i in range(len(cities)-1):
            
            # Probability Calculation
            probability_denominator = sum((pheromone[current_city][j]**alfa)*(eta[current_city][j]**beta) for j in unvisited)
            probability = []
            for j in unvisited:
                probability_nominator = (pheromone[current_city][j]**alfa)*(eta[current_city][j]**beta)
                P = probability_nominator/probability_denominator
                probability.append(P)
            # print(probability, sum(probability))
            
            # Roulette Wheel
            rand = random.uniform(0,1)
            # cumulative sum
            roulette = []
            cumulative_sum = 0
            for r in range(0,len(probability)):
                cumulative_sum+=probability[r]
                roulette.append(cumulative_sum)
            # print(roulette)
                
            for wheel in roulette:
                # print(rand,wheel)
                if rand <= wheel:
                    index = roulette.index(wheel)
                    # print(index)
                    break
            
            
            # next_city = random.choice(unvisited)
            next_city = unvisited[index]
            visited.append(next_city)
            unvisited.remove(next_city)
            distance += distances[current_city][next_city]
            current_city = next_city
        
        distance += distances[current_city][start] 
        visited.append(start)

        # Pheromone Update
        for a in range(len(tour)-1):
            pheromone[tour[a]][tour[a+1]] = pheromone[tour[a]][tour[a+1]]+Q/distance
        
        evaporation_rate*=r_damp
        pheromone = (1-evaporation_rate)*pheromone
        
        if distance < best_distance:
            best_distance = distance
            best_tour = visited
            
        
                
    
    best_array.append(best_distance)
            
 
best_tour_cities = []
for name in best_tour:
    best_tour_cities.append(cities[name])
    
    
    
#%%%%%%%%%%%%% PLOT THE RESULTS %%%%%%%%%%%%%

x = np.arange(1,nIter+1)
y = best_array

plt.plot(x,y)
plt.xlabel("Iteration")
plt.ylabel("Best Ant")
plt.title("Travelling Salesman Problem")
plt.show()
plt.savefig('aco.png')

file1 = open("tour.txt","w")#write mode 
for i in range(len(best_tour_cities)):
    file1.write(best_tour_cities[i]+"\n")
file1.close() 

print("Parameters;",
      "\nEvaporation Rate: ", evaporation_rate,
      "\nBeta: ", 1,
      "\nAlfa: ", 1,
      "\nNumber of Ants: ",nAnts,
      "\nNumber of Iteration: ",nIter)
















