
# importing the required module
import matplotlib.pyplot as plt
import math  
# x axis values
rate = 0.8
x = [i*1E-3 for i in range(int(1E3+1))]
# corresponding y axis values
amplitude = 1.01

def guaussian(x):
  squish_factor = (rate - 1) / math.log(0.5 * (1 - rate))
  return -amplitude * ( 2 * math.expm1((x-1)/squish_factor) + 1 ) 



y = list(map(guaussian, x))
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
plt.show()
