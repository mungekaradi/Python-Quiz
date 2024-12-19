print(2**3);        # o/p: 8

print("A"*3);        # o/p: AAA

x= [1,2,3]
print(x[1]);        # o/p: 2

print("Python"[2:])        # o/p: thon

print(len([1,2,3,4]));        # o/p: 4

print(10 // 3);        # o/p: 3

x= "Coding"
print(x[1:4]);        # o/p: odi

x= [10,20,30]
print(x.pop(),x);        # o/p: 30 [10, 20]

a= [1,2,3]
b= a+[4,5]
print(b);        # o/p: [1, 2, 3, 4, 5]

name= "Aditya"
print(name.upper());    # o/p: ADITYA

x= 3
y= 4
print(x**y);        # o/p: 81

print(bool(0), bool(1), bool(-1));        # o/p: False True True

print(2*3+4);        # o/p: 10

a= 10
b= 20
print(a+b*0);        # o/p: 10

print("A", "B", "C", sep="-");        # o/p: A-B-C

x=10
print("Even" if x%2==0 else "Odd");        # o/p: Even

print("Python"*2);        # o/p: PythonPython

nums= [1,2,3]
nums.append(4)
print(nums);        # o/p: [1, 2, 3, 4]

x= [1,2,3,4]
print(x[-1] + x[-2]);        # o/p: 7

for i in range(3):
    print(i, end=" ");        # o/p: 0 1 2

x= "abc"
y= x*2
print(y[::-1]);        # o/p: cbacba

def fun(a, b=2, c=3):
    return a+b*c
print(fun(1));        # o/p: 7

a= [1,2,3]
b=a
b[0]=99
print(a);        # o/p: [99, 2, 3]

x= 5
x+= 3
print(x);        # o/p: 8

my_list= [1,2,3]
print(len(my_list));        # o/p: 3

print("python"[0]);        # o/p: p

a= 5
def change_value():
    a= 10
    print(a);
change_value()
print(a);        # o/p: 10

a= 10
b= 5
print(a-b);        # o/p: 5

x= [1,2,3]
x +=[4]
print(x);        # o/p: [1, 2, 3, 4]

text= "Programming"
print(text[4:8]);        # o/p: ramm

def add(a,b):
    return a+b
print(add(3,7));        # o/p: 10

numbers= [1,2,3,4]
print(numbers[2]);        # o/p: 3

x= 8
y= 3
print(x // y);        # o/p: 2

for i in range(4):
    print(i, end=" ");        # o/p: 0 1 2 3 

def add(a,b):
    return a + b
print(add(4,5));        # o/p: 9

x= 2        
y= 4
if x < y:
    print("x is less than y");        # o/p: x is less than y
else:
    print("x is greater than or equal to y");

for i in range(3):
    print("Python",end=" ");        # o/p: Python Python Python John

names= ["John", "Aditya", "Sara"]
print(names[0]);                    # o/p: John

x= "Python"
print(x[2:]);        # o/p: thon

x= "HELLO"
print(x.lower());        # o/p: hello

x= "hello"
y= x.upper()
print(y);            # o/p: HELLO

def greet(name):
    return "Hello" + name
print(greet("Aditya"));        # o/p: HelloAditya

def multiply(a,b):
    return a * b
print(multiply(3,4));        # o/p: 12

x= "123"
y= int(x)+2
print(y);            # o/p: 125

x= 5
y= "5"
print(x + int(y));        # o/p: 10

print(5==5);        # o/p: True

for i in range(1,4):
    print(i,end=" ");        # o/p: 1,2,3

print(bool(1));        # o/p: True

x= [1,2,3]
print(x[-2]);        # o/p: 2

a= [1,2,3]
a.insert(1,4)
print(a);        # o/p: [1, 4, 2, 3]

x= 4
y= 4
print(x==y);        # o/p: True

x= [1,2,3,4,5]
print(sum(x));        # o/p: 15

def func(x, y=[]):
    y.append(x)
    return y
print(func(x));        
print(func(y));       # o/p: [[1, 2, 3, 4, 5]] 
                            [[1, 2, 3, 4, 5], 4]


print("Hello\nAditya");        # o/p: Hello
                                      Aditya

print("Hello\tAditya");        # o/p: Hello	Aditya

color= ["Red","Green","yellow"]
x= len(color)
print(x);                            # o/p: 3

color= ["Red","Green","yellow","blue"]
for x in color:
    print(x,end=" ");                    # o/p: Red Green yellow blue

color= ["Red","Green","blue","yellow"]
color.append("pink")
print(color);                            # o/p: ['Red', 'Green', 'blue', 'yellow', 'pink']

color= ["Red","Green","yellow"]
color.pop(2)
print(color);                        # o/p: ['Red', 'Green']

list= ["grapes","banana","apple","mango","kiwi"]
list.sort()
print(list);                        # o/p: ['apple', 'banana', 'grapes', 'kiwi', 'mango']

list= ["red","green","yellow"]
list.remove("green")
print(list);                        # o/p: ['red', 'yellow']

list= ["Red","green","blue"]
list1= [4,14,20]
list.extend(list1)
print(list);                        # o/p: ['Red', 'green', 'blue', 4, 14, 20]

list= ["Red","green","blue"]
list.reverse()
print(list);                        # o/p: ['blue', 'green', 'Red']

x= "22_22"
print(float(x));                # o/p: 2222.0

total= 0
for i in range(1,6):
    total+= i
print(total);                    # o/p: 15

print(3*(2+4));                # o/p: 18

var= "James"*2*3
print(var);                    # o/p: JamesJamesJamesJamesJamesJames

p,q,r= 10,20,30
print(p,q,r);            # o/p: 10 20 30

valueone= 5**2
valuetwo= 5**4
print(valueone);
print(valuetwo);        # o/p: 25 625

x= 12
print(type(x));        # o/p: <class 'int'>

x= "aditya"
print(type(x));        # o/p: <class 'str'>

x= 14.99
print(type(x));        # o/p: <class 'float'>

print("Aditya" + "Mungekar");        # o/p: AdityaMungekar

tuple1= (10000,20000,30000,40000,50000)
for i in tuple1:
    print("Salary of employees",i);       '''  o/p: Salary of employees 10000
                                                    Salary of employees 20000
                                                    Salary of employees 30000
                                                    Salary of employees 40000
                                                    Salary of employees 50000   '''
    
emptytuple=()
print(emptytuple);            # o/p: ()

onevaluetuple=(49)
print(onevaluetuple);        # o/p: 49

def allnum(*args):
    print(args);
allnum(3,2.0,"4")        # o/p: (3, 2.0, '4')

a= 4
b= 5
temp= a
a=b
b= temp
print(a,b);        # o/p: 5 4

x= "Ayesha"
print(x[2:3]);        # o/p: e

s= "Coding"
print(s[10 : 0 : -1]);        # o/p: gnido

s= "aditya"
print(s.upper());        # o/p: ADITYA

s= "ADITYA"
print(s.lower());        # o/p: aditya

s= "aditya mungekar"
print(s.capitalize());        # o/p: Aditya mungekar

a= "Mumbai"
a1= "University"
print(a+a1);            # o/p: MumbaiUniversity

thisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
print(len(thisdict));        # o/p: 3

thisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
print(type(thisdict));        # o/p: <class 'dict'>

thisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
x= thisdict["model"]
print(x);                    # o/p: mustang

thisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
x= thisdict.keys()
print(x);                # o/p: dict_keys(['brand', 'model', 'year'])

thisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
x= thisdict.values()
print(x);                # o/p: dict_values(['ford', 'mustang', 2020])

fruits= ["Apple","Banana","Mango"]
for x in fruits:
    print(x,end=" ");        # o/p: Apple Banana Mango

print(5**10);        # o/p: 9765625

printthisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
x= thisdict.keys()
print(x);                # o/p: dict_keys(['brand', 'model', 'year'])

fruits= ["Apple","Banana","Mango"]
for x in fruits:
    print(x,end=" ");        # o/p: Apple Banana Mango

print(5**10);                # o/p: 9765625

print(1000 / 4);        # o/p: 250.0

x=2j
print(x);
print(type(x));    ''' o/p: 2j
                            <class 'complex'> '''

x= True
print(x);
print(type(x));      ''' o/p: True
                              <class 'bool'> '''

x= None
print(x);
print(type(x));      ''' o/p: None
                        <class 'NoneType'> '''

x= ["BMW","Audi","volvo","Ferrari"]
print(x);
print(type(x));            ''' o/p: ['BMW', 'Audi', 'volvo', 'Ferrari']
                                    <class 'list'> '''

print(5 + 6 * 2);           # o/p:  17

print(99.4 * 20);        # o/p: 1988.0

print("My\n\tFamily");      ''' o/p: My
	                                    Family '''

print("god is great");       # o/p:  god is great

x= 44.9
print(type(x));        # o/p: <class 'float'>

m= 60
if m>=50:
    print("pass")
else:
    print("fail")        # o/p: pass

a= 70
if a>=60:
    print("retired")
else:
    print("not retired")        # o/p: retired

p= 78
if m>=90:
    print("excellent")
elif (p>=80 and p<90):
    print("very good")
elif (p>=70 and p<80):
    print("good")
elif (p>=60 and p<70):
    print("average")
else:
    print("poor")            # o/p: good















    















    


































       















    



















































    





















































































































































































































































































































































































































































































































































































      
