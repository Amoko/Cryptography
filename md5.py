#!/usr/bin/env python
# coding: utf-8
# coder: Amoko
# email: toosimple1984@gmail.com
# time:  Sat Nov 15 22:40:20 CST 2014

K=range(64)
K[0:64]=[0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
         0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
         0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
         0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
         
         0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
         0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
         0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
         0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,

         0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
         0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
         0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
         0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,

         0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
         0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
         0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
         0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]

J=range(64)
for i in range(0,64):
    if i<16:
        J[i]=i
    elif i<32:
        J[i]=(5*i+1)%16
    elif i<48:
        J[i]=(3*i+5)%16
    elif i<64:
        J[i]=(7*i)%16
    #print J[i]



#从M取第i个32位比特块
def getm(M,i):
    return M[32*i:32*(i+1)]


#将十进制或十六进制数n，转换为32位二进制字符数组out
def tob(n):
    b=bin(n)
    b=b[2:]
    b=(32-len(b))*'0'+b

    out=range(32)
    for i in range(0,32):
        out[i]=b[i]
    
    return out

#将二进制字符数组b，转换为十六进制数n
def toh(s):
    l=len(s)
    n=0

    for i in range(0,l):
        if s[i]=='1':
            n=n+2**(l-i-1)
    n=hex(n)
    return n


def and32(x,y):
    z=range(32)
    for i in range(0,32):
        z[i]=str(int(x[i]) and int(y[i]))
    return z

def or32(x,y):
    z=range(32)
    for i in range(0,32):
        z[i]=str(int(x[i]) or int(y[i]))
    return z

def xor32(x,y):
    z=range(32)
    for i in range(0,32):
        if x[i]==y[i]:
            z[i]='0'
        else:
            z[i]='1'
    return z

def not32(x):
    y=range(32)
    for i in range(0,32):
        if x[i]=='0':
            y[i]='1'
        else:
            y[i]='0'
    return y

def plus32(x,y):
    z=range(32)
    carry=0
    for i in range(31,-1,-1):
        sum=int(x[i])+int(y[i])+carry
        if sum>=2:
            carry=1
            z[i]=str(sum-2)
        else:
            carry=0
            z[i]=str(sum)
    return z

#32位数组s循环左移c位
def left32(s,c):
    o=range(32)
    for i in range(0,32):
        j=(i+c)%32
        o[i]=s[j]
    return o

def fun_F(x,y,z):
    a=and32(x,y)
    b=and32(not32(x),z)
    return or32(a,b)

def fun_G(x,y,z):
    a=and32(x,z)
    b=and32(y,not32(z))
    return or32(a,b)

def fun_H(x,y,z):
    b=xor32(y,z)
    return xor32(x,b)

def fun_I(x,y,z):
    b=or32(x,not32(z))
    return xor32(y,b)

def cal(f,x1,x2,x3,x4,x5,m,k,c):
    if f=='F':
        F=fun_F(x3,x4,x5)
    elif f=='G':
        F=fun_G(x3,x4,x5)
    elif f=='H':
        F=fun_H(x3,x4,x5)
    elif f=='I':
        F=fun_I(x3,x4,x5)

    #print(f,len(F),len(x1),len(x2),len(x3),len(x4),len(x5),len(m),len(k),c)
    
    t1=plus32(x2,F)
    t2=plus32(m,k)
    t3=plus32(t1,t2)
    t4=plus32(x1,left32(t3,c))
    return t4
    

#MD5的核心循环算法,64次循环
def fun(A,B,C,D,M):
    for i in range(0,16):
        if i<4:
            A=cal('F',B,A,B,C,D,getm(M,J[i*4+0]),tob(K[i*4+0]),7)
            D=cal('F',A,D,A,B,C,getm(M,J[i*4+1]),tob(K[i*4+1]),12)
            C=cal('F',D,C,D,A,B,getm(M,J[i*4+2]),tob(K[i*4+2]),17)
            B=cal('F',C,B,C,D,A,getm(M,J[i*4+3]),tob(K[i*4+3]),22)
        elif i<8:
            A=cal('G',B,A,B,C,D,getm(M,J[i*4+0]),tob(K[i*4+0]),5)
            D=cal('G',A,D,A,B,C,getm(M,J[i*4+1]),tob(K[i*4+1]),9)
            C=cal('G',D,C,D,A,B,getm(M,J[i*4+2]),tob(K[i*4+2]),14)
            B=cal('G',C,B,C,D,A,getm(M,J[i*4+3]),tob(K[i*4+3]),20)
        elif i<12:
            A=cal('H',B,A,B,C,D,getm(M,J[i*4+0]),tob(K[i*4+0]),4)
            D=cal('H',A,D,A,B,C,getm(M,J[i*4+1]),tob(K[i*4+1]),11)
            C=cal('H',D,C,D,A,B,getm(M,J[i*4+2]),tob(K[i*4+2]),16)
            B=cal('H',C,B,C,D,A,getm(M,J[i*4+3]),tob(K[i*4+3]),23)
        elif i<16:
            A=cal('I',B,A,B,C,D,getm(M,J[i*4+0]),tob(K[i*4+0]),6)
            D=cal('I',A,D,A,B,C,getm(M,J[i*4+1]),tob(K[i*4+1]),10)
            C=cal('I',D,C,D,A,B,getm(M,J[i*4+2]),tob(K[i*4+2]),15)
            B=cal('I',C,B,C,D,A,getm(M,J[i*4+3]),tob(K[i*4+3]),21)
    return A,B,C,D


#将字符串转换为其ascii码的二进制字符串
def ascii(s):
    m=''
    for i in range(0,len(s)):
        t1=ord(s[i])
        t2=bin(t1)
        t3=t2[2:]
        b='0'*(8-len(t3))+t3
        m=m+b
        
    return m

#消息的初始化
def init():
    m=ascii('')
    len_m=len(m)
    b=bin(len_m)
    b=b[2:]
    
    len_r=512-len_m%512
    if len_r>=65:
        o=m+'1'+(len_r-1-len(b))*'0'+b
    else:
        o=m+'1'+(512+len_r-1-len(b))*'0'+b

    return o

#对任意长度输入，输出128比特杂凑值
def md5():
    s=init()
    n=len(s)/512

    #A0=tob(0x01234567)
    #B0=tob(0x89abcdef)
    #C0=tob(0xfedcba98)
    #D0=tob(0x76543210)
    
    A0=tob(0x67452301)
    B0=tob(0xefcdab89)
    C0=tob(0x98badcfe)
    D0=tob(0x10325476)

    for k in range(0,n):
        A=A0
        B=B0
        C=C0
        D=D0
        M=s[k*512:(k+1)*512]
        
        #64次循环计算
        A,B,C,D=fun(A,B,C,D,M)

        A0=plus32(A0,A)
        B0=plus32(B0,B)
        C0=plus32(C0,C)
        D0=plus32(D0,D)

    return toh(A0+B0+C0+D0)


def test_plus32():
    x=['1']+['1']*31
    y=['1']*31+['0']
    z=plus32(x,y)

    print(x)
    print(y)
    print(z)

if __name__ == '__main__':
    out = md5()
    print(out)
