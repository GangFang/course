# week3

# lecture 5 - recursion

**function->iterative computations->recursion->induction&why work->design recursion algo->classic recursion algo**

## iterative algorithms

1. iterative algorithm
2. "state variables"
	* have a beginning
	* state being updated
	* have an end

## recursive algorithms

_def of recursion: recursion is a method of defining functions in which the function being defined is applied within its own definition_

**think recursively: reduce the problem to a simpler version of the same problem plus some operations I know how to do**

1. recursive step ("think recursively" above)
2. base case: computations that are easy enough to solve directly

## using env to understand recursion
this pic perfectly describes the whole process of recursion calls

![recursion-env](/Users/gang_fang/documents/stem/course/mitx-intro-to-cs/img/recursion-env1.png)

> * Each recursive call to a funcDon creates its own environment, with local scoping of variables  * Bindings for variable in each frame disDnct, and not changed by recursive call  * Flow of control will pass back to earlier frame once funcDon call returns value

## inductive reasoning

1. why it will stop?  
	ans: given the base case, we know recursive algorithms will **terminate**
2. why it will return correct answer?
	* first, given the base case, we are sure that it will return the correct answer for base case
	* second, let assume `recurMul(a, b-1)` will return correct answer, since `recurMul(a, b)` will return `a + recurMul(a, b-1)`, `recurMul(a, b)` will also return correct answer

## factorial (a classic recursive problem)

comparison(form):

* iterative code: state variables
* recursive code: base case plus _recursive step_(the simpler version of the same problem and an additional computation)

## towers of hanoi

**important: when writing recursive code, note that the function() we define is ABLE to perform the task that we want. So simply reuse it within the definition of itself**

```python
c = 0  # 'c' is used to count the number of moves

def towers(n, fr, to, spare):
    if n == 1:
        print 'move from ' + str(fr) + ' to ' + str(to)
	global c
	c += 1
	print 'count: ' + str(c)  	
    else:
	towers(n-1, fr, spare, to)
	towers(1, fr, to, spare)
	towers(n-1, spare, to, fr)
		
# invoke the towers funciton
towers(15, '1', '3', '2')
```

## fiboncci - recursion with _multiple_ base cases

1. description of the problem
2. multiple base cases:
	- females(0) = 1
	- females(1) = 1

## recursion on strings

1. base case:
2. recursive step

3. comparison: inconvenient vs. convenient

```python
length = 0

def lenRecur(aStr):
    '''
    aStr: a string
    returns: int, the length of aStr
    '''
    global length
    
    if aStr == '':
        return length
    else:
        aStr = aStr[1:]
        length = length + 1
        return lenRecur(aStr)

```

```python
def lenRecur(aStr):
    '''
    aStr: a string
    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0

    return 1 + lenRecur(aStr[1:])
```

From the observation, using ==global variables== is always
a bit risky. So if there are a few things that you need to check the first time you look at the inputs that you should not check on subsequent recursive calls, the other two ways are to ==use keyword arguments== and to ==use a wrapper function==

## global variables

1. usage: count the number of times a recursion function calls itself recursively
2. comments:
	- **use with care**!!
	- destroy locality of code -> introduce bugs

# lecture 6 - objects

**keyword: compound data types (tuples, lists and dictionary), operations on them, creating and manipulating them**

*note2: the opposite of compound data objects: _scalar objects_*

## tuples

1. def: ordered sequence of elements which can be more than just characters
	- more complicated structure: nested tuples
3. operations on tuples
	- concatenation `(t1+t2)`
	- indexing `(t1+t2)[3]`
	- slicing  `(t1+t2)[1:3]`
	- singletons	`('five',)`
		- `,` used in singletons: to distinguish itself from `('five')`
	- empty tuples `em = ()`
4. manipulating tuples
	- we can **iterate** over tuples

*Note1: when using slicing, like `x[0:1]`, we get a tuple instead of the element, which is resulted from `x[0]`*
*Note2: 'tuple' object does not support item assignment*


## lists

1. small/look diff:
	- singletons: [4] rather than (4,)
2. big diff: lists are **mutable**; tuples are not
	- some data objects we want to treat as fixed
		- this will be valuable when these objects will be referenced frequently but elements don't change
	- some data objects may want to support _modifications to elements_ for efficiency
		- great flexibility but more prone to bugs
3. the inner workings of changing a list and creating a new list
	- ![list-mutate](/Users/gang_fang/Desktop/list-mutate.png)
	- ==aliasing==: two distinct **paths share** the **same one** data object
	- we can mutate object through **either** path, but effect will be visible through **both**

	
## operations on lists

1. iteration
2. flattening vs. append
	- flattening/concatenation
		- use `<list3>=<list1>+<list2>`
		- **essentially create a new list, and assgin `<list3>` to it**
	- append
		- `<list>.append()`
		- **essentially mutate the original list**
3. ==clone==
	- bkg: we have to avoid mutating a list over which one is iterating. Like this:
	
	```python
	def removeDups(L1, L2):
		for e1 in L1:
			if e1 in L2:
				L1.remove(e1)
				
	L1 = [1,2,3,4]
	L2 = [1,2,5,6]
	removeDups(L1, L2)
	
	Out[]: [2,3,4]
	```
	- this is because after the first iteration, `L1` is mutated and became `L1 = [2,3,4]` while the internal counter is still pointing to `L1[1]`, which is `3`
	- use `L1Start = L1[:]`, then we make a _copy_ of `L1` and assign L1Start to it
	- _using `L1Start = L1`_ will be useless because `L1Start` will point to the value pointed to by `L1`, which is the list itself


## functions as objects

1. ==fist class objects==
	- properties
		- have types
		- can be elements of data structures like lists
		- can appear in expressions
			- as part of an assignment statement
			- _as an argument to a function_
2. ==higher order programming==
	- useful to use func as argu when coupled with lists (we treat func as if they are elements of data structures)
	- example

	```python
	def applyToEach(L, f):
		for i in range(len(L)):
			L[i] = f(L[i])
			
	applyToEach(L, abs)
	print(L)
	
	Out[]:[1,2,3.39999999]
	```
3. lists of functions
	
	```python
	def applyFUnc(L,x):
		for f in L:
			print(f(x))
			
	applyFuns([abs, int, fact, fib],4)
	4
	4
	24
	5
	```
4. generalizations of higher order functions
	- a general purpose HOP, `map`
	- general form: an n-ary func and n collections of arguments
	
	```python
	L1 = [1,28,36]
	L2 = [2,57,9]
	map(min, L1, L2)
	
	Out[]: [1,28,9]
	```
	

## dictionaries

1. def: Dict is generalization of lists, but now indices don't have to be integers, it can be values of any _immutable type_
2. refer to indices as **keys** in _arbitrary in form_
3. syntax
	
	```python
	dict_test = {'jan':1, (1,2,3): [21,2], 3: 'fed'}
	```
	
4. entries in a dict are _unordered_  
5. can be accessed by a **key** not an **index**  
6. operations
	- insertion  `dict_test['abc'] = 5`
	- iteration
7. dict can be **complex**, where a key can be a tuple
	- a key has to be immutable