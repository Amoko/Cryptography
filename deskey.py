#!/usr/bin/env python
# coding: utf-8
# coder:Tom Hou
# email: toosimple1984@gmail.com
# time:  Wed Oct 22 20:49:18 CST 2014


#将16位十六进制密钥，转化为64位二进制数组
def htob(h):
    b=bin(h)
    b=b[2:]
    b=(64-len(b))*'0'+b
    return b

#进行初始置换1，64 to 56
def permutation1(key):
    s=[];
    s.append(key[57-1]);s.append(key[49-1]);s.append(key[41-1]);s.append(key[33-1]);
    s.append(key[25-1]);s.append(key[17-1]);s.append(key[9-1]);s.append(key[1-1]);
    s.append(key[58-1]);s.append(key[50-1]);s.append(key[42-1]);s.append(key[34-1]);
    s.append(key[26-1]);s.append(key[18-1]);s.append(key[10-1]);s.append(key[2-1]);
    s.append(key[59-1]);s.append(key[51-1]);s.append(key[43-1]);s.append(key[35-1]);
    s.append(key[27-1]);s.append(key[19-1]);s.append(key[11-1]);s.append(key[3-1]);
    s.append(key[60-1]);s.append(key[52-1]);s.append(key[44-1]);s.append(key[36-1]);
    
    s.append(key[63-1]);s.append(key[55-1]);s.append(key[47-1]);s.append(key[39-1]);
    s.append(key[31-1]);s.append(key[23-1]);s.append(key[15-1]);s.append(key[7-1]);
    s.append(key[62-1]);s.append(key[54-1]);s.append(key[46-1]);s.append(key[38-1]);
    s.append(key[30-1]);s.append(key[22-1]);s.append(key[14-1]);s.append(key[6-1]);
    s.append(key[61-1]);s.append(key[53-1]);s.append(key[45-1]);s.append(key[37-1]);
    s.append(key[29-1]);s.append(key[21-1]);s.append(key[13-1]);s.append(key[5-1]);
    s.append(key[28-1]);s.append(key[20-1]);s.append(key[12-1]);s.append(key[4-1]);
    return s

#对28比特进行循环左移一位
def leftshift(s):
    temp=s[0]
    for i in range(0,26):
        s[i]=s[i+1]
    s[27]=temp
    return s

#进行置换2，56 to 48
def permutation2(s):
    key=[];
    key.append(s[14-1]);key.append(s[17-1]);key.append(s[11-1]);key.append(s[24-1]);
    key.append(s[1-1]);key.append(s[5-1]);key.append(s[3-1]);key.append(s[28-1]);
    key.append(s[15-1]);key.append(s[6-1]);key.append(s[21-1]);key.append(s[10-1]);

    key.append(s[23-1]);key.append(s[19-1]);key.append(s[12-1]);key.append(s[4-1]);
    key.append(s[26-1]);key.append(s[8-1]);key.append(s[16-1]);key.append(s[7-1]);
    key.append(s[27-1]);key.append(s[20-1]);key.append(s[13-1]);key.append(s[2-1]);

    key.append(s[41-1]);key.append(s[52-1]);key.append(s[31-1]);key.append(s[37-1]);
    key.append(s[47-1]);key.append(s[55-1]);key.append(s[30-1]);key.append(s[40-1]);
    key.append(s[51-1]);key.append(s[45-1]);key.append(s[33-1]);key.append(s[48-1]);

    key.append(s[44-1]);key.append(s[49-1]);key.append(s[39-1]);key.append(s[56-1]);
    key.append(s[34-1]);key.append(s[53-1]);key.append(s[46-1]);key.append(s[42-1]);
    key.append(s[50-1]);key.append(s[36-1]);key.append(s[29-1]);key.append(s[32-1]);
    return key


def deskey(key):
    s=htob(key)
    #print "初始密钥的二进制表示为:%s,长度为%d位\n"%(s,len(s))
    
    s=permutation1(s)
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

print ">>此算法为根据16位十六进制初始密钥,求16轮子密钥。"
#key=input(">>请输入初始密钥（例：0xfedcba9876543210)：")
key=0xfedcba9876543210
s=deskey(key)

for i in range(0,16):
    print "第%d轮%d位子密钥为:%s"%(i+1,len(s[i]),s[i])

