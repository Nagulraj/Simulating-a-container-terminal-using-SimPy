# Simulating a Container Terminal Using SimPy

## Description

This Python script simulates the operations of a container terminal using the SimPy library. The simulation models key terminal operations including:

- **Vessel Arrivals:** Vessels arrive at the terminal with inter-arrival times that follow an exponential distribution.
- **Berthing:** Vessels berth at available slots. If no berths are free, vessels wait in a queue.
- **Unloading:**  cranes unload containers from vessels. The cranes operate independently but may be limited by availability.
- **Transportation:** Trucks transport containers from cranes to the terminal’s yard.

## Dependencies

- **SimPy**: A discrete-event simulation library for Python.

To install SimPy, run:

    pip install simpy

## How to Run

1. **Clone the repository**:

        git clone https://github.com/Nagulraj/Simulating-a-container-terminal-using-SimPy.git

2. **Navigate to the project directory**:

        cd Simulating-a-container-terminal-using-SimPy

3. **Run the main script**:

        python main.py

## Output

The script will print log messages to the console detailing:
- Vessel arrivals
- Berthing assignments
- unloading containers
- Truck transport operations


## Files

- **`main.py`**: The main script to run the simulation.
- **`container_terminal.py`**: Contains the `ContainerTerminal` class.
- **`vessel.py`**: Contains the `Vessel` class.
- **`logger.py`**: Provides logging functionality for the simulation.