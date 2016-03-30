from sys import argv

#Assigning necessary variables
scripts, fileName = argv
nUmerator = int (raw_input ("What is your Numerator?: "))
dEnominator = int (raw_input ("What is your Denominator?: "))

#This reads in the list of primes, convert to integer for use in calc.
#Current limit from file is 16384 values of Prime, upto 180503. Working!
with open (fileName) as primes:
	primeL = primes.read()
	primeNumbers = primeL.split(',')
	allPrimes = [int(eachPrime) for eachPrime in primeNumbers]

#oddReduce goes through allPrimes to reduce. Working!
def primeReduce (nUmerator, dEnominator, allPrimes):
	for eachPrime in allPrimes:
		while (nUmerator % eachPrime == 0) and (dEnominator % eachPrime == 0):
			nUmerator /= eachPrime
			dEnominator /= eachPrime
	print ("%d / %d") % (nUmerator, dEnominator)
	return nUmerator, dEnominator

primeReduce(nUmerator,dEnominator, allPrimes)
