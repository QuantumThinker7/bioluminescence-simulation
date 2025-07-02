import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(12.8, 7.2))  # HD resolution approx 1280x720 pixels scaled

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')  # Ocean dark background

# Initialize positions of siphonophores
num_siph = 20
x = np.random.uniform(1, 9, num_siph)
y = np.random.uniform(1, 9, num_siph)

# Create scatter plot with initial sizes and colors (alpha for glow)
scat = ax.scatter(x, y, s=300, c='cyan', alpha=0.5, edgecolors='none')

def update(frame):
    # Pulsing glow effect by changing alpha sinusoidally
    alphas = 0.3 + 0.7 * (np.sin(frame / 10 + np.linspace(0, 2*np.pi, num_siph)) + 1) / 2
    scat.set_alpha(alphas)
    
    # Optional: slight random movement to simulate drifting
    global x, y
    x += np.random.uniform(-0.05, 0.05, num_siph)
    y += np.random.uniform(-0.05, 0.05, num_siph)
    x = np.clip(x, 0, 10)
    y = np.clip(y, 0, 10)
    scat.set_offsets(np.c_[x, y])
    
    return scat,

ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()
