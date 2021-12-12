from web3 import Web3, EthereumTesterProvider
from hexbytes import HexBytes
import entro
import time
from Crypto.Cipher import AES

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
"""
@dev Returns an AES-GCM Encrypted string, also given a key
"""
def aes_gcm(key: str, text: str) -> str:
    return AES.new(key, AES.MODE_GCM).encrypt_and_digest(text.encode("utf-8"))

def main():
    x = entro.entropy_event(100)

    w3 = Web3(EthereumTesterProvider())
    f_name = input("File to save your seed in: ")
    f_pass = input("Password to encrypt your seed: ")
    print("Begin moving your mouse to generate entropy")
    time.sleep(2)
    #ebytes = bytes of entropy
    ebytes = 125
    x = entro.entropy_event(ebytes)
    

    with open(f_name, "w+") as f:
        f.write(aes_gcm(f_pass, x))
    print("Seed saved to {n}".format(n=f_name))
    print("Address: {n}".format(n=eas(w3, x)))
    print("Private Key: {n}".format(n=w3.toHex(private_key_from_seed(x))))

if __name__ == "__main__":
    main()
