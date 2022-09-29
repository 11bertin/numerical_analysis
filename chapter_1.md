## 3. Show that f‘(x) **has at least one zero in the given interval.**




### $$ f(x)=1-e^x+(e-1)sin\frac{\pi}{2}x ,[0,1]$$

**Proof:** It can be easily verified that $$f(x)$$ is continuous in the interval $$[0,1]$$ and $$f(0)=0$$ and $$f(1)=0$$

So, from Rolle Mean Value Theorem we conclude that there exists one zero $$\xi\in[0,1]$$ such that$$f'(x)=0$$







## 4. Find the 4-th Taylor polynomial for p_4(x) for the function $$f(x)=x{e}^x$$at the point $$x_0=0$$
### (b) approximate $$\int_{0}^{0.4}{f(x){d}x}$$ by using $$\int_{0}^{0.4}{p_\mathbf{4}({x}){d}x}$$
**Solution**: The Taylor polynomial for $$f(x)$$ is as follows, 
$$p_n(x)=f(x_0)+f^\prime(x_0)(x-x_0)+\frac{1}{2}f''(x_0)(x-x_0)^2+\frac{1}{3!}f'''(x_0)(x-x_0)^3+...+\frac{1}{n!}f^{(n)}(x_0)(x-x_0)^n$$  and we can also get 
$$f(0)=0，f'(0)=1，f″(0)=2，f‴(0)=3，f（4）(0)=4 $$
So we have 
$$p_4(x)=x+x^2+\frac{1}{2}x^3+\frac{1}{6}x^4$$.
Therefore,
$$\int_{0}^{0.4}{f(x)dx}\approx\int_{0}^{0.4}{p_4(x)dx}=\int_{0}^{0.4}{(x+x^2+\frac{1}{2}x^3+\frac{1}{6}x^4)dx}= 0.104874666666667$$



### (c) Find the upper bound for the error$$ \left|\int_{0}^{0.4}{f(x)dx}-\int_{0}^{0.4}{p_4(x)dx}\right|$$
**Solution**: From Taylor Theorem, we have
$$\left|f(x)-p_4(x)\right|=|\frac{f(5)(ξ)}{5!}x^5|=|\frac{5ξ+ξe^ξ}{5!}x^5|$$, where  
Therefore, 
$$ \left|f\left(x\right)-p_4\left(x\right)\right|=\left|\frac{5ξ+ξe^ξ}{5!}x^5\right|\leq\left|\frac{5 \times 0.4+0.4 e^{0.4}}{5 !} 0.4^{5}\right|$$
                             $$=0.2215876163 $$ 



## 7. Let $ f(x)=\frac{x*cos(x)-sin(x)}{x-sin(x)}$ .
### a. Find $\lim_{x \to 0} f(x)$.

**Solution** :$lim_{x \to 0}f(x)=lim_{x \to 0}\frac{-xsin(x)}{1-cos(x)}=lim_{x \to 0}\frac{-sin(x)-xcos(x)}{sin(x)}=lim_{x \to 0}\frac{xsin(x)-2cos(x)}{cos(x)}=-2$

### b. Use four-digit rounding arithmetic to evaluate $f(0.1)$.

**Solution** :since $cos0.1=1.000$, $sin0.1=0.001745$

​				  so $f(0.1)=1.00$

### c. Replace each trigonometric function with its third Maclaurin polynomial and repeat part (b).

**Solution** : $sinx=x-\frac{x^3}{3!}+\frac{x^5}{5!}=1-\frac{x^2}{2!}+\frac{x^4}{4!}$

​				  $ f(0.1)=-1.941$

### d. The actual value is $f(0,1)=-1.99899998$.Find the relative error for the values obtained in part(b) and part(c).

**Solution** :The relative errors in part(b) is as follows:
				$e_r=\left|\frac{-1.99899998-1}{1}\right|=2.99899998$

​		         The relative errors in part(c) is as follows:
​			    $e_r=\left|\frac{-1.99899998+1.941}{1.941}\right|=0.02988$

## 8. Assume that the permissible relative error of the volume of a sphere is at most $10^-2$.Determine the permissible relative error of its radius.

**Solution** :$v=\frac{4}{3}\pi r^3$
		   So $\frac{\mathrm{d}R }{R}=\frac{\frac{\mathrm{d}V }{V}}{3}=\frac{0.01}{3}=0.00333$


## 9. The following approximations are obtained by rounding arithmetic, Determine how many significant digits they have respectively.

 $$(a) p_1^*=1.1021$$  $$(b)p_2*=0.031$$     $$(c)p_3^*=56.430$$   $$(d)p_4^*=7\times1.0$$

**Solution** :$$ (a) 5$$  $$  (b) 2$$   $$  (c) 5$$  $$  (d) 2$$       