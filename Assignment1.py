import numpy as np
import matplotlib.pyplot as plt
def print_value(x) :
  #slope of the line @ origin
    m_origin = x[1]/x[0]
  #slope of the required line
    m_line = -1/m_origin
  #required constant of the line
    c_line = x[1]-m_line*x[0]
  #presenting the value of slope and constant
    print("the slope of the m_line is ",m_line)
    print("the value of c in the line ",c_line)
    point1=[0,0]
    point2=[-1,2]
    x_values = [point1[0], point2[0]]
#gather x-values
    y_values = [point1[1], point2[1]]
#gather y-values
   
   
    plt.xlim(-6,6)
    plt.ylim(-6,6)
    plt.plot(x_values, y_values)
    x = np.linspace(-10,10,50)
    y = (m_line*x) + c_line
    print(c_line)
    plt.plot(x, y, '-r')
    plt.plot(-1,2, 'ro')
    plt.plot(0,0, 'ro')
  

    plt.grid()
    
    plt.show()
z=[-1,2]
print_value(z)
