#!/usr/bin/env python
# coding: utf-8
# coder: Amoko
# email: toosimple1984@gmail.com
# time:  Wed Oct 22 20:49:18 CST 2014


#将16位十六进制数，转化为64位二进制字符数组
def htob(h):
    b = bin(h)
    b = b[2:]
    b = (64-len(b))*'0'+b
    return b

#将64位二进制字符数组，转换为16位十六进制数
def btoh(s):
    key = 0
    L = len(s)
    for i in range(0, L):
        if s[i] == '1':
            key += 2**(L-1-i)
    key = hex(key)
        
    return key

#进行初始置换1，64 to 56
def permutation1(k):
    position = [
        57, 49, 41, 33, 25, 17, 9, 1, 
        58, 50, 42, 34, 26, 18, 10, 2, 
        59, 51, 43, 35, 27, 19, 11, 3, 
        60, 52, 44, 36, 63, 55, 47, 39, 
        31, 23, 15, 7, 62, 54, 46, 38, 
        30, 22, 14, 6, 61, 53, 45, 37, 
        29, 21, 13, 5, 28, 20, 12, 4]
    s = []
    for pos in position:
        s.append(k[pos -1])
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
    position = [
        14, 17, 11, 24, 1, 5, 3, 28, 
        15, 6, 21, 10, 23, 19, 12, 4, 
        26, 8, 16, 7, 27, 20, 13, 2, 
        41, 52, 31, 37, 47, 55, 30, 40, 
        51, 45, 33, 48, 44, 49, 39, 56, 
        34, 53, 46, 42, 50, 36, 29, 32] 
    k = []
    for pos in position:
        k.append(s[pos -1])
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
    print(">>此算法为根据16位十六进制初始密钥,求16轮子密钥。")
    #key=input(">>请输入初始密钥（例：0xfedcba9876543210)：")
    key=0xfedcba9876543210
    k=htob(key)

    s=deskey(k)

    for i in range(0,16):
        print("第%d轮子密钥:"%(i+1))
        h=btoh(s[i])
        print("%d位十六进制表示为:%s"%(len(h)-3,h))
        print("%d位二进制表示为:%s\n"%(len(s[i]),s[i]))

if __name__ == '__main__':
    main()
