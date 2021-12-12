import math

# @dev Calculate bits of entropy for a theoretical password set
def p_entropy(charset_len: int, pw_len: int):
    return ((pw_len*math.log(charset_len))/math.log(2))


if __name__ == "__main__":
    print("Blockchain Industry Standard:")
    print(p_entropy(2048, 12))
    print("Default eth-keys wallet:")
    print(p_entropy(94, 500))
    
