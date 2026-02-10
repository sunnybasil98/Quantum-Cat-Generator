import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Your quantum cat circuit
dev = qml.device('default.qubit', wires=1)

@qml.qnode(dev)
def quantum_cat(params):
    qml.RY(params[0], wires=0)
    qml.PhaseShift(params[1], wires=0)
    return qml.state()

params = np.array([np.pi/2, np.pi/4])
state = quantum_cat(params)
print(f"🐱 Quantum Cat State: {state}")

# Calculate cat position on sphere
r, theta, phi = 1.0, np.arccos(state[0].real), np.angle(state[1])
cat_x = r * np.sin(theta) * np.cos(phi)
cat_y = r * np.sin(theta) * np.sin(phi) 
cat_z = r * np.cos(theta)

# 3D CAT MODEL positioned at quantum state
cat_body = 0.15  # Scale
cat_verts = [
    # Body (at quantum position)
    [[cat_x-cat_body, cat_y-cat_body/2, cat_z-cat_body/2], 
     [cat_x-cat_body, cat_y+cat_body/2, cat_z-cat_body/2], 
     [cat_x+cat_body, cat_y+cat_body/2, cat_z+cat_body/2], 
     [cat_x+cat_body, cat_y-cat_body/2, cat_z+cat_body/2]],
    
    # Head
    [[cat_x+cat_body*1.3, cat_y-cat_body/3, cat_z-cat_body/3], 
     [cat_x+cat_body*1.3, cat_y+cat_body/3, cat_z-cat_body/3], 
     [cat_x+cat_body*1.6, cat_y+cat_body/3, cat_z+cat_body/3], 
     [cat_x+cat_body*1.6, cat_y-cat_body/3, cat_z+cat_body/3]],
    
    # Left Ear
    [[cat_x+cat_body*1.5, cat_y-cat_body/2.5, cat_z+cat_body/0.8], 
     [cat_x+cat_body*1.7, cat_y-cat_body/3, cat_z+cat_body/1.1], 
     [cat_x+cat_body*1.4, cat_y-cat_body/4, cat_z+cat_body/0.9]],
    
    # Right Ear  
    [[cat_x+cat_body*1.5, cat_y+cat_body/2.5, cat_z+cat_body/0.8], 
     [cat_x+cat_body*1.7, cat_y+cat_body/3, cat_z+cat_body/1.1], 
     [cat_x+cat_body*1.4, cat_y+cat_body/4, cat_z+cat_body/0.9]],
    
    # Tail
    [[cat_x-cat_body*1.2, cat_y+cat_body/4, cat_z], 
     [cat_x-cat_body*1.6, cat_y+cat_body/2, cat_z+cat_body/0.3], 
     [cat_x-cat_body*1.4, cat_y+cat_body/1.5, cat_z-cat_body/0.2]]
]

# Create plot
plt.figure(figsize=(14, 12))
ax = plt.axes(projection='3d')

# Bloch sphere
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, alpha=0.15, color='lightblue')

# ORANGE 3D CAT at quantum position!
cat = Poly3DCollection(cat_verts, alpha=0.9, facecolors='orange', edgecolors='darkorange')
ax.add_collection3d(cat)

# Axes labels
ax.set_xlim([-1.5, 1.5]); ax.set_ylim([-1.5, 1.5]); ax.set_zlim([-1.5, 1.5])
ax.set_xlabel('X (Alive ↔ Dead)'); ax.set_ylabel('Y (Phase)'); ax.set_zlabel('Z')
plt.title('REAL 3D QUANTUM CAT ON BLOCH SPHERE \nOrange Cat = BOTH Alive + Dead Superposition!', 
          fontsize=18, fontweight='bold', pad=20)

plt.tight_layout()
plt.show(block=True)
print("ORANGE 3D CAT on Bloch Sphere! Drag to rotate!")
