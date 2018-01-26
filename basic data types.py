Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 1
>>> b = 1.5
>>> c = "abc"
>>> print"Hello"
Hello
>>> 
>>> print"abc"
abc
>>> type(a)
<type 'int'>
>>> type(b)
<type 'float'>
>>> type(c)
<type 'str'>
>>> a = []
>>> b = ()
>>> c = {}
>>> type(a)
<type 'list'>
>>> type(b)
<type 'tuple'>
>>> type(c)
<type 'dict'>
>>> a = ["abc", 1,5.6]
>>> a[1]
1
>>> a[2]
5.6
>>> len(a)
3
>>> a[0]
'abc'
>>> a.
SyntaxError: invalid syntax
>>> a.append(22)
>>> a
['abc', 1, 5.6, 22]
>>> a.append("xyz")
>>> a
['abc', 1, 5.6, 22, 'xyz']
>>> a.append(1,2)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.append(1,2)
TypeError: append() takes exactly one argument (2 given)
>>> a.count
<built-in method count of list object at 0x02735378>
>>> a.count()

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.count()
TypeError: count() takes exactly one argument (0 given)
>>> a.extend([22,3333])
>>> a
['abc', 1, 5.6, 22, 'xyz', 22, 3333]
>>> a.insert (3,4)
>>> a
['abc', 1, 5.6, 4, 22, 'xyz', 22, 3333]
>>> a.remove(22)
>>> a
['abc', 1, 5.6, 4, 'xyz', 22, 3333]
>>> a.pop()
3333
>>> a.index()

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.index()
TypeError: index() takes at least 1 argument (0 given)
>>> a.index(1)
1
>>> a.index(4)
3
>>> a.sort()
>>> a
[1, 4, 5.6, 22, 'abc', 'xyz']
>>> a.count()

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.count()
TypeError: count() takes exactly one argument (0 given)
>>> a.count
<built-in method count of list object at 0x02735378>
>>> a.count()

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.count()
TypeError: count() takes exactly one argument (0 given)
>>> a.count(1)
1
>>> a
[1, 4, 5.6, 22, 'abc', 'xyz']
>>> a.index(1)
0
>>> a.(12)
SyntaxError: invalid syntax
>>> a=12
>>> for i in range(1,10);
SyntaxError: invalid syntax
>>> a=12
>>> number =raw_input("enter number")
enter number1212
>>> type(number)
<type 'str'>
>>> 
