# Bitcoin Wallet & Transactions [![GitHub stars](https://img.shields.io/github/stars/badges/shields.svg?style=social&label=Stars)](https://github.com/sirdavalos/Bitcoin-Python-Python/)

[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://github.com/sirdavalos/Bitcoin-Python)
[![Repo](https://img.shields.io/badge/source-GitHub-303030.svg?maxAge=3600&style=flat-square)](https://github.com/sirdavalos/Bitcoin-Python)
[![Requires.io](https://img.shields.io/requires/github/celery/celery.svg)](https://requires.io/github/sirdavalos/Bitcoin/requirements/?branch=master)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/filp/whoops.svg)](https://github.com/sirdavalos/Bitcoin-Python)
[![DUB](https://img.shields.io/dub/l/vibe-d.svg)](https://choosealicense.com/licenses/mit/)
[![Donate with Bitcoin](https://img.shields.io/badge/Donate-BTC-orange.svg)](https://blockchain.info/address/17dXgYr48j31myKiAhnM5cQx78XBNyeBWM)
[![Donate with Ethereum](https://img.shields.io/badge/Donate-ETH-blue.svg)](https://etherscan.io/address/91dd20538de3b48493dfda212217036257ae5150)

Python scripts which are for checking a wallet balance, show all transactions of an address.
[Blockchain.info](https://blockchain.info/api) API used.

### Info

There are 3 scripts in this repository.

***single_address.py*** - Prints the final balance, total received bitcoins, usd equivalent and the number of transactions of the address.

***wallet_balance.py*** - Shows the current balance of the wallet addresses in satoshi, bitcoin and the usd equivalent amount of the provided wallet address.

***wallet_transactions.py*** Shows the every transaction made to the provided wallet address.

### Instructions
------

0. Fork, clone or download this repository

    `git clone https://github.com/sirdavalos/Bitcoin-Python.git`

1. Navigate to the directory

    `cd Bitcoin`

2. Add wallet addresses to ***'inc/bitcoin-address.txt'*** file

3. Run the scripts

    `python wallet_balance.py`

    `python single_address.py [WALLET ADDRESS]`
    
    `python wallet_transactions.py [WALLET ADDRESS]`


### LICENSE
------

MIT License
