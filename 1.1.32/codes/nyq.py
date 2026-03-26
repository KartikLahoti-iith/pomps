
import control as ctrl
import matplotlib.pyplot as plt

num = [1]
den = [1, 3, 2, 0]  # s(s+1)(s+2) = s^3 + 3s^2 + 2s

G = ctrl.TransferFunction(num, den)

ctrl.nyquist_plot(G)

plt.title("Nyquist Plot")
plt.grid()
plt.show()

