#!/usr/bin/env python
import glob, os, time
import urllib.request
import bitcoin

addresses = []
balances = []

	
def loadAddress():
	file = os.path.dirname(os.path.realpath(__file__)) + "/inc/bitcoin-address.txt"
	with open(file) as fp:
		for line in fp:
			addresses.append(line.replace("\n",""))

def main():
	# Load addresses
	loadAddress()

	# Check balance of each address
	print("Address\t:\tBalance (Satoshi)\t:\tBTC\t:\tUSD")
	for x in addresses:
		balance = bitcoin.checkBalance(x)
		balances.append(balance)
		print(x + "\t:\t%.d\t:\t%.d\t:\t%.d" % (balance,bitcoin.SatoshiToBTC(balance),bitcoin.price(bitcoin.SatoshiToBTC(balance))))
		time.sleep(1)
	
	wallet = dict(zip(addresses, balances))
	#print(wallet)

if __name__ == '__main__':
	main()