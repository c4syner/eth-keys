#CREATE WALLETS
from web3 import Web3, EthereumTesterProvider
from hexbytes import HexBytes
from cryptography.fernet import Fernet


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
    #DEFAULTS
    #STATES
    u_show_private_key = 1
    u_show_mnemonic = 1
    u_save_mnemonic = 1
    u_use_bip_wl = 0
    u_encrypt_seed = 1

    #LITERALS
    u_file = "seed.txt"
    u_entropy = 215

    w3 = Web3(EthereumTesterProvider())
    print("\n"*50) #lol
    print("Begin moving your mouse and talking into your microphone to generate entropy")
    #ebytes = bytes of entropy
    ebytes = u_entropy
    #import it now to avoid libraries trying to use 
    import entro 
    x = entro.entropy_event(ebytes, u_use_bip_wl)
    if(u_encrypt_seed):
        key = Fernet.generate_key()
    
    tx = x
    if(u_encrypt_seed):
        tx = Fernet(key).encrypt(x.encode('utf-8')).decode('utf-8')
    if(u_save_mnemonic):
        with open(u_file, "w+") as f:
            f.write(tx)
        
    print("Seed saved to {n}\n".format(n=u_file))
    print("Address: {n}".format(n=eas(w3, x)))
    print("Seed Key: {f}".format(f=key.decode("utf-8")))

    if(u_show_private_key):
        print("Private Key: {n}".format(n=w3.toHex(private_key_from_seed(x))))
    if(u_show_mnemonic):
        if(u_encrypt_seed):
            print("(Encrypted) ", end="")
        print("Seed (Mnemonic): {n}".format(n=tx))

if __name__ == "__main__":
    main()