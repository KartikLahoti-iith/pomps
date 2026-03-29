import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy import signal

# --- 1. Linearization (Theoretical K values) ---
# Option A: g'(x) = 6 - 3/x^2  --> K = 17/3 (~5.667)
# Option B: g'(x) = 1/sqrt(3+2x) --> K = 1/3  (~0.333)
# Option D: g'(x) = x            --> K = 3.0
# Custom M: g(x) = 9/x -> g'(x) = -9/x^2 --> K = -1.0

options = {
    'Option A (Unstable)': {'K': 17/3, 'color': 'red', 'marker': 'x'},
    'Option B (Stable)':   {'K': 1/3,  'color': 'green', 'marker': 'o'},
    'Option D (Unstable)': {'K': 3.0,  'color': 'orange', 'marker': 's'},
    'Custom M (Marginal)': {'K': -1.0, 'color': 'blue', 'marker': 'd'}
}

for name, data in options.items():
    sys = signal.dlti([1, 0], [1, -data['K']])
    data['system'] = sys
    data['pole'] = sys.poles[0]

fig = plt.figure(figsize=(15, 7))
gs = GridSpec(1, 2, width_ratios=[1, 1.2], wspace=0.3)
ax_z = fig.add_subplot(gs[0])
ax_time = fig.add_subplot(gs[1])

ax_z.set_title("Z-Domain Stability Map (System Poles)")
ax_z.set_xlabel("$\mathcal{R}e\{z\}$")
ax_z.set_ylabel("$\mathcal{I}m\{z\}$")
ax_z.axis('equal')
ax_z.set_xlim(-6.5, 6.5) 
ax_z.set_ylim(-6.5, 6.5)
ax_z.grid(True, linestyle=':', alpha=0.6)

uc = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--', linewidth=2)
ax_z.add_artist(uc)
theta_uc = np.linspace(0, 2*np.pi, 200)
ax_z.fill(np.cos(theta_uc), np.sin(theta_uc), color='green', alpha=0.1, label='Stable ($|z|<1$)')

ax_z.axhline(0, color='k', linewidth=1)
ax_z.axvline(0, color='k', linewidth=1)

for name, data in options.items():
    p = data['pole']
    ax_z.plot(np.real(p), np.imag(p), data['marker'], markersize=10, 
              color=data['color'], markeredgecolor='k', 
              label=f"{name}: Pole at {np.real(p):.2f}")

ax_z.legend(loc='upper right')

ax_time.set_title("Time-Domain Error Response (Log Scale)")
ax_time.set_xlabel("Iteration Step ($n$)")
ax_time.set_ylabel("Error Magnitude Multiplier $|K|^n$")
ax_time.grid(True, linestyle=':', alpha=0.6)

num_steps = 10
for name, data in options.items():
    t, y = signal.dimpulse(data['system'], n=num_steps)
    
    response = np.abs(np.squeeze(y))
    
    ax_time.plot(t, response, marker=data['marker'], color=data['color'], 
                 linestyle='-', linewidth=2, label=name)

ax_time.set_yscale('log')
ax_time.legend()

plt.tight_layout()
plt.savefig("../figs/plt2.png")
plt.show()