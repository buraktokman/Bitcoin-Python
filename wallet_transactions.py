#!/usr/bin/env python
import bitcoin, sys

if len(sys.argv) < 2:
	ADDRESS = "17hf5H8D6Yc4B7zHEg3orAtKn7Jhme7Adx"
elif len(sys.argv) < 3:
	ADDRESS = sys.argv[1]
else:
	print('Wallet address must be provided.')

def main():
	#bitcoin.allTransactions(ADDRESS)
	bitcoin.simpleTransactions(ADDRESS)
	
if __name__ == '__main__':
	main()