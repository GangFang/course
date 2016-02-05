# special-notes

1. usage of print:  
in[1]: `print 'A'.lower() in 'aeiou'`  
out[1]: `True`

2. difference between _just output_ and _rebind_  
in[2]:

```python
str1 = 'terminate'
str1.swapcase()			# just output, but not rebind; `str1` no change
print str1
str1 = str1.swapcase()		# rebind, change `str1`
print str1
```
out[2]:

```
terminate
TERMINATE
```

3. comparison among  
`listA.sort   # this returns the function type <function sort>`  
`listA.sort()   # this returns None` 

```python
listA.sort()
listA   # this returns the sorted listA
```

4. comparison between  
`3/2   # return 1`  
`-3/2   # return -2`