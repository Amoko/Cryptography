#!/usr/bin/env python
# coding: utf-8
# coder:Tom Hou
# email: toosimple1984@gmail.com
# time:  Sat Nov 15 22:40:20 CST 2014

#s.append(m[-1]);s.append(m[-1]);s.append(m[-1]);s.append(m[-1]);

import deskey

#初始置换
def permutation1(m):
    s=[]
    s.append(m[58-1]);s.append(m[50-1]);s.append(m[42-1]);s.append(m[34-1]);
    s.append(m[26-1]);s.append(m[18-1]);s.append(m[10-1]);s.append(m[2-1]);
    s.append(m[60-1]);s.append(m[52-1]);s.append(m[44-1]);s.append(m[36-1]);
    s.append(m[28-1]);s.append(m[20-1]);s.append(m[12-1]);s.append(m[4-1]);

    s.append(m[62-1]);s.append(m[54-1]);s.append(m[46-1]);s.append(m[38-1]);
    s.append(m[30-1]);s.append(m[22-1]);s.append(m[14-1]);s.append(m[6-1]);
    s.append(m[64-1]);s.append(m[56-1]);s.append(m[48-1]);s.append(m[40-1]);
    s.append(m[32-1]);s.append(m[24-1]);s.append(m[16-1]);s.append(m[8-1]);

    s.append(m[57-1]);s.append(m[49-1]);s.append(m[41-1]);s.append(m[33-1]);
    s.append(m[25-1]);s.append(m[17-1]);s.append(m[9-1]);s.append(m[1-1]);
    s.append(m[59-1]);s.append(m[51-1]);s.append(m[43-1]);s.append(m[35-1]);
    s.append(m[27-1]);s.append(m[19-1]);s.append(m[11-1]);s.append(m[3-1]);

    s.append(m[61-1]);s.append(m[53-1]);s.append(m[45-1]);s.append(m[37-1]);
    s.append(m[29-1]);s.append(m[21-1]);s.append(m[13-1]);s.append(m[5-1]);
    s.append(m[63-1]);s.append(m[55-1]);s.append(m[47-1]);s.append(m[39-1]);
    s.append(m[31-1]);s.append(m[23-1]);s.append(m[15-1]);s.append(m[7-1]);
    return s

#逆初始置换
def permutation2(m):
    s=[]
    s.append(m[40-1]);s.append(m[8-1]);s.append(m[48-1]);s.append(m[16-1]);
    s.append(m[56-1]);s.append(m[24-1]);s.append(m[64-1]);s.append(m[32-1]);
    s.append(m[39-1]);s.append(m[7-1]);s.append(m[47-1]);s.append(m[15-1]);
    s.append(m[55-1]);s.append(m[23-1]);s.append(m[63-1]);s.append(m[31-1]);

    s.append(m[38-1]);s.append(m[6-1]);s.append(m[46-1]);s.append(m[14-1]);
    s.append(m[54-1]);s.append(m[22-1]);s.append(m[62-1]);s.append(m[30-1]);
    s.append(m[37-1]);s.append(m[5-1]);s.append(m[45-1]);s.append(m[13-1]);
    s.append(m[53-1]);s.append(m[21-1]);s.append(m[61-1]);s.append(m[29-1]);

    s.append(m[36-1]);s.append(m[4-1]);s.append(m[44-1]);s.append(m[12-1]);
    s.append(m[52-1]);s.append(m[20-1]);s.append(m[60-1]);s.append(m[28-1]);
    s.append(m[35-1]);s.append(m[3-1]);s.append(m[43-1]);s.append(m[11-1]);
    s.append(m[51-1]);s.append(m[19-1]);s.append(m[59-1]);s.append(m[27-1]);

    s.append(m[34-1]);s.append(m[2-1]);s.append(m[42-1]);s.append(m[10-1]);
    s.append(m[50-1]);s.append(m[18-1]);s.append(m[58-1]);s.append(m[26-1]);
    s.append(m[33-1]);s.append(m[1-1]);s.append(m[41-1]);s.append(m[9-1]);
    s.append(m[49-1]);s.append(m[17-1]);s.append(m[57-1]);s.append(m[25-1]);    
    return s

#E盒扩展，32 to 48
def extension(m):
    s=[]
    s.append(m[32-1]);s.append(m[1-1]);s.append(m[2-1]);s.append(m[3-1]);
    s.append(m[4-1]);s.append(m[5-1]);s.append(m[4-1]);s.append(m[5-1]);
    s.append(m[6-1]);s.append(m[7-1]);s.append(m[8-1]);s.append(m[9-1]);

    s.append(m[8-1]);s.append(m[9-1]);s.append(m[10-1]);s.append(m[11-1]);
    s.append(m[12-1]);s.append(m[13-1]);s.append(m[12-1]);s.append(m[13-1]);
    s.append(m[14-1]);s.append(m[15-1]);s.append(m[16-1]);s.append(m[17-1]);

    s.append(m[16-1]);s.append(m[17-1]);s.append(m[18-1]);s.append(m[19-1]);
    s.append(m[20-1]);s.append(m[21-1]);s.append(m[20-1]);s.append(m[21-1]);
    s.append(m[22-1]);s.append(m[23-1]);s.append(m[24-1]);s.append(m[25-1]);

    s.append(m[24-1]);s.append(m[25-1]);s.append(m[26-1]);s.append(m[27-1]);
    s.append(m[28-1]);s.append(m[29-1]);s.append(m[28-1]);s.append(m[29-1]);
    s.append(m[30-1]);s.append(m[31-1]);s.append(m[32-1]);s.append(m[1-1]);
    return s

#P盒移位排列，32 to 32
def permutation3(m):
    s=[]
    s.append(m[16-1]);s.append(m[7-1]);s.append(m[20-1]);s.append(m[21-1]);
    s.append(m[29-1]);s.append(m[12-1]);s.append(m[28-1]);s.append(m[17-1]);
    s.append(m[1-1]);s.append(m[15-1]);s.append(m[23-1]);s.append(m[26-1]);
    s.append(m[5-1]);s.append(m[18-1]);s.append(m[31-1]);s.append(m[10-1]);

    s.append(m[2-1]);s.append(m[8-1]);s.append(m[24-1]);s.append(m[14-1]);
    s.append(m[32-1]);s.append(m[27-1]);s.append(m[3-1]);s.append(m[9-1]);
    s.append(m[19-1]);s.append(m[13-1]);s.append(m[30-1]);s.append(m[6-1]);
    s.append(m[22-1]);s.append(m[11-1]);s.append(m[4-1]);s.append(m[25-1]);
    return s

#将0~15的十进制数转换为4位二进制数组
def dtob(d):
    s=bin(d)
    s=s[2:]
    s='0'*(4-len(s))+s
    return s

#Ｓ盒代替，48 to 32
def substitution(m):
    c=[]
#S1
    b=[]
    a=[]
    a.append(14);a.append(4);a.append(13);a.append(1);
    a.append(2);a.append(15);a.append(11);a.append(8);
    a.append(3);a.append(10);a.append(6);a.append(12);
    a.append(5);a.append(9);a.append(0);a.append(7);
    b.append(a)
    a=[]
    a.append(0);a.append(15);a.append(7);a.append(4);
    a.append(14);a.append(2);a.append(13);a.append(1);
    a.append(10);a.append(6);a.append(12);a.append(11);
    a.append(9);a.append(5);a.append(3);a.append(8);
    b.append(a)
    a=[]
    a.append(4);a.append(1);a.append(14);a.append(8);
    a.append(13);a.append(6);a.append(2);a.append(11);
    a.append(15);a.append(12);a.append(9);a.append(7);
    a.append(3);a.append(10);a.append(5);a.append(0);
    b.append(a)
    a=[]
    a.append(15);a.append(12);a.append(8);a.append(2);
    a.append(4);a.append(9);a.append(1);a.append(7);
    a.append(5);a.append(11);a.append(3);a.append(14);
    a.append(10);a.append(0);a.append(6);a.append(13);
    b.append(a)
    c.append(b)
#S2
    b=[]
    a=[]
    a.append(15);a.append(1);a.append(8);a.append(14);
    a.append(6);a.append(11);a.append(3);a.append(4);
    a.append(9);a.append(7);a.append(2);a.append(13);
    a.append(12);a.append(0);a.append(5);a.append(10);
    b.append(a)
    a=[]
    a.append(3);a.append(13);a.append(4);a.append(7);
    a.append(15);a.append(2);a.append(8);a.append(14);
    a.append(12);a.append(0);a.append(1);a.append(10);
    a.append(6);a.append(9);a.append(11);a.append(5);
    b.append(a)
    a=[]
    a.append(0);a.append(14);a.append(7);a.append(11);
    a.append(10);a.append(4);a.append(13);a.append(1);
    a.append(5);a.append(8);a.append(12);a.append(6);
    a.append(9);a.append(3);a.append(2);a.append(15);
    b.append(a)
    a=[]
    a.append(13);a.append(8);a.append(10);a.append(1);
    a.append(3);a.append(15);a.append(4);a.append(2);
    a.append(11);a.append(6);a.append(7);a.append(12);
    a.append(0);a.append(5);a.append(14);a.append(9);
    b.append(a)
    c.append(b)
#S3
    b=[]
    a=[]
    a.append(10);a.append(0);a.append(9);a.append(14);
    a.append(6);a.append(3);a.append(15);a.append(5);
    a.append(1);a.append(13);a.append(12);a.append(7);
    a.append(11);a.append(4);a.append(2);a.append(8);
    b.append(a)
    a=[]
    a.append(13);a.append(7);a.append(0);a.append(9);
    a.append(3);a.append(4);a.append(6);a.append(10);
    a.append(2);a.append(8);a.append(5);a.append(14);
    a.append(12);a.append(11);a.append(15);a.append(1);
    b.append(a)
    a=[]
    a.append(13);a.append(6);a.append(4);a.append(9);
    a.append(8);a.append(15);a.append(3);a.append(0);
    a.append(11);a.append(1);a.append(2);a.append(12);
    a.append(5);a.append(10);a.append(14);a.append(7);
    b.append(a)
    a=[]
    a.append(1);a.append(10);a.append(13);a.append(0);
    a.append(6);a.append(9);a.append(8);a.append(7);
    a.append(4);a.append(15);a.append(14);a.append(3);
    a.append(11);a.append(5);a.append(2);a.append(12);
    b.append(a)
    c.append(b)
#S4
    b=[]
    a=[]
    a.append(7);a.append(13);a.append(14);a.append(3);
    a.append(0);a.append(6);a.append(9);a.append(10);
    a.append(1);a.append(2);a.append(8);a.append(5);
    a.append(11);a.append(12);a.append(4);a.append(15);
    b.append(a)
    a=[]
    a.append(13);a.append(8);a.append(11);a.append(5);
    a.append(6);a.append(15);a.append(0);a.append(3);
    a.append(4);a.append(7);a.append(2);a.append(12);
    a.append(1);a.append(10);a.append(14);a.append(9);
    b.append(a)
    a=[]
    a.append(10);a.append(6);a.append(9);a.append(0);
    a.append(12);a.append(11);a.append(7);a.append(13);
    a.append(15);a.append(1);a.append(3);a.append(14);
    a.append(5);a.append(2);a.append(8);a.append(4);
    b.append(a)
    a=[]
    a.append(3);a.append(15);a.append(0);a.append(6);
    a.append(10);a.append(1);a.append(13);a.append(8);
    a.append(9);a.append(4);a.append(5);a.append(11);
    a.append(12);a.append(7);a.append(2);a.append(14);
    b.append(a)
    c.append(b)
#S5
    b=[]
    a=[]
    a.append(2);a.append(12);a.append(4);a.append(1);
    a.append(7);a.append(10);a.append(11);a.append(6);
    a.append(8);a.append(5);a.append(3);a.append(15);
    a.append(13);a.append(0);a.append(14);a.append(9);
    b.append(a)
    a=[]
    a.append(14);a.append(11);a.append(2);a.append(12);
    a.append(4);a.append(7);a.append(13);a.append(1);
    a.append(5);a.append(0);a.append(15);a.append(10);
    a.append(3);a.append(9);a.append(8);a.append(6);
    b.append(a)
    a=[]
    a.append(4);a.append(2);a.append(1);a.append(11);
    a.append(10);a.append(13);a.append(7);a.append(8);
    a.append(15);a.append(9);a.append(12);a.append(5);
    a.append(6);a.append(3);a.append(0);a.append(14);
    b.append(a)
    a=[]
    a.append(11);a.append(8);a.append(12);a.append(7);
    a.append(1);a.append(14);a.append(2);a.append(13);
    a.append(6);a.append(15);a.append(0);a.append(9);
    a.append(10);a.append(4);a.append(5);a.append(3);
    b.append(a)
    c.append(b)
#S6
    b=[]
    a=[]
    a.append(12);a.append(1);a.append(10);a.append(15);
    a.append(9);a.append(2);a.append(6);a.append(8);
    a.append(0);a.append(13);a.append(3);a.append(4);
    a.append(14);a.append(7);a.append(5);a.append(11);
    b.append(a)
    a=[]
    a.append(10);a.append(15);a.append(4);a.append(2);
    a.append(7);a.append(12);a.append(9);a.append(5);
    a.append(6);a.append(1);a.append(13);a.append(14);
    a.append(0);a.append(11);a.append(3);a.append(8);
    b.append(a)
    a=[]
    a.append(9);a.append(14);a.append(15);a.append(5);
    a.append(2);a.append(8);a.append(12);a.append(3);
    a.append(7);a.append(0);a.append(4);a.append(10);
    a.append(1);a.append(13);a.append(11);a.append(6);
    b.append(a)
    a=[]
    a.append(4);a.append(3);a.append(2);a.append(12);
    a.append(9);a.append(5);a.append(15);a.append(10);
    a.append(11);a.append(14);a.append(1);a.append(7);
    a.append(6);a.append(0);a.append(8);a.append(13);
    b.append(a)
    c.append(b)
#S7
    b=[]
    a=[]
    a.append(4);a.append(11);a.append(2);a.append(14);
    a.append(15);a.append(0);a.append(8);a.append(13);
    a.append(3);a.append(12);a.append(9);a.append(7);
    a.append(5);a.append(10);a.append(6);a.append(1);
    b.append(a)
    a=[]
    a.append(13);a.append(0);a.append(11);a.append(7);
    a.append(4);a.append(9);a.append(1);a.append(10);
    a.append(14);a.append(3);a.append(5);a.append(12);
    a.append(2);a.append(15);a.append(8);a.append(6);
    b.append(a)
    a=[]
    a.append(1);a.append(4);a.append(11);a.append(13);
    a.append(12);a.append(3);a.append(7);a.append(14);
    a.append(10);a.append(15);a.append(6);a.append(8);
    a.append(0);a.append(5);a.append(9);a.append(2);
    b.append(a)
    a=[]
    a.append(6);a.append(11);a.append(13);a.append(8);
    a.append(1);a.append(4);a.append(10);a.append(7);
    a.append(9);a.append(5);a.append(0);a.append(15);
    a.append(14);a.append(2);a.append(3);a.append(12);
    b.append(a)
    c.append(b)
#S8
    b=[]
    a=[]
    a.append(13);a.append(2);a.append(8);a.append(4);
    a.append(6);a.append(15);a.append(11);a.append(1);
    a.append(10);a.append(9);a.append(3);a.append(14);
    a.append(5);a.append(0);a.append(12);a.append(7);
    b.append(a)
    a=[]
    a.append(1);a.append(15);a.append(13);a.append(8);
    a.append(10);a.append(3);a.append(7);a.append(4);
    a.append(12);a.append(5);a.append(6);a.append(11);
    a.append(0);a.append(14);a.append(9);a.append(2);
    b.append(a)
    a=[]
    a.append(7);a.append(11);a.append(4);a.append(1);
    a.append(9);a.append(12);a.append(14);a.append(2);
    a.append(0);a.append(6);a.append(10);a.append(13);
    a.append(15);a.append(3);a.append(5);a.append(8);
    b.append(a)
    a=[]
    a.append(2);a.append(1);a.append(14);a.append(7);
    a.append(4);a.append(10);a.append(8);a.append(13);
    a.append(15);a.append(12);a.append(9);a.append(0);
    a.append(3);a.append(5);a.append(6);a.append(11);
    b.append(a)
    c.append(b)

    s=''
    for i in range(0,8):
        row=0
        if '1'==m[i*6+0]:
            row=row+2
        if '1'==m[i*6+5]:
            row=row+1

        column=0
        if '1'==m[i*6+1]:
            column=column+8
        if '1'==m[i*6+2]:
            column=column+4
        if '1'==m[i*6+3]:
            column=column+2
        if '1'==m[i*6+4]:
            column=column+1
        
        o=c[i][row][column]
        s=s+dtob(o)

    return s

#按位异或
def xor(a,b):
    m=[]
    l=len(a)
    for i in range(0,l):
        if a[i]==b[i]:
            m.append('0')
        else:
            m.append('1')
    return m

#f函数
def fun(r,k):
    r=extension(r)
    m=xor(r,k)
    m=substitution(m)
    m=permutation3(m)
    return m

#des算法
def des(m,k):
    m=permutation1(m)
    
    l=m[0:32]
    r=m[32:64]
    for i in range(0,16):
        temp=l
        l=r
        r=xor(temp,fun(r,k[i]))
    
    c=permutation2(r+l)
    
    return c

def main():
    #m=input("请输入明文：（例：0xabcde0123456789）")
    m=0x0123456789abcdef
    #key=input("请输入密钥：（例：0x1234567890abcde）")
    key=0x0123456789abcdef

    m=deskey.htob(m)
    key=deskey.htob(key)
  
    k=deskey.deskey(key)
    c=des(m,k)

    c=deskey.btoh(c)
    print c

main()
