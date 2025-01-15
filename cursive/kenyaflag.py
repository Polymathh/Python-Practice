import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
import random

# Canvas size
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')  # Hide axes

# Number of shapes
NUM_SHAPES = 150

# Generate random shapes
for _ in range(NUM_SHAPES):
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)
    width = random.uniform(0.5, 2)
    height = random.uniform(0.5, 2)
    color = np.random.rand(3,)  # Random color (RGB)

    shape_type = random.choice(['circle', 'rectangle', 'ellipse'])

    if shape_type == 'circle':
        circle = plt.Circle((x, y), width / 2, color=color, alpha=0.7)
        ax.add_artist(circle)
    elif shape_type == 'rectangle':
        rectangle = plt.Rectangle((x, y), width, height, color=color, alpha=0.7)
        ax.add_artist(rectangle)
    elif shape_type == 'ellipse':
        ellipse = Ellipse((x, y), width, height, color=color, alpha=0.7)
        ax.add_patch(ellipse)

# Save and display
plt.savefig('generative_art.png', dpi=300, bbox_inches='tight')
plt.show()
