from manim import *


class ParticleWithDynamicField2D(ThreeDScene):
    def construct(self):
        # Create the electron (represented as a small blue dot)
        electron = Dot(radius=0.2, color=BLUE).move_to(ORIGIN)
        electron_label = Tex("-e", color=BLUE).scale(0.5).next_to(electron, UP)
        self.add(electron)

        # Function to calculate the electric field
        def electric_field_func(pos, electron_pos):
            displacement = pos - electron_pos
            r = np.linalg.norm(displacement)
            if r == 0:  # Avoid division by zero
                return np.zeros(2)
            return -2 * displacement / r**2# Negative charge electric field

        # Create the initial electric field
        def create_field(electron_position):
            return ArrowVectorField(
                lambda pos: electric_field_func(pos, electron_position),
                x_range=[-7, 7, 0.7],
                y_range=[-4, 4, 0.7],
            )

        field = create_field(electron.get_center())
        self.add(field)

        # Define a circular path for the electron
        path = ParametricFunction(
            lambda t: np.array([2 * np.cos(t), 2 * np.sin(t), 0]),
            t_range=[0, PI],
            
        )
        #self.add(path)

        # Animate the electron along the circular path
        def update_electron_and_field(mob, alpha):
            t = alpha * 2 * PI  # Map alpha (0-1) to the full circle
            new_position = path.function(t)
            mob.move_to(new_position)

            # Update the electric field
            new_field = create_field(new_position)
            field.become(new_field)

        self.play(UpdateFromAlphaFunc(electron, update_electron_and_field), run_time=1, rate_func=linear)

        # Wait for a moment at the end
        #self.wait(1)
        


class ElectronWithElectricField3D(ThreeDScene):
    def construct(self):
        # Set the initial camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        #rotate camera
        self.begin_ambient_camera_rotation(rate=0.1)
        
        # Create the electron (a small blue sphere)
        electron = Sphere(radius=0.2, color=BLUE).move_to(ORIGIN)
        electron_label = Tex("-e", color=BLUE).scale(0.5).next_to(electron, UP)
        self.add(electron, electron_label)

        # Function to calculate the electric field
        def electric_field_func(pos, electron_pos):
            displacement = pos - electron_pos
            r = np.linalg.norm(displacement)
            if r == 0:  # Avoid division by zero
                return np.zeros(3)
            return -2 * displacement / r**2  # Negative charge electric field

        # Create the initial electric field
        def create_field(electron_position):
            return ArrowVectorField(
                lambda pos: electric_field_func(pos, electron_position),
                x_range=[-5, 5, 1],
                y_range=[-4, 4, 1],
                z_range=[-3, 3, 1],
            )

        field = create_field(electron.get_center())
        self.add(field)

        # Define a helical path for the electron
        path = ParametricFunction(
            lambda t: np.array([2 * np.cos(t/8), 2 * np.sin(t/3), 2* np.cos(t/2)+2* np.sin(t/8)]),
            t_range=[0, 50, 0.5],
            color=YELLOW,
        )
        # self.add(path)

        # Animate the electron along the helical path
        def update_electron_and_field(mob, alpha):
            t = alpha * 10  # Map alpha (0-1) to the full path
            new_position = path.function(t)
            mob.move_to(new_position)

            # Update the electric field
            new_field = create_field(new_position)
            field.become(new_field)

        self.play(UpdateFromAlphaFunc(electron, update_electron_and_field), run_time=10, rate_func=linear)

        # Wait at the end
        # self.wait(2)
        
from manim import *
from multiprocessing import Pool, cpu_count

from manim import *
from multiprocessing import Pool, cpu_count
from manim import *
from multiprocessing import Pool, cpu_count
import numpy as np

def electric_field_func(pos, electron_pos):
    """Calculate the electric field vector at a given position."""
    displacement = pos - electron_pos
    r = np.linalg.norm(displacement)
    if r == 0:  # Avoid division by zero
        return np.zeros(3)
    return -2 * displacement / r**2  # Negative charge electric field

def calculate_arrow(pos, electron_position):
    """Calculate a single arrow for the electric field."""
    field_vector = electric_field_func(pos, electron_position)
    magnitude = np.linalg.norm(field_vector)
    if magnitude > 0:
        field_vector = field_vector / magnitude
    return Arrow(
        pos,
        pos + 0.3 * field_vector,
        buff=0,
        color=BLUE,
        stroke_width=2,
    )

def create_field(electron_position):
    """Create a VGroup of arrows representing the electric field."""
    x_range = np.linspace(-5, 5, 11)
    y_range = np.linspace(-4, 4, 9)
    z_range = np.linspace(-3, 3, 7)

    grid_points = [
        np.array([x, y, z])
        for x in x_range
        for y in y_range
        for z in z_range
    ]

    # Parallel computation using multiprocessing
    with Pool(cpu_count()) as pool:
        arrows = pool.starmap(calculate_arrow, [(pos, electron_position) for pos in grid_points])
    return VGroup(*arrows)
from manim import *
from multiprocessing import Pool, cpu_count
import numpy as np


def electric_field_func(pos, electron_pos):
    """Calculate the electric field vector at a given position."""
    displacement = pos - electron_pos
    r = np.linalg.norm(displacement)
    if r == 0:  # Avoid division by zero
        return np.zeros(3)
    return -2 * displacement / r**2  # Negative charge electric field


def calculate_arrow(args):
    """Calculate a single arrow for the electric field."""
    pos, electron_position = args
    field_vector = electric_field_func(pos, electron_position)
    magnitude = np.linalg.norm(field_vector)
    if magnitude > 0:
        field_vector = field_vector / magnitude
    return Arrow(
        pos,
        pos + 0.3 * field_vector,
        buff=0,
        color=BLUE,
        stroke_width=2,
    )


def create_field(electron_position):
    """Create a VGroup of arrows representing the electric field."""
    x_range = np.linspace(-5, 5, 11)
    y_range = np.linspace(-4, 4, 9)
    z_range = np.linspace(-3, 3, 7)

    grid_points = [
        np.array([x, y, z])
        for x in x_range
        for y in y_range
        for z in z_range
    ]

    # Parallel computation using multiprocessing
    with Pool(cpu_count()) as pool:
        arrows = pool.map(calculate_arrow, [(pos, electron_position) for pos in grid_points])
    return VGroup(*arrows)


class ElectronWithElectricField3D_core(ThreeDScene):
    def construct(self):
        # Set the initial camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Create the electron
        electron = Sphere(radius=0.2, color=BLUE).move_to(ORIGIN)
        electron_label = Tex("-e", color=BLUE).scale(0.5).next_to(electron, UP)
        self.add(electron, electron_label)

        # Create the initial electric field
        field = create_field(electron.get_center())
        self.add(field)

        # Define a helical path for the electron
        path = ParametricFunction(
            lambda t: np.array([
                2 * np.cos(t / 8),
                2 * np.sin(t / 3),
                2 * np.cos(t / 2) + 2 * np.sin(t / 8)
            ]),
            t_range=[0, 50, 0.5],
            color=YELLOW,
        )

        # Animate the electron along the helical path
        def update_electron_and_field(mob, alpha):
            t = alpha * 50  # Map alpha (0-1) to the full path
            new_position = path.function(t)
            mob.move_to(new_position)

            # Update the electric field
            new_field = create_field(new_position)
            field.become(new_field)

        self.play(UpdateFromAlphaFunc(electron, update_electron_and_field), run_time=10, rate_func=linear)


#if __name__ == "__main__":
#    from manim import config
#
#    config.media_width = "75%"  # Optional for better visualization
#    scene = ElectronWithElectricField3D()
#    scene.render()

import multiprocessing
import time

def calculate_square_sum(start, end):
    """
    Calcola la somma dei quadrati dei numeri interi in un intervallo.
    """
    total = 0
    for i in range(start, end):
        total += i ** 2
    return total

def parallel_square_sum(n):
    """
    Divide il lavoro su tutti i core per calcolare la somma totale dei quadrati
    da 0 a n in parallelo.
    """
    cpu_count = multiprocessing.cpu_count()
    chunk_size = n // cpu_count  # Suddividi il lavoro tra i core
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(cpu_count)]
    ranges[-1] = (ranges[-1][0], n)  # Gestisci gli eventuali resti

    # Esegui i calcoli in parallelo
    with multiprocessing.Pool(cpu_count) as pool:
        results = pool.starmap(calculate_square_sum, ranges)

    # Somma i risultati parziali
    return sum(results)

if __name__ == "__main__":
    n = 10**10  # Cambia questo valore per testare con numeri più grandi
    print(f"Calcolando la somma dei quadrati da 0 a {n}...")
    
    start_time = time.time()
    result = parallel_square_sum(n)
    end_time = time.time()
    
    print(f"Risultato: {result}")
    print(f"Tempo di esecuzione: {end_time - start_time:.2f} secondi")