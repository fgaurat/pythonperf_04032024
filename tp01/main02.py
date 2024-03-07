
# def mult2(i):
#     return i*2

from collections import deque

# def hello(name,firstName):
def hello(**d):  # hello(name="",firstName="",age=47)
    print("Hello",d['name'],d['firstName'])


def hellokw(*,name,firstName):
    print("Hello",name,firstName)
      
    
def f():
    return 1,2

def add(*l):
    a = 0
    for i in l:
        a+=i
        
    return a

def main():
    l = [10,20,30,40]  
    
    v = add(*l)
    print(v) # 100
    
    v = add(10,20,30,40)
    print(v) # 100
    l2 = [10,20,5,8,7,8]
    a,b,c,*d = l2
    print(a,b,c,d)
    # a,b=0,1
    
    # a,b= f()
    # print(a,b)
    hello(firstName= "fred",name="Gaurat")
    d = {
        "name":"Gaurat",
        "firstName":"fred",
        "age":47
    }
    # hello(**d)# 
    # hello(firstName= "fred",name="Gaurat",age=47)
    hellokw(firstName= "fred",name="Gaurat")
    
def main02():
    l = [10,20,30,40]
    l.append(50)
    print(l)
    last = l.pop()    
    print(last)
    print(l)
    l.insert(0,0)
    print(l)
    first = l.pop(0)
    print(first)
    print(l)
    
    d = deque(l)
    print(d)
    d.appendleft(0)
    print(d)
    
def main01():
    l = [10,20,30,40]
    r=[]
    
    for i in l:
        r.append(i*2)
    print(r)
    
    m = list(map(lambda i:i*2,l))
    print(m)
    
    c = [i*2 for i in l]
    
    
    lines = ["  ligne 01 ","ligne 02    ","   ligne 03"]
    cleanlines = [line.strip() for line in lines]
    print(cleanlines)
    
    
if __name__=='__main__':
    main()
