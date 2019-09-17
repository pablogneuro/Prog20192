''' import numpy as np  

a = np. array ([20, 30,40, 50])
b = np. arange (4)
print(a) 
print (b)


import numpy as np  

pallete = np.array ([[0,0, 0],
                    [255,0,0],
                    [0,255,0],
                    [0, 0, 255],
                    [255, 255,255]])
image = np. array ([ [0,1,2,0],
                    [0,3,4,0]])

print(pallete[image])

import numpy as np

a = np. arange (12).reshape (3,4)
b = a > 4
print (b)


import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

t = np.arange(0.0, 2.0, 0.01)

s = 1 + np.sin (2* np. pi * t)
fig, ax = plt.subplots ()
ax.plot(t,s)
plt.show()

import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

t = np.arange(0.0, 5.0, 0.01)

fig,ax = plt.subplots(2,2)

ax [0,0].plot(np.sin(2* np.pi * t)*np.exp(-0,5 *t))
ax [0,0].set_title("vibração atenuada", fontsize = 10)

ax [0,1].plot(np.sin(2* np.pi * t)*np.log(0,5 *t))
ax [0,1].set_title("vibração LOG", fontsize = 10)

ax [1,0].plot(np.sin(2* np.pi * t)*np.cos(-0,5 *t))
ax [1,0].set_title("vibração COS", fontsize = 10)

ax [1,1].plot(np.sin(2* np.pi * t)*np.tan(-0,5 *t))
ax [1,1].set_title("vibração taN", fontsize = 10)

plt.show()
'''



import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

N= 5
mediaHomens = (20,35, 30, 35, 27)
mediaMulheres = (25,32, 34,36,17) 
desvpadHomens = (2, 4,3,4,1)
desvpadMulheres = (2,3,5,2,1,)

ind = np.arange (N)
width = 0.35

p1=plt.bar(ind, mediaHomens, width, yearr = desvpadHomens)
p2=plt.bar(ind, mediaMulheres, width, yearr = desvpadMulheres)


plt.ylabel("Pontuaçao")
plt.title ("Pontuaçao por grupo de genero")
plt.xticks(ind, ('G1', 'G2', 'G3','G4' ,'G5'))
plt.yticks(np.arange(0,81,10))
plt.legend((p1[0],p2 [0]), ('Homens','Mulheres'))

plt.show()
