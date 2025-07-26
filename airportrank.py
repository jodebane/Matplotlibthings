import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



#info

airports  = ['ATL', 'DXB', 'DFW', 'HND', 'LHR', 'DEN', 'ORD', 'IST', 'DEL', 'PVG']
passengernum = [108, 92, 88, 85, 84, 82, 80, 80, 78, 77]


#plotting graph
plt.bar(airports, passengernum)
plt.title('Busiest airports of 2024')
plt.xlabel('Airport code')
plt.ylabel('Passenger Numbers in millions (rounded to nearest)')

#display graph
plt.show()
