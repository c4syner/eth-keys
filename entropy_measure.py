import math

# @dev Calculate bits of entropy for a theoretical password
def p_entropy(charset_len: int, pw_len: int):
    return ((pw_len*math.log(charset_len))/math.log(2))

# @dev Calculate the % of values between 0-n up to a max value
def logp(n: int, m_test: int, base: int) -> float:
    v = 0
    for i in range(n):
        if(not i):
            continue
        v +=  math.log(i)/math.log(base)
    v_test = 0
    for i in range(m_test):
        if(not i):
            continue
        v_test += math.log(i)/math.log(base)
    return (v/v_test)*100


if __name__ == "__main__":
    #print(p_entropy(2048, 12))
    print(logp(2048, 1000000, 2))
