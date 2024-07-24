import simpy
import random
from log import Log
from container_terminal import ContainerTerminal
from vessel import Vessel

def vessel_generator(env, terminal, logger):
    vessel_id = 0
    while True:
        yield env.timeout(random.expovariate(1 / 300))
        vessel_id += 1
        Vessel(env, terminal, logger, vessel_id)

def run_simulation(simulation_time):
    env = simpy.Environment()
    logger = Log(env)
    terminal = ContainerTerminal(env, logger)
    env.process(vessel_generator(env, terminal, logger))
    env.process(terminal.handle_waiting_vessels())
    env.run(until=simulation_time)

if __name__ == "__main__":
    SIMULATION_TIME = int(input("Give the duration of the simulation time:"))
    run_simulation(SIMULATION_TIME)