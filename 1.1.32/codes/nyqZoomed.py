import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

num = [1]
den = [1, 3, 2, 0] 

G = ctrl.TransferFunction(num, den)

plt.figure(figsize=(8, 6))

ctrl.nyquist_plot(G)

plt.axvline(x=-0.75, color='red', linestyle='--', label='Asymptote')

plt.xlim(-1, 0) 
plt.ylim(-10, 10)

plt.title("Nyquist Plot with Low-Frequency Asymptote")
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.grid(True, which='both', linestyle=':', alpha=0.6)
plt.legend()
plt.savefig('../figs/plt1.png')
plt.show()