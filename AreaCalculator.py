"""
The program should do the following:

Prompt the user to select a shape.
Calculate the area of that shape.
Print the area of that shape to the user.
"""
print "Starting the calculator..."
option = raw_input("Enter C for Circle or T for Triangle: ")

if option == "C":
  radius = float(raw_input("enter radius: "))
  area = 3.14 * radius**2
  print "Area %f" % area 
