#!/usr/bin/env python
# coding: utf-8
# coder:Tom Hou
# email: toosimple1984@gmail.com
# time:  Wed Oct 22 20:49:18 CST 2014


#将16位十六进制数，转化为64位二进制字符数组
def htob(h):
    b=bin(h)
    b=b[2:]
    b=(64-len(b))*'0'+b
    return b

#将64位二进制字符数组，转换为16位十六进制数
def btoh(s):
    l=len(s)
    key=0

    for i in range(0,l):
        if s[i]=='1':
            key=key+2**(l-1-i)
    key=hex(key)
        
    return key

#进行初始置换1，64 to 56
def permutation1(k):
    s=[];
    s.append(k[57-1]);s.append(k[49-1]);s.append(k[41-1]);s.append(k[33-1]);
    s.append(k[25-1]);s.append(k[17-1]);s.append(k[9-1]);s.append(k[1-1]);
    s.append(k[58-1]);s.append(k[50-1]);s.append(k[42-1]);s.append(k[34-1]);
    s.append(k[26-1]);s.append(k[18-1]);s.append(k[10-1]);s.append(k[2-1]);
    s.append(k[59-1]);s.append(k[51-1]);s.append(k[43-1]);s.append(k[35-1]);
    s.append(k[27-1]);s.append(k[19-1]);s.append(k[11-1]);s.append(k[3-1]);
    s.append(k[60-1]);s.append(k[52-1]);s.append(k[44-1]);s.append(k[36-1]);
    
    s.append(k[63-1]);s.append(k[55-1]);s.append(k[47-1]);s.append(k[39-1]);
    s.append(k[31-1]);s.append(k[23-1]);s.append(k[15-1]);s.append(k[7-1]);
    s.append(k[62-1]);s.append(k[54-1]);s.append(k[46-1]);s.append(k[38-1]);
    s.append(k[30-1]);s.append(k[22-1]);s.append(k[14-1]);s.append(k[6-1]);
    s.append(k[61-1]);s.append(k[53-1]);s.append(k[45-1]);s.append(k[37-1]);
    s.append(k[29-1]);s.append(k[21-1]);s.append(k[13-1]);s.append(k[5-1]);
    s.append(k[28-1]);s.append(k[20-1]);s.append(k[12-1]);s.append(k[4-1]);
    return s

#对28比特进行循环左移一位
def leftshift(s):
    temp=s[0]
    for i in range(0,27):
        s[i]=s[i+1]
    s[27]=temp
    return s

#进行置换2，56 to 48
def permutation2(s):
    k=[];
    k.append(s[14-1]);k.append(s[17-1]);k.append(s[11-1]);k.append(s[24-1]);
    k.append(s[1-1]);k.append(s[5-1]);k.append(s[3-1]);k.append(s[28-1]);
    k.append(s[15-1]);k.append(s[6-1]);k.append(s[21-1]);k.append(s[10-1]);

    k.append(s[23-1]);k.append(s[19-1]);k.append(s[12-1]);k.append(s[4-1]);
    k.append(s[26-1]);k.append(s[8-1]);k.append(s[16-1]);k.append(s[7-1]);
    k.append(s[27-1]);k.append(s[20-1]);k.append(s[13-1]);k.append(s[2-1]);

    k.append(s[41-1]);k.append(s[52-1]);k.append(s[31-1]);k.append(s[37-1]);
    k.append(s[47-1]);k.append(s[55-1]);k.append(s[30-1]);k.append(s[40-1]);
    k.append(s[51-1]);k.append(s[45-1]);k.append(s[33-1]);k.append(s[48-1]);

    k.append(s[44-1]);k.append(s[49-1]);k.append(s[39-1]);k.append(s[56-1]);
    k.append(s[34-1]);k.append(s[53-1]);k.append(s[46-1]);k.append(s[42-1]);
    k.append(s[50-1]);k.append(s[36-1]);k.append(s[29-1]);k.append(s[32-1]);
    return k

#64比特初始密钥，生成16个48比特子密钥
def deskey(key):
    s=permutation1(key)
    #print "进行初始置换1后%d位为:%s"%(len(s),s)
    
    out=[]
    once=[1,2,9,16]
    for i in range(1,17):
        c=s[0:28]
        d=s[28:56]
        c=leftshift(c)
        d=leftshift(d)
        if i not in once:
            c=leftshift(c)
            d=leftshift(d)
        s=c+d
        key=permutation2(s)
        #print "第%d轮%d位子密钥为:%s"%(i,len(key),key)
        out.append(key)
    return out
    
def main():
    print ">>此算法为根据16位十六进制初始密钥,求16轮子密钥。"
    #key=input(">>请输入初始密钥（例：0xfedcba9876543210)：")
    key=0xfedcba9876543210
    k=htob(key)

    s=deskey(k)

    for i in range(0,16):
        print "第%d轮子密钥:"%(i+1)
        h=btoh(s[i])
        print "%d位十六进制表示为:%s"%(len(h)-3,h)
        print "%d位二进制表示为:%s\n"%(len(s[i]),s[i])

def test():
    s=[]
    s.append('a')
    for i in range(0,26):
        s.append('0')
        s.append('e')
        print s
        s=leftshift(s)
        print s
