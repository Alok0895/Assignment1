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
x=[-1,2]
print_value(x)
