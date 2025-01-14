import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters for the simulation
grid_size = 100  # Size of the 2D grid
wave_speed = 1.0  # Speed of wave propagation
time_step = 0.1  # Time step for animation
num_frames = 100  # Number of frames in the animation
epicenter = (50, 50)  # Coordinates of the earthquake epicenter

# Create a 2D grid
x = np.linspace(0, grid_size, grid_size)
y = np.linspace(0, grid_size, grid_size)
X, Y = np.meshgrid(x, y)

# Calculate distance of each point from the epicenter
distance = np.sqrt((X - epicenter[0])**2 + (Y - epicenter[1])**2)

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.set_title("Seismic Wave Propagation Simulation")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Initialize the wave image
wave = ax.imshow(
    np.zeros((grid_size, grid_size)), 
    extent=(0, grid_size, 0, grid_size), 
    origin="lower", 
    cmap="viridis", 
    vmin=0, 
    vmax=1
)

# Update function for the animation
def update(frame):
    time = frame * time_step
    wave_amplitude = np.sin(2 * np.pi * (distance - wave_speed * time)) * np.exp(-0.05 * distance)
    wave.set_data(wave_amplitude)
    return wave,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=50, blit=True
)

# Show the animation
plt.colorbar(wave, ax=ax, label="Wave Amplitude")
plt.show()
