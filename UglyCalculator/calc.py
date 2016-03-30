def add (firstNumber, nextNumber):#Defines add function and variable to be used
	print "Adding %s + %s" % (firstNumber, nextNumber)#Displays summary of function
	return float(firstNumber + nextNumber) #performs the math of the function
	
def subtract (firstNumber, nextNumber):
	print "Subtract %s - %s" % (firstNumber, nextNumber)
	return float(firstNumber - nextNumber)
	
def multiply (firstNumber, nextNumber):
	print "Multiply %s * %s" % (firstNumber, nextNumber)
	return float(firstNumber * nextNumber)
	
def divide (firstNumber, nextNumber):
	print "Dividing %s / %s" % (firstNumber, nextNumber)
	return float(firstNumber / nextNumber)

#assigning necessary variables
firstNumber = float(raw_input("What is your first number?\n"))
againLoop = "Y"

while againLoop == "Y":
	function = str (raw_input( "Would you like to Add (+), Subtract (-), Multiply (*), or Divide (/)?\n"))
	nextNumber = float(raw_input("What is your next number?\n"))

#Logic test assessing user input and calls the appropriate function to be performed
	if function == "+":
		result = add (firstNumber, nextNumber)
		print "Result is: %s" % result
		firstNumber = result
		againLoop = str (raw_input("\nDo you nedd to perform more calculations on the result? (Y)es or (N)\n")).upper()
		

	elif function == "-":
		result = subtract (firstNumber, nextNumber)
		print "Result is: %s" % result
		firstNumber = result
		againLoop = str (raw_input("\nDo you nedd to perform more calculations on the result? (Y)es or (N)\n")).upper()

	elif function == "*":
		result = multiply (firstNumber, nextNumber)
		print "Result is: %s" % result
		firstNumber = result
		againLoop = str (raw_input("\nDo you nedd to perform more calculations on the result? (Y)es or (N)\n")).upper()
		
	elif function == "/":
		result = divide (firstNumber, nextNumber)
		print ("Result is: %s") % result
		firstNumber = result
		againLoop = str (raw_input("\nDo you nedd to perform more calculations on the result? (Y)es or (N)\n")).upper()
