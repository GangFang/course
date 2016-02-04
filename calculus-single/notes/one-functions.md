# one - functions

# functions

- function is the main object of the study of calculus
	- study their inner workings
	- also how they interact with other func
	- interpretation of func 
		- graph
		- pair 
		- **input->output**
- concepts of func
	- domain
	- range
- operations of func
	- composition: $(f\bullet g)(x) = f(g(x))$
	- inverse: $f^-1(x)$
- classes of func
	- polynomials $P(x) = c_0+c_1x+...+c_nx^n = \displaystyle\sum_{k=0}^{n} c_kx^k$
	- *note: 'c' is the coefficients/constants*
	- rationals $\frac{P(x)}{Q(x)}$  where both $P$ and $Q$ are polynomials
	- powers (like $x^{-\frac{1}{2}}$)
	- trigs  (like $cos\theta$)
		- inverse trigs $arcsin$
	- exponentials  $e^x$ and $ln x$
		- ==euler's formula==  \\[e^{ix} = cosx + i\cdot sinx\\] where $i = \sqrt{-1}\ and\ i^2 = -1$

_so.. what the heck is $e$?_

# exponentials

**view exponential as a infinite polynomial**

compute
make sense

1. recall:
	- algebraic properties: 
	- diff and integral properties
	- euler's formula
2. def (view exponential as a infinite polynomial) \\[e^x = 1 + x + \frac{1}{2!}x^2 + \frac{1}{3!}x^3 + \frac{1}{4!}x^4 + ... = \displaystyle\sum_{k=0}^{\infty} \frac{x^k}{k!}\\]
3. use the definition above, which $d^x$ is equal to the long _polynomial_, since we know the rule of diff and integral for polynomial, we can compute the $\frac{\mathrm d}{\mathrm d x} e^x$ and $\int \mathrm{e}^{x}\ \mathrm{d}x$ which is $e^x + (c)$ itself
4. Based on the euler's formula, we can derive the $cosx$ and $sinx$ by viewing the $e^{ix}$ as a long polynomial, also in the form of polynomial  \\[sinx = \displaystyle\sum_{k=0}^{\infty} (-1)^k \frac{x^{2k+1}}{(2k+1)!}\\]  \\[cosx = \displaystyle\sum_{k=0}^{\infty} (-1)^k \frac{x^{2k}}{(2k)!}\\]
	- then we can compute the differentiation of trig functions

--

- understanding: why the def of exponentials looks like that? why we want to view exponential as a long polynomial?
	- Ans: the long polynomial is a **approximation** to the expoential. The _more terms_ we include in the polynomial, _the preciser_ the approx.
![approx1](/Users/gang_fang/Documents/STEM/course/calculus-single/img/taylor-approx-1.png)
![approx2](/Users/gang_fang/Documents/STEM/course/calculus-single/img/taylor-approx-2.png)

- remarks:
	1. there approx. are best near **zero** (when x is a large number, we need to include more terms in the poly in order to make the approx. precise)


