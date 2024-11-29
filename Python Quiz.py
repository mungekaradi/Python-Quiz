print(2**3);

print("A"*3);

x= [1,2,3]
print(x[1]);

print("Python"[2:])

print(len([1,2,3,4]));

print(10 // 3);

x= "Coding"
print(x[1:4]);

x= [10,20,30]
print(x.pop(),x);

a= [1,2,3]
b= a+[4,5]
print(b);

name= "Aditya"
print(name.upper());

x= 3
y= 4
print(x**y);

print(bool(0), bool(1), bool(-1));

print(2*3+4);

a= 10
b= 20
print(a+b*0);

print("A", "B", "C", sep="-");

x=10
print("Even" if x%2==0 else "Odd");

print("Python"*2);

nums= [1,2,3]
nums.append(4)
print(nums);

x= [1,2,3,4]
print(x[-1] + x[-2]);

for i in range(3):
    print(i, end=" ");

x= "abc"
y= x*2
print(y[::-1]);

def fun(a, b=2, c=3):
    return a+b*c
print(fun(1));

a= [1,2,3]
b=a
b[0]=99
print(a);

x= 5
x+= 3
print(x);

my_list= [1,2,3]
print(len(my_list));

print("python"[0]);

a= 5
def change_value():
    a= 10
    print(a);
change_value()
print(a);

a= 10
b= 5
print(a-b);

x= [1,2,3]
x +=[4]
print(x);

text= "Programming"
print(text[4:8]);

def add(a,b):
    return a+b
print(add(3,7));

numbers= [1,2,3,4]
print(numbers[2]);

x= 8
y= 3
print(x // y);

for i in range(4):
    print(i, end=" ");

def add(a,b):
    return a + b
print(add(4,5));

x= 2
y= 4
if x < y:
    print("x is less than y");
else:
    print("x is greater than or equal to y");

for i in range(3):
    print("Python",end=" ");

names= ["John", "Aditya", "Sara"]
print(names[0]);

x= "Python"
print(x[2:]);

x= "HELLO"
print(x.lower());

x= "hello"
y= x.upper()
print(y);

def greet(name):
    return "Hello" + name
print(greet("Aditya"));

def multiply(a,b):
    return a * b
print(multiply(3,4));

x= "123"
y= int(x)+2
print(y);

x= 5
y= "5"
print(x + int(y));

print(5==5);

for i in range(1,4):
    print(i,end=" ");

print(bool(1));

x= [1,2,3]
print(x[-2]);

a= [1,2,3]
a.insert(1,4)
print(a);

x= 4
y= 4
print(x==y);

x= [1,2,3,4,5]
print(sum(x));

def func(x, y=[]):
    y.append(x)
    return y
print(func(x));
print(func(y));

print("Hello\nAditya");

print("Hello\tAditya");

color= ["Red","Green","yellow"]
x= len(color)
print(x);

color= ["Red","Green","yellow","blue"]
for x in color:
    print(x,end=" ");

color= ["Red","Green","blue","yellow"]
color.append("pink")
print(color);

color= ["Red","Green","yellow"]
color.pop(2)
print(color);

list= ["grapes","banana","apple","mango","kiwi"]
list.sort()
print(list);

list= ["red","green","yellow"]
list.remove("green")
print(list);

list= ["Red","green","blue"]
list1= [4,14,20]
list.extend(list1)
print(list);

list= ["Red","green","blue"]
list.reverse()
print(list);

x= "22_22"
print(float(x));

total= 0
for i in range(1,6):
    total+= i
print(total);

print(3*(2+4));

var= "James"*2*3
print(var);

p,q,r= 10,20,30
print(p,q,r);

valueone= 5**2
valuetwo= 5**4
print(valueone);
print(valuetwo);

x= 12
print(type(x));

x= "aditya"
print(type(x));

x= 14.99
print(type(x));

print("Aditya" + "Mungekar");

tuple1= (10000,20000,30000,40000,50000)
for i in tuple1:
    print("Salary of employees",i);

emptytuple=()
print(emptytuple);

onevaluetuple=(49)
print(onevaluetuple);

def allnum(*args):
    print(args);
allnum(3,2.0,"4")

a= 4
b= 5
temp= a
a=b
b= temp
print(a,b);

x= "Ayesha"
print(x[2:3]);

s= "Coding"
print(s[10 : 0 : -1]);

s= "aditya"
print(s.upper());

s= "ADITYA"
print(s.lower());

s= "aditya mungekar"
print(s.capitalize());

a= "Mumbai"
a1= "University"
print(a+a1);

thisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
print(len(thisdict));

thisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
print(type(thisdict));

thisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
x= thisdict["model"]
print(x);

thisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
x= thisdict.keys()
print(x);

thisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
x= thisdict.values()
print(x);

fruits= ["Apple","Banana","Mango"]
for x in fruits:
    print(x,end=" ");

print(5**10);

printthisdict= {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2020
    }
x= thisdict.keys()
print(x);

fruits= ["Apple","Banana","Mango"]
for x in fruits:
    print(x,end=" ");

print(5**10);

print(1000 / 4);

x=2j
print(x);
print(type(x));

x= True
print(x);
print(type(x));

x= None
print(x);
print(type(x));

x= ["BMW","Audi","volvo","Ferrari"]
print(x);
print(type(x));

print(5 + 6 * 2);

print(99.4 * 20);

print("My\n\tFamily");

print("god is great");

x= 44.9
print(type(x));

m= 60
if m>=50:
    print("pass")
else:
    print("fail")

a= 70
if a>=60:
    print("retired")
else:
    print("not retired")

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
    print("poor")















    















    


































       















    



















































    





















































































































































































































































































































































































































































































































































































      
