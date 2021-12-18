# EVM Wallet Manager
Provides a means to generate ultra secure Ethereum and Ethereum compliant blockchain wallets.

## Installation
The project is built with python and requires the following modules:
### Cryptography:
```
pip install cryptography
pip install web3
```
### Entropy:
```
pip install pyautogui
pip install sounddevice
```

## Usage
### Generating Wallets:
1. Navigate to line 25 in `wallet_gen.py` and change the following variables to suit your needs:
```
    u_show_private_key = 1
    u_show_mnemonic = 1
    u_save_mnemonic = 1
    u_use_bip_wl = 0
    u_encrypt_seed = 1

    u_file = "seed.txt"
    u_entropy = 215
```
2. Run `python wallet_gen.py` to create your wallet and keys.
### Reading Wallets:
1. Navigate to line 30 in `wallet_reader.py` and change the following variables:
```
    u_is_encrypted = True
    u_key = ""
    u_file = "seed.txt"
```
2. Run `python wallet_reader.py` to get your keys.
