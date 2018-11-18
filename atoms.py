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
