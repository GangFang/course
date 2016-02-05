# keywords-functions
---
*structure: a key word is presented, followed by an example*

---
keywords

1. `global`  
in[1]:

	```python
	a_var = 'global value'
	
	def a_func():
		global a_var
		a_var = 'local value'
		print(a_var, '[ a_var inside a_func() ]')
	
	print(a_var, '[ a_var outside a_func() ]')
	a_func()
	print(a_var, '[ a_var outside a_func() ]')
	```
	out[1]:
	
	```python
	global value [ a_var outside a_func() ]
	local value [ a_var inside a_func() ]
	local value [ a_var outside a_func() ]
	```
2. `is` operator
	- the difference between `is` and `==`
		- `==` will check if the two objects are equal. 
		- `is` will check if they are the exact same object in memory.
		- ex:

	```python
	a = [1, 2, 3]
	b = a
	
	b is a 
	Out[]: True
	
	b == a
	Out[]:True
	
	b = a[:]
	
	b is a
	Out[]: False
	
	b == a
	Out[]: True	
	```

---

Built-in Functions

1. `range(p1,p2,p3)`
	- 1st ex:
		- in[]: `range(10, 3, -1)`
		- out[]: `[10, 9, 8, 7, 6, 5, 4]`
	- 2nd ex:
		- in[]: `range(10, 3)`
		- out[]: `[]`
	- 3rd ex:
		- in[]: `range(3, 10.5, 0.5)`
		- out[]: `error`