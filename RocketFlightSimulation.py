import numpy as np
import matplotlib.pyplot as plt

class Rocket:
    def __init__(self, mass, thrust, burn_time):
        self.mass = mass
        self.thrust = thrust
        self.burn_time = burn_time
        self.velocity = 0
        self.altitude = 0
        self.time = 0
        self.dt = 0.1  # time step

    def update(self):
        if self.time < self.burn_time:
            acceleration = self.thrust / self.mass
        else:
            acceleration = -9.81  # gravity

        self.velocity += acceleration * self.dt
        self.altitude += self.velocity * self.dt
        self.time += self.dt

    def simulate(self):
        altitudes = []
        times = []
        while self.altitude >= 0:
            self.update()
            altitudes.append(self.altitude)
            times.append(self.time)
        return times, altitudes

def plot_trajectory(times, altitudes):
    plt.figure(figsize=(10, 5))
    plt.plot(times, altitudes)
    plt.title('Rocket Altitude Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Altitude (m)')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    rocket = Rocket(mass=500,
