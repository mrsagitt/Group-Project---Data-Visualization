# program to find number of coins required to make a total amount

def main ():
	# enter the amount in euro
	amount = input("enter the amount in:")
	
	# conver the amount into cents
	cents = int(amount*100)
	
	# calculate the number of E2 coins required
	
	coins = int(cents/200)
	cents = int(cents%200)
	print " The number of  %3s coins is : %4d"%('E2',coins)
	
	# calculate the number of E1 coins required
	coins = cents/100
	cents = cents%100
	print " The number of  %3s coins is : %4d"%('E1',coins)
	
	# calculate the number of 50c coins required
	coins = cents/50
	cents = cents%50
	print " The number of %4s coins is : %4d"%('50C',coins)
	
	# calculate the number of 20c coins required
	coins = cents/20
	cents = cents%20
	print " The number of %4s coins is : %4d"%('20C',coins)
	
	# calculate the number of 10c coins required
	coins = cents/10
	cents = cents%10
	print " The number of %4s coins is : %4d"%('10C',coins)
	
	# calculate the number of 05c coins required
	coins = cents/5
	cents = cents%5
	print " The number of  %3s coins is : %4d"%('5C',coins)
	
	# calculate the number of 02c coins required
	coins = cents/2
	cents = cents%2
	print " The number of  %3s coins is : %4d"%('2C',coins)
	
	# calculate the number of 01c coins required
	coins = cents/1
	cents = cents%1
	print " The number of  %3s coins is : %4d"%('1C',coins)
	
main()



# Anotherway to write the same program


def main():
	import sys
	eurocents = [200,100,50,20,10,5,2,1]
	coinnames = ['2 Euro', '1 Euro', '50 Cent','20 Cent','10 Cent','5 Cent','2 Cent','1 Cent']
	
	# enter the amount in euro
	amount = input("enter the amount in:")
	
	# conver the amount into cents
	cents = int(amount*100)
	for index, i in enumerate(eurocents):
		coins = cents/i
		cents = cents%i
		print "The number of %-8s coins is : %3d" %(coinnames[index], coins)
main()
		
	
		
		
	
	
	
	
	
	