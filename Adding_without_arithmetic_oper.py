#Python Program to add 2 numbers without using arithmatic operators

def add(a, b):
	#Iteration is continued till carry diminishes
	while (b!=0):
		#Carry containing common set bits in a and b
		carry = a & b
		a = a ^ b
		b = carry << 1 
		# carry gets shifted by one so that after adding it to a gives the required sum
	return a

def main():
	a = int(input("Enter the 1st number : "))
	b = int(input("Enter the 2nd number : "))
	print(f"Sum of {a} + {b} is ", int(add(a,b)))


main()

