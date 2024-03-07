import lemodule
import sys
import copy
b=13

def main01():
    global b
    print(b)
    b=1456
    if True:
        a=2
    print(a)


def main02():
    print("nb ref 2",sys.getrefcount(2))
    a=2
    print("nb ref 2",sys.getrefcount(2))

    print(a)
    print(hex(id(a)))
    a=3
    print(a)
    print(hex(id(a)))
    # s = "toto"
    # print(s)
    # s[0] = 'J'
    # print(s)
    b=3
    print(b)
    print(hex(id(b)))    


def main():
    l = [10,20,30,40,50]
    l[0] = 1000
    print(l[1:4])
    print(l[-1])
    
    print(l[:3])
    print(l[3:])
    l1 = l[:3]
    l1[0] = 10
    print(l)
    print(l1)
    
    
    
    l = [
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]
    
    # l1 = l[:]
    l1 = copy.deepcopy(l)
    l[0][0] = 1000
    print(l)
    print(l1)
    
if __name__=='__main__':
    # print(b)
    main()
    # print(b)


