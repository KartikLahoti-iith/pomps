import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0.01, 1.0, 1000)

s = 1j * w
G = 1 / (s * (s + 1) * (s + 2))

x_exact = np.real(G)
y_exact = np.imag(G)

x_asymp = np.full_like(w, -0.75) 
y_asymp = -1 / (2 * w)

plt.figure()

plt.plot(x_exact, y_exact, label='Exact $G(j\omega)$', color='blue')
plt.plot(x_asymp, y_asymp, label='Asymptote $x = -3/4$', color='red', linestyle='--')

plt.title('Nyquist Plot Low-Frequency Asymptote ($\omega \\rightarrow 0^+$)')
plt.xlabel('Real Part: $Re(G)$')
plt.ylabel('Imaginary Part: $Im(G)$')
plt.grid()
plt.legend()
plt.xlim(-1.5, 0.5)
plt.ylim(-15, 0) 

plt.savefig("../figs/plt1.png")
plt.show()
