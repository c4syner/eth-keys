#READ WALLETS
#CREATE WALLETS
from web3 import Web3, EthereumTesterProvider
from hexbytes import HexBytes
import time
from cryptography.fernet import Fernet
import getpass
import sys
import json
import warnings

from web3._utils.encoding import FriendlyJsonSerde

"""
@dev returns a byte hash of a string
"""
def private_key_from_seed(seed: str) -> HexBytes:
    return Web3.keccak(text=seed)
"""
@dev returns an ethereum address from a private key string
"""
def eth_address_from_private_key(w3: Web3, private_key: str) -> str:
    return w3.eth.account.from_key(private_key).address
"""
@dev returns an ethereum address from a mnemonic (seed)
"""
def eas(w3: Web3, seed: str) -> str:   
    return eth_address_from_private_key(w3,private_key_from_seed(seed))

def main():
    u_is_encrypted = True
    u_key = ""
    u_file = "seed.txt"

    w3 = Web3(EthereumTesterProvider())
    with open(u_file, "r") as f:
        seed_data = (f.readlines())[0]
        print(seed_data)
        if(u_is_encrypted):
            seed_data = Fernet(u_key.encode('utf-8')).decrypt(bytes(seed_data, "utf-8")).decode('utf-8')

    x = seed_data
    print("Address: {n}".format(n=eas(w3, x)))
    print("Private Key: {n}".format(n=w3.toHex(private_key_from_seed(x))))
    print("Seed (Mnemonic): {n}".format(n=x))

if __name__ == "__main__":
    main()