from web3 import Web3, EthereumTesterProvider
from hexbytes import HexBytes
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
    w3 = Web3(EthereumTesterProvider())
    x = (input("Seed: "))
    print("Address: {n}".format(n=eas(w3, x)))
    print("Private Key: {n}".format(n=w3.toHex(private_key_from_seed(x))))
if __name__ == "__main__":
    main()
