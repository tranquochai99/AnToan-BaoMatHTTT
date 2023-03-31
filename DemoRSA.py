def chon_p(key_size) :
    import sympy
    p = sympy.randprime((2**((int(key_size)/2)-1)) , (2**(int(key_size)-(int(key_size)/2))-1))
    return p

def chon_q(key_size) :
    import sympy
    q = sympy.randprime((2**((int(key_size)/2)-1)) , (2**(int(key_size)-(int(key_size)/2))-1))
    return q

def Tao_Khoa(key_size) :
    p = chon_p(key_size)
    q = chon_q(key_size)
    n = p * q
    z = (p-1) * (q-1)
    e = tinh_e(n,z)
    d = tinh_d(e,z)
    return[p,q,n,z,e,d]

def UCLN(a, b):
    if b == 0:
        return a
    return UCLN(b, a % b)

def tinh_e(n,z) :
    import random
    e = random.randint(1,n-1)
    while UCLN(e,z) != 1:
        e = random.randint(1,n-1)
    return e

def tinh_d(e,z) :
    t1 = 0
    t2 = 1 
    a = z
    b = e
    while True :
        q = a // b
        r = a % b
        a = b
        b = r
        t = t1 - t2 * q
        t1 = t2
        t2 = t
        if a == 1 :
            d = t1
            break
    if d<0 :
        d = d + z
        return d
    else :
        return d


def encrypt(plain_text,n,e) :
    cipher_text =''
    L =[]
    for i in plain_text :
        m = ord(i)
        c = pow(m,e,n)
        cipher_text = cipher_text + str(c)
        L = L + [c]
    return cipher_text, L

def decrypt(L,n,d) :
    plain_text=''
    for i in range(0, len(L)) :
        m = pow(L[i],d,n)
        plain_text = plain_text + chr(m)
    return plain_text


def ky_thong_diep(thong_diep,n,d) :
    import hashlib
    hash_value = hashlib.sha1(thong_diep.encode()).hexdigest()
    thong_diep_da_ky = ''
    thong_diep_da_bam = ''
    for i in range(0,len(hash_value)) :
        m = ord(hash_value[i])
        c = pow(m,d,n)
        thong_diep_da_bam = thong_diep_da_bam + str(c) + '\n'

    thong_diep_da_ky = thong_diep + '\n' + thong_diep_da_bam
    return thong_diep_da_ky


key_size = input('Nhap do dai bit: ')
thong_diep = input(str('Nhap thong diep: '))
p,q,n,z,e,d = Tao_Khoa(key_size)

print('q=',q)
print('p=',p)
print('n=',n)
print('z=',z)
print('e=',e)
print('d=',d)
print('\n')

print('Public key: (',n,',',e,')')
print('Private key: (',n,',',d,')')
print('\n')

cipher_text, L= encrypt(thong_diep,n,e)
print('mã hóa:',cipher_text)
print('\n')

plain_text = decrypt(L,n,d)
print('giải mã:',plain_text)
print('\n')

thong_diep_da_ky = ky_thong_diep(thong_diep,n,d)
print(thong_diep_da_ky)


