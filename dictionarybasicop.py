Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=dog

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x=dog
NameError: name 'dog' is not defined
>>> x = dog

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x = dog
NameError: name 'dog' is not defined
>>> cont={'first'='shital' ,'last'='gorhe' ,'age'=22, 'registered'='true' }
SyntaxError: invalid syntax
>>> cont={'first':'shital', 'last':'gorhe', 'age':22, 'registered':'true'}
>>> cont
{'age': 22, 'last': 'gorhe', 'registered': 'true', 'first': 'shital'}
>>> del cont['first']
>>> cont
{'age': 22, 'last': 'gorhe', 'registered': 'true'}
>>> cont ['age']=30
>>> cont
{'age': 30, 'last': 'gorhe', 'registered': 'true'}
>>> cont ['salary']=30000
>>> cont
{'salary': 30000, 'age': 30, 'last': 'gorhe', 'registered': 'true'}
>>> 'first' in cont
False
>>> 'salary' in cont
True
>>> phonebook={
	'jhon':123456
	'jack':789000
	
SyntaxError: invalid syntax
>>> phonebook={'jhon':324, 'jack':123, 'jill':345 }
>>> phonebook
{'jill': 345, 'jhon': 324, 'jack': 123}
>>> phonebook ['jeesy']=456
>>> phonebook
{'jeesy': 456, 'jill': 345, 'jhon': 324, 'jack': 123}
>>> del 'jill' in phonebook
SyntaxError: invalid syntax
>>> del phonebook["jill"]
>>> phonebook
{'jeesy': 456, 'jhon': 324, 'jack': 123}
>>> 
