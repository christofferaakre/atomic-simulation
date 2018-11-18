from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np
import math

from functions import scale_vector, electric_force, sum_vectors, force_to_acceleration
from constants import e, u, Å

hydrogen1 = dict(
    name='Hydrogen 1',
    charge=1 * e,
    mass=1.00793 * u,
    position=[0.5 * Å, 0.5 * Å, 0.5 * Å],
    velocity=[0, 0, 0],
    acceleration=[0, 0, 0],
    force=[0, 0, 0]
)
hydrogen2 = dict(
    name='Hydrogen 2',
    charge=1 * e,
    mass=1.00793 * u,
    position=[-0.5 * Å, -0.5 * Å, -0.5 * Å],
    velocity=[0, 0, 0],
    acceleration=[0, 0, 0],
    force=[0, 0, 0]
)
oxygen1 = dict(
    name='Oxygen 1',
    charge=-2 * e,
    mass=15.9994 * u,
    position=[0, 0, 0],
    velocity=[0, 0, 0],
    acceleration=[0, 0, 0],
    force=[0, 0, 0]
)

atoms = [hydrogen1, oxygen1]

time = 5

t = 0
period = 1 / 1000

while t < time:
    i = 0
    while i < len(atoms):
        atom = atoms[i]
        position = atom['position']
        velocity = atom['velocity']
        acceleration = atom['acceleration']

        # Moving the atom
        atom['position'] = sum_vectors(
            [position, scale_vector(velocity, period)])

        # Accelerating the atom using its current acceleration vector
        atom['velocity'] = sum_vectors([
            velocity, scale_vector(acceleration, period)])

        # Calculating the net force on the atom
        force = [0, 0, 0]
        j = 0
        while j < len(atoms):
            if j != i:
                force = sum_vectors(
                    [force, electric_force(atoms[i], atoms[j])])
            j += 1

        # Updating the force and acceleration on the atom
        atoms[i]['force'] = [force[0], force[1], force[2]]
        atom['acceleration'] = force_to_acceleration(
            [force[0], force[1], force[2]], atom['mass'])

        i += 1

    t += period

np.random.seed(19680801)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for atom in atoms:
    name = atom['name']
    position = atom['position']
    X = position[0]
    Y = position[1]
    Z = position[2]
    print(
        f'Position of {name}: [{X}, {Y}, {Z}]')
    color = 'green'
    if 'Oxygen' in atom['name']:
        color = 'red'
    ax.scatter(X, Y, Z, color=color)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
