import random
import math

def gcd(x,y):
    while (y):
        x,y=y,x%y
    return x

def Miller_Rabin(p):
    for number in [2,3,5,7]:
        if gcd(number,p) != 1 or pow(number,p-1,p) != 1:
            return False
    d = p - 1
    s = 0
    alredy_chosen = []
    while d % 2 == 0:
        d //= 2
        s += 1
    for counter in range(10):
        x = 0
        while True:
            x = random.randint(1,p-1)
            if x not in alredy_chosen:
                break
        if gcd(x,p) > 1:
            return False
        if pow(x,d,p) == 1 or pow(x,d,p) == p-1:
            continue
        else:
            pseudo_random = False
            for r in range(1,s):
                x_r = pow(x,d * 2**r,p)
                if x_r == p-1:
                    pseudo_random = True
                elif x_r == 1:
                    return False
                else:
                    continue
            if not pseudo_random:
                return False
    return True


def Choose_Random_Prime(amount_of_bits,info_for_report=False):
    n0 = int('1'+'0'*(amount_of_bits // 2-2)+'1',2)
    n1 = int('1'*(amount_of_bits // 2),2)
    x = random.randint(n0,n1)
    m0 = x if x % 2 != 0 else x + 1
    for i in range(1,n1-m0//2):
        candidate = m0+2*i
        if Miller_Rabin(candidate):
            return candidate
        if info_for_report:
            print("кандидат на роль {} {} не пройшов тест Міллера–Рабіна".format(info_for_report,hex(candidate)))

def Find_Mod_Inverse(a, m):
    if math.gcd(a,m) != 1:
        return None
    orig_m = m
    prevu, u = 1, 0
    prevv, v = 0, 1
    while m != 0:
        q = a//m
        u, prevu = prevu - q*u, u
        v, prevv = prevv - q*v, v
        a, m = m, a % m
    return prevu % orig_m
