import matplotlib.pyplot as plt
import numpy as np

X = np.array([1, 2, 3])
prob = np.array([0.45, 0.23, 0.32])

cdf = np.cumsum(prob)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.stem(X, prob, basefmt=" ", linefmt='b-', markerfmt='bo')
ax1.set_title('Probability Mass Function (PMF)', fontsize=14)
ax1.set_xlabel('Random Variable X', fontsize=12)
ax1.set_ylabel('Probability P(X=x)', fontsize=12)
ax1.set_xticks(X)
ax1.set_ylim(0, 0.5)
ax1.grid()


x_step = [0, 1, 2, 3, 4]
y_step = [0, cdf[0], cdf[1], cdf[2], cdf[2]]

ax2.step(x_step, y_step, where='post', color='r', linewidth=2)

ax2.plot(X, cdf, 'ro') 

ax2.set_title('Cumulative Distribution Function (CDF)', fontsize=14)
ax2.set_xlabel('Random Variable X', fontsize=12)
ax2.set_ylabel('Cumulative Probability P(X <= x)', fontsize=12)
ax2.set_xticks(x_step)
ax2.set_ylim(0, 1.1)
ax2.grid()

plt.tight_layout()
plt.savefig("../figs/fig.png")
plt.show()