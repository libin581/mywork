#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-1,1,10)
y=x**2  
fig=plt.figure(figsize=(8,4))
ax=plt.subplot(111)
plt.plot(x,y)
for i,(_x,_y) in enumerate(zip(x,y)):
    plt.text(_x,_y,i,color='red',fontsize=i+10)
    plt.text(0.5,0.8,'subplot words',color='blue',ha='center',transform=ax.transAxes)
    plt.figtext(0.1,0.92,'figure words',color='green')
    plt.annotate('buttom',xy=(0,0),xytext=(0.2,0.2),arrowprops=dict(facecolor='blue', shrink=0.05))
    plt.show()
