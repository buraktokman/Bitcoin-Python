#!/usr/bin/env python
import glob, os, time, json, datetime
import urllib.request
from pprint import pprint

def convertTime(time):
	return datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')

def price(balance):
	web = urllib.request.urlopen("https://blockchain.info/tobtc?currency=USD&value=1").read()
	rate = float(web)
	price = ( 1 / rate ) * balance
	return price

def SatoshiToBTC(balance):
	balance  = balance / 100000000.0
	return(balance)

def checkBalance(address):
	try:
		web = urllib.request.urlopen("https://blockchain.info/q/addressbalance/" + address).read()
		return int(web)
	except Exception as e:
		web = 0
		print("Connection Error")

def checkBalance(address):
	try:
		web = urllib.request.urlopen("https://blockchain.info/q/addressbalance/" + address).read()
		return int(web)
	except Exception as e:
		web = 0
		print("Connection Error")

def singleAddress(address):
	try:
		with urllib.request.urlopen("https://blockchain.info/balance?active=" + address) as url:
   			data = json.loads(url.read().decode())
	except Exception as e:
		print("Connection Error")

	print("Address: " + address)
	print("Final balance: " + str(SatoshiToBTC(data.get(address).get('final_balance'))))
	print("Equivalent as USD: " + str(price(SatoshiToBTC(data.get(address).get('final_balance')))))
	print("Total received: " + str(SatoshiToBTC(data.get(address).get('total_received'))))
	print("Number of transactions: " + str(data.get(address).get('n_tx')))

def allTransactions(address):
	with urllib.request.urlopen("https://blockchain.info/rawaddr/" + address) as url:
   		data = json.loads(url.read().decode())

	#pprint(data)
	#pprint(data['txs'][0])

	print("address: " + data['address'])
	print("final balance: " + str(data['final_balance']))
	print("hash160: " + data['hash160'])
	print("n_tx: " + str(data['n_tx']))
	print("total_received: " + str(data['total_received']))
	print("total_sent: " + str(data['total_sent']))

	for x in range(0,len(data['txs'])):
		print("# --------- TX : " + str(x)  + " -------")
		print("block height: " + str(data['txs'][x]['block_height']))
		print("hash: " + data['txs'][x]['hash'])
		print("lock time: " + str(data['txs'][x]['lock_time']))
		print("relayed by: " + str(data['txs'][x]['relayed_by']))
		print("size: " + str(data['txs'][x]['size']))
		print("time: " + str(data['txs'][x]['time']))
		print("tx index: " + str(data['txs'][x]['tx_index']))
		print("ver: " + str(data['txs'][x]['ver']))
		print("vin sz: " + str(data['txs'][x]['vin_sz']))
		print("vout sz: " + str(data['txs'][x]['vout_sz']))
		print("weight: " + str(data['txs'][x]['weight']))
	
		#print("inputs: " + str(data['txs'][x]['inputs']))
		for y in range(0,len(data['txs'][x]['inputs'])):
			print("# --------- RECEIVED : " + str(y) + " -------")
			print("sequence: " + str(data['txs'][x]['inputs'][y].get('sequence')))
			print("witness: " + data['txs'][x]['inputs'][y].get('witness'))

			#print("prev out: " + str(data['txs'][0]['inputs'][0].get('prev_out')))
			print("spent: " + str(data['txs'][x]['inputs'][y].get('prev_out').get('spent')))
			print("tx index: " + str(data['txs'][x]['inputs'][y].get('prev_out').get('tx_index')))
			print("type: " + str(data['txs'][x]['inputs'][y].get('prev_out').get('type')))
			print("addr: " + str(data['txs'][x]['inputs'][y].get('prev_out').get('addr')))
			print("value: " + str(data['txs'][x]['inputs'][y].get('prev_out').get('value')))
			print("n: " + str(data['txs'][x]['inputs'][y].get('prev_out').get('n')))
			print("script: " + str(data['txs'][x]['inputs'][y].get('prev_out').get('script')))

		#print("out: " + str(data['txs'][0]['out']))
		for z in range(0,len(data['txs'][x]['out'])):
			print("# --------- SENT : " + str(z) + " -------")
			print("spent: " + str(data['txs'][x]['out'][z].get('spent')))
			print("tx index: " + str(data['txs'][x]['out'][z].get('tx_index')))
			print("type: " + str(data['txs'][x]['out'][z].get('type')))
			print("addr: " + data['txs'][x]['out'][z].get('addr'))
			print("value: " + str(data['txs'][x]['out'][z].get('value')))
			print("n: " + str(data['txs'][x]['out'][z].get('n')))
			print("script: " + data['txs'][x]['out'][z].get('script'))

def simpleTransactions(address):
	with urllib.request.urlopen("https://blockchain.info/rawaddr/" + address) as url:
   		data = json.loads(url.read().decode())

	print("Address: " + data['address'])
	print("Final Balance: " + str(SatoshiToBTC(data['final_balance'])))
	print("Transaction count: " + str(data['n_tx']))
	print("Total Bitcoins Received: " + str(SatoshiToBTC(data['total_received'])))
	print("Total Bitcoins Sent: " + str(SatoshiToBTC(data['total_sent'])))

	for x in range(0,len(data['txs'])):
		print("# --------- TRANSACTION " + str(x)  + " -------")
		print("Hash: " + data['txs'][x]['hash'])
		print("Size: " + str(data['txs'][x]['size']) + " bytes")
		print("Time: " + convertTime(data['txs'][x]['time']))

		for y in range(0,len(data['txs'][x]['inputs'])):
			print("---RECEIVED " + str(y))
			print("Receive Address: " + str(data['txs'][x]['inputs'][y].get('prev_out').get('addr')))
			print("Amount: " + str(SatoshiToBTC(data['txs'][x]['inputs'][y].get('prev_out').get('value'))))
			print("Spent: " + str(data['txs'][x]['inputs'][y].get('prev_out').get('spent')))

		for z in range(0,len(data['txs'][x]['out'])):
			print("---SENT " + str(z))
			print("Sent Address: " + data['txs'][x]['out'][z].get('addr'))
			print("Amount: " + str(SatoshiToBTC(data['txs'][x]['out'][z].get('value'))))
			print("Spent: " + str(data['txs'][x]['out'][z].get('spent')))
