key_size=128
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


def encrypt(in_file,out_file,n,e) :
    f1 = open(in_file)
    f2 = f1.read()
    f3=''
    for i in f2 :
        m = ord(i)
        c = pow(m,e,n)
        f3 = f3 + str(c) + '\n'

    f4 = open(out_file, 'x')
    f4.write(f3)
    f4.close()
    

def decrypt(in_file,out_file,n,d) :
    f1 = open(in_file)
    f2 = f1.readlines()
    f3 = ''
    L = []
    for i in range(0, len(f2)) :
        L = L + [int(f2[i].rstrip('\n'))]
    for i in range(0,len(L)) :    
        m = pow(L[i],d,n)
        f3 = f3 + chr(m)
    f4 = open(out_file, 'x')
    f4.write(f3)


def ky_thong_diep(in_file,out_file,n,d) :
    f1 = open(in_file)
    f2 = f1.read()
    import hashlib
    hash_value = hashlib.sha1(f2.encode()).hexdigest()
    thong_diep_da_bam = ''
    for i in range(0,len(hash_value)) :
        m = ord(hash_value[i])
        c = pow(m,d,n)
        thong_diep_da_bam = thong_diep_da_bam + str(c) + '\n'

    f3 = open(out_file, 'x')
    f3.writelines(f2 + '\n' + thong_diep_da_bam)

def Check_integrity(in_file,n,e) :
    f1 = open(in_file)
    data = f1.readlines()
    mess = ''
    for i in range(0, len(data) - 40):
        line = data[i].rstrip('\n')
        if i != (len(data) - 41) :
            line = line + '\n'
        mess = mess + line

    global MD1, MD2, check

    import hashlib
    MD1 = hashlib.sha1(mess.encode()).hexdigest()

    CKS = []
    for i in range(len(data) - 40, len(data)) :
        line = data[i]
        CKS = CKS + [line]
    
    MD2 = ''
    for i in range(0, len(CKS)) :
        m = pow(int(CKS[i]), e, n)
        h = chr(m)
        MD2 = MD2 + h

    if MD1 == MD2 :
        check = 'Dữ liệu toàn vẹn'
    else :
        check = 'Dữ liệu không toàn vẹn'


