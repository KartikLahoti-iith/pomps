import numpy as np
import matplotlib.pyplot as plt

xStar = 3.0
x0 = 3.1 
i = 10

def g_a(x): 
    return -16 + 6*x + 3/x
def g_b(x): 
    return np.sqrt(3 + 2*x)
def g_c(x): 
    return 3/x - x/2
def g_d(x): 
    return (x**2 - 3)/2

functions = {
    'Option A': g_a,
    'Option B': g_b,
    'Option C': g_c,
    'Option D': g_d
}

plt.figure(figsize=(10, 6))
plt.axhline(y=xStar, color='k', linestyle='--', label='Fixed Point ($x^* = 3$)')

for name, g in functions.items():
    if name == 'Option C':
        continue
        
    x_vals = [x0]
    
    try:
        for _ in range(i):
            next_x = g(x_vals[-1])
            if abs(next_x) > 1000:
                break
            x_vals.append(next_x)
            
        plt.plot(range(len(x_vals)), x_vals, marker='o', label=name)
        
    except OverflowError:
        pass 

plt.title("Time-Domain Simulation of Iterative Error")
plt.xlabel("Iteration Step ($n$)")
plt.ylabel("Value ($x_n$)")
plt.ylim(0, 10) 
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("../figs/plt1.png")
plt.show()