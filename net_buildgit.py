from triangulatedgit import triangulated
import numpy as np
import matplotlib.pyplot as plt
import algorithmsgit as alg

population = int(input('Number of nodes = '))
net = triangulated(population)
print('Number of created nodes = ',len(net.nodes))
neighbors = []
for i in net.nodes:
	neighbors.append(len(i.neighbors))

neighbors = np.asarray(neighbors)
y = np.bincount(neighbors)

y = y/population
print('pdf of neighbors:',y)

fig, ax = plt.subplots()

ax.plot( y)
plt.title('pdf of neighbors')
plt.xlabel('number of neighbors')
plt.ylabel('probability')
plt.show()

print(alg.is_triangulated(net))
