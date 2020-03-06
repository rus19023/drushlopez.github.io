import replit

#-------------------------FUNCTIONS--------------------------

# Checks if you have entered only numbers
def tableValue(val):
  while(True):
    try:
      if(val == 'x'):
        x = input("Enter the x-values seperated by commas: ")
        x = x.replace(" ", "")
        x = x.split(",")
        x = [float(i) for i in x]
        return x
      elif(val == 'y'):
        y = input("Enter the y-values spereated by commas: ")
        y = y.replace(" ", "")
        y = y.split(",")
        y = [float(i) for i in y]
        return y
      else:
        decimal = input("Enter the amount of decimal points you would want to add: ")
        decimal = int(decimal)
        return decimal
    except:
      print("")
      print("Please enter numbers")
      print("")
      continue
    else:
      break

#Finds the mean of x and y
def mean(total, length):
  mean = total / length
  return mean

#Finds the Standard Deviation of x and y
def std(value, length, mean):
  diff = 0
  for i in range(length):
    diff += (value[i] - mean) ** 2
  try:
    variance = diff / (length - 1)
  except(ZeroDivisionError):
    return True
  stanDev = (variance) ** 0.5
  return stanDev

# Finds the coefficient of r
def r(x, y, meanX, meanY, length):
  sum1 = 0
  sum2 = 0
  sum3 = 0
  
  for i in range(length):
    sum1 += (float(x[i]) - meanX) * (float(y[i]) - meanY)
    sum2 += ((float(x[i]) - meanX) ** 2)
    sum3 += ((float(y[i]) - meanY) ** 2)
  
  #sum2Sqrt = sum2 ** 0.5
  #sum3Sqrt = sum3 ** 0.5
  r = sum1 / (sum2 * sum3) ** 0.5
  return r

# Squares r
def rSquared(r):
  squared = (r) ** 2
  return squared

#Finds b1
def b1(Sx, Sy, r):
  b1 = (r * Sy) / Sx
  
  return b1

#Finds b0
def b0(meanX, meanY, b1):
  b0 = meanY - b1 * meanX
  return b0

# Prints the predicted values
def predicted(x, roundb0, roundb1, deci, predict):
  print("Predicted Value:")
  for i in range(len(x)):
    mult = roundb0 + (roundb1 * float(x[i]))
    predict.append(round(mult, deci))
    print("x{}: {}".format(i+1, predict[i]))
    
  print("")

# Prints the residual values
def residual(x, y, predict, deci):
  print("Residual Value:")
    
  for i in range(len(x)):
    num1 = float(y[i])
    num2 = float(predict[i])
    sub = num1 - num2
    diff = round(sub,deci)
    print("x{}: {}".format(i+1, diff))

# Adds or removes x and y values
def addRem(x, y):
  decide = 0
  while(decide != 'a' and decide != 'b'):
    try:
      decide = input("Add (a) or remove (b) an x and y value: ").lower()
    except(ValueError):
      print("Please enter a or b")
      continue
  
  if(decide == 'a'):
    while(True):
      try:
        addX = input("Enter a number to add it to x-values: ")
        addX = float(addX)
        addY = input("Enter a number to add it to y-values: ")
        addY = float(addY)
      except(ValueError):
        print("Please enter only numbers")
        continue
      else:
        break
    x.append(addX)
    y.append(addY)
    
  elif(decide == 'b'):
    x = x.pop()
    y = y.pop()
    
    print("")
    print("Removed the last items")

# Plugs a number into the regression line equation and calculates it
def calc(b0, b1, deci):
  while(True):
    try:
      ins = input("Enter a number: ")
      ins = float(ins)
    except(ValueError):
      print
      print("Please insert a number")
      print("")
      continue
    else:
      break
  calculation = roundb0 + (roundb1 * ins)
  calculation = round(calculation, deci)
  print("")
  if(b1 > 0):
    print("{} + {}({}) = {}".format(roundb0, roundb1, ins, calculation))
  else:
    print("{} - {}({}) = {}".format(roundb0, abs(roundb1), ins, calculation))
  print("")

def info(meanX, meanY, sx, sy, co, rSqrd, slope, inter):
  # Speaks for itself
    print("")
    print("Mean of x: {}".format(meanX))
    print("Mean of y: {}".format(meanY))
    print("Sx: {}".format(sx))
    print("Sy: {}".format(sy))
    print("r: {}".format(co))
    print("r²: {}".format(rSqrd))
    print("b1: {}".format(slope))
    print("b0: {}".format(inter))

#----------------------------MAIN SCRIPT-----------------------------------

# Introduction
print("Made by Miguel Nunez.")
print("")
print("This calculator will give you mean and standard deviation of both x and y, r, b1, b0, the regression line equation, the predicted of each x value, and the residual of each x value")
print("In order to enter each term please add a commas inbetween each one")
print("")
print("EXAMPLE:")
print("x value: 19, 28, 14, 10")
print("y value: 47, 2, 57, 39")
print("")
print("")

t = True

while(True):
  
  # Checks to see if the x and y values are the same length
  while(True):
    x = 'x'
    y = 'y'
    decimal = None
    
    # Asks for the table (x and y) values
    x = tableValue(x)
    y = tableValue(y)
    decimal = tableValue(decimal)
    
    if(len(x) == len(y)):
      break
    
    else:
      print("")
      print("The x and y values are not the same length")
      print("")
      continue
  
  while(True):
    
    replit.clear()
    
    # Gets the sum of x and y
    totalX, totalY = sum(x), sum(y)
    
    # Gets the length of x and y
    lenX, lenY = len(x), len(y)
    
    # Mean of x and y
    meanX, meanY = mean(totalX, lenX), mean(totalY, lenY)
    
    # Gets the standard deviation of x and y
    sx, sy = std(x, lenX, meanX), std(y, lenY, meanY)
    
    # Tells the user that a number is being devided by 0
    if(sx == True):
      print("")
      print("The numbers you entered are dividing by 0 in the Standard Deviation and in r")
      print("")
      continue
    
    # Gets the corelation coefficient (r)
    co = r(x, y, meanX, meanY, lenX)
    
    # Gets the value of r squared and where the problem starts
    rSqrd = rSquared(co)
    
    # Gets the value of b1 and b0
    slope = b1(sx, sy, co)
    inter = b0(meanX, meanY, slope)
    
    # Rounds b1 and b0 to the number of decimals you wanted
    roundb1 = round(slope, decimal)
    roundb0 = round(inter, decimal)
    
    # This is to add values into the predicted value table
    predict =[]
    
    if(t == True):
      info(meanX, meanY, sx, sy, co, rSqrd, slope, inter)
    
    t = False
    
    while(True):
      
      # DOES NO UPDATE WHEN X AND Y VALUES ARE CHANGED
      print("")
      if(slope > 0):
        print("Regression line: y = {} + {}x".format(roundb0, roundb1))
      else:
        print("Regression line: y = {} - {}x".format(roundb0, abs(roundb1)))
      print("")
      
      # UPDATES WHEN X AND Y VALUES ARE CHANGED
      predicted(x, roundb0, roundb1, decimal, predict)
      residual(x, y, predict, decimal)
      
      print("-----------------------------")
      print("")
      
      ask = 0
      while(ask != 'a' and ask != 'b'):
        ask = input("Do you want to add / remove x and y value (a) or plug an x value to the regression line (b): ").lower()
      
      if(ask == 'a' or ask == 'A'):
        addRem(x, y)
        break
      if(ask == 'b' or ask == 'B'):
        calc(roundb0, roundb1, decimal)
        break
    
      