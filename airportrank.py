import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv

#info

airports  = []
passengernum = []

##reads from the csv file
import csv
with open('airports.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        airports.append(lines[0])
        strvar = (lines[1].replace(',', ''))
        numvar = int(strvar)
        passengernum.append(numvar)
        print(lines)

print(airports)
print(passengernum)

##create dictionary
font = {'size': 10}

##font for plot 
plt.rc('font', **font)

#plotting graph
plt.bar(airports, passengernum)
plt.title('Busiest airports of 2024')
plt.xlabel('Airport name')
plt.ylabel('Passenger Numbers')

##initialize y limit
plt.ylim(0,150000000)

#display graph
plt.show()
