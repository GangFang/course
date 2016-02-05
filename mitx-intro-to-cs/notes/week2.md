# week 2
## lec 4 - functions
### intro
1. black box ==abstraction==
	- build a collection of such abstractions to do complex computation
	- reuse this abstraction
2. ==environment==

### Creating functions
1. ==Turing complete==
	- the set of tools: numbers, assignments, input/output, comparsions, looping constructs
2. it is enough? -- no, we lack abstaction
	- why? -- hard to maintain, cant use same variable names, piece of code cant be reused
3. Func give us abstraction -> treat that as a primitive
4. Syntax: `<func-name>(<formal para1>,...,<formal paran>)`

	```python
def max(x, y):
	if x > y:
		return x
	else:
		return y
```
5. _func returns_ _(remember: a func must return something!)_
	- _None_ if run out of expressions
	- until 'return' is reached

*Note1: docstrings*  

```python
def myFunction(argument):
   """
   Docstring goes here. Explain what type argument(s) should have, and what your function
   is going to return.
   """
   < Code for your function (the body of the function) goes here >
```
### environments
**to understand how bindings of vriables take place**

1. def of environments: env are formalism for tracking bindings of variables and values
2. Py shell is default (global) env
3. `def` _pair function name with details of function (what we call procedural object)_
4. so when we involve (call) a function, this is what happens:  
	1. evaluate `<expr0>(<expr1>,...,<exprn>)`
	2. pair `<expr0>` which is `max` with `Procedure1`
	3. evaluate `<expr1>` which is `3`, `<expr2>` which is `4`
	4. **create a new env `E2`**, pair `<expr1>` with `3` and `<expr2>` with `4` in `E2`
	4. evaluate body
	![call function](/Users/gang_fang/documents/stem/course/mitx-intro-to-cs/img/call-func.png)
5. the arrow pointing from Procedure1 back to E1 is called *environment pointer*; it tells the
	context relative to which I want to evaluate the procedural object

### namespaces, scope resolution, and the LEGB rule
1. ==Namespace==: container for mapping names to objects  
	* namespaces are currently implemented as dictionaries in Python
	`a_namespace = {'name_a':object_1, 'name_b':object_2, ...}`
	* namespaces can exist independently from each other
2. ==Scope==: defines the "hierarchy level" in which we search namespaces  

--
Q: Given the concepts of namespace and scope, the next question is: "In which order does Python 
search the different levels of namespaces before it finds the name-to-object' mapping?"  
Ans: **Local -> Enclosed -> Global -> Built-in** ( so called ==LEGB rule== )

### the necessity of function

1. **essence: it create new procedures and treat as if python primitives**  

2. properties:
	- ==Decomposition==: break problems into modules that are self-contained, and can be **reused**
	- ==Abstraction==: Hide details. _User_ need not konw interior details, can just use as if a black box with *specification (the instruction written below the `def` bounded by a set of triple quotation marks, which specifies the 'assumption' and 'guarantee')*

	
### modules
1. what is modules? -- modularity suggests grouping **functions** together that share **common theme**
2. how to create them? -- Place all those functions in a single **.py** file
3.  how to use them? -- use `import` command to access
	1. `import circle`
	2. `from circle import`

*Note1: `print circle.area(3)` the '.' notatoin specifies context from which to read values. here is the module `circle`*  
*Note2: I can overwirte value for a variable which has been assigned to a certain value in the imported module*