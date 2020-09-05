import turtle as t
import pandas as pd
import numpy as np
import time
file = open(r"tour.txt")

tour=file.read().splitlines()
data = pd.read_excel(r"coordinates.xlsx")
cities = pd.DataFrame(data, columns=["Cities"])

def pull_coordinates(city):
    ind = cities[cities["Cities"]==city].index.values.astype(int)[0]
    print(city,"\t",ind)
    N = data.at[ind,'N']
    E = data.at[ind,'E']
    #print(N,E)
    return N, E



animation = True

height = 750
width  = 1515

#N_bottom = 34.6
N_bottom = 34.85
N_top       = 42.15
E_left       = 25.75
E_right     = 45

N_average = 0.5*(N_bottom + N_top)
E_average = 0.5*(E_left + E_right)
N_denominator = 0.5*(N_bottom - N_top)
E_denominator = 0.5*(E_left - E_right)
    
def get_coordinates(N, E):
    
    N_coor = -((N_average) - N)/(N_denominator)*(0-height/2)
    E_coor = -((E_average) - E)/(E_denominator)*(0-width/2)

    #print(N_coor, E_coor )
    return [E_coor, N_coor]

if animation ==True:

    
    screen = t.Screen()
    screen.setup(width, height)
    screen.bgpic("newbg2.png")
    screen.update()

    #time.sleep(10)
    loc = t.Turtle()
    loc.color('purple') #mediumvioletred
    loc.pensize(5)
    loc.hideturtle()           
    loc.penup()
    #loc.speed(2)

    N, E = pull_coordinates(tour[0])

    start = get_coordinates(N, E)
    loc.goto(start)
    loc.showturtle()
    loc.pendown()

    for i in range(1,len(tour)):
        loc.speed(int(np.random.uniform(1,4)))
        N, E = pull_coordinates(tour[i])
        next_c = get_coordinates(N, E)
        loc.goto(next_c)
        loc.write(i,align="center", font=("Arial", 32, "bold"))


    t.exitonclick()

