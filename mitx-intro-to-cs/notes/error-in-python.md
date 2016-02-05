# error-in-python
---
*structure: error name followed by examples followed by explanations*

---  

1. `UnboundLocalError`  
in[1-0]: (good one)

	```python
	a = 1
	
	def err_test(x, y):
		b = a + 1
		print b
	
	err_test(3, 4)
```
out[1-0]:

	```python
	2
	```
in[1-1]: (error)

	```python
	a = 1
	
	def err_test(x, y):
		a = a + 1
		print a
	
	err_test(3, 4)
```
out[1-1]:

	```python
	UnboundLocalError: local variable 'a' referenced before assignment 
	```
**Here is why: in [1-0] 'a' will refer to its global value '1'. However, in [1-1] line 4 implicitly makes 'a' local to err_test so that 'a' will not refer to global value of 'a'. Trying to execute this line will try to read the value of the local variable 'a' before it is assigned, resulting in an `UnboundLocalError `**







