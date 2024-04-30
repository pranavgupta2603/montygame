import numpy as np
from add_data import add_data
import pandas as pd
def monty_hall(num_doors):
    stay_wins = 0
    switch_wins = 0
    stay_loses = 0
    switch_loses = 0
    doors = [0] * (num_doors-1)
    doors.append(1)
    np.random.shuffle(doors)
    print(doors)
    choice = np.random.randint(num_doors)
    print("I choose: " + str(choice))
    host_opens = np.random.choice([i for i in range(num_doors) if i != choice and doors[i] == 0])
    print("Host opens door: " + str(host_opens))
    
    switch = np.random.randint(2)
    print("Do you want to switch: " + str(switch))
    if switch:
        print("You switched doors!")
        new_door = np.random.choice([i for i in range(num_doors) if i != choice and i != host_opens])
        print("You chose: " + str(new_door))
        if doors[new_door] == 1:
            print("You won!")
            switch_wins += 1
        else:
            print("You lost even though you switched!")
            switch_loses += 1
    else:
        print("You stayed with your original choice!")
        if doors[choice] == 1:
            print("You won!")
            stay_wins += 1
        else:
            print("You lost! You should have switched doors!")
            stay_loses += 1
    results = [stay_wins, switch_wins, stay_loses, switch_loses]
    return results



num_doors = 500
for i in range(10000):
    df = pd.read_csv('data.csv')
    results = list(monty_hall(num_doors))
    result_column = df.columns[2:][results.index(1)]
    add_data(df, num_doors, result_column)

data_to_use = list(df[df['num_doors'] == num_doors].values[0])

print("For " + str(num_doors) + " doors:") 
print("The number of times the game has been played is:", int(data_to_use[1]))

print("The number of times you won when you stayed: " + str(data_to_use[2]))

print("The number of times you lost when you stayed: "+ str(data_to_use[4]))

print("The number of times you won when you switched: " + str(data_to_use[3]))

print("The number of times you lost when you switched: "+ str(data_to_use[5]))

print("Percentage Win when stayed: " + str(data_to_use[2]/(data_to_use[2]+data_to_use[4]) * 100))
print("Percentage Win when switched: " + str(data_to_use[3]/(data_to_use[3]+data_to_use[5]) * 100))