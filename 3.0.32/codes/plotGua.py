import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

X = [1, 2, 3]
prob = [0.45, 0.23, 0.32]

samples = 10000000

data = np.random.choice(X, size=samples, p=prob)

mu = np.mean(data)
sigma = np.std(data)

print(f"Theoretical Mean: 1.870  | Simulated Mean: {mu:.3f}")
print(f"Theoretical Std:  0.868  | Simulated Std:  {sigma:.3f}")

plt.figure(figsize=(10, 6))

bins = [0.5, 1.5, 2.5, 3.5]

plt.hist(data, bins=bins, density=True, alpha=0.5, color='blue', 
         edgecolor='black', label='Simulated Data Histogram')

x_axis = np.linspace(0, 4, 100)
gaussianCurve = norm.pdf(x_axis, mu, sigma)


plt.plot(x_axis, gaussianCurve, 'r-', linewidth=2, 
         label=f'Gaussian Overlay\n($\mu$={mu:.2f}, $\sigma$={sigma:.2f})')

plt.axvline(1.87,color = "yellow",linewidth=1)

plt.axvline(mu,color = "green",linewidth=1)

plt.title('Simulation of Discrete PMF vs Continuous Gaussian Overlay', fontsize=14)
plt.xlabel('Random Variable X', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.xticks(X)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("../figs/plt.png")
plt.show()