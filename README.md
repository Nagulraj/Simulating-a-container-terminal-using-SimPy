# Simulating a Container Terminal Using SimPy

## Description

This Python script simulates the operations of a container terminal using the SimPy library. The simulation models key terminal operations including:

- **Vessel Arrivals:** Vessels arrive at the terminal with inter-arrival times that follow an exponential distribution.
- **Berthing:** Vessels berth at available slots. If no berths are free, vessels wait in a queue.
- **Unloading:** Quay cranes unload containers from vessels. The cranes operate independently but may be limited by availability.
- **Transportation:** Trucks transport containers from cranes to the terminal’s yard.

## Dependencies

- **SimPy**: A discrete-event simulation library for Python.

To install SimPy, run:

    pip install simpy

## How to Run

1. **Clone the repository** (if applicable):

        git clone <repository_url>

2. **Navigate to the project directory**:

        cd <project_directory>

3. **Run the main script**:

        python main.py

## Output

The script will print log messages to the console detailing:
- Vessel arrivals
- Berthing assignments
- Crane operations (unloading containers)
- Truck transport operations

## Notes

- This is a basic simulation model intended for demonstration purposes. It includes fundamental features such as vessel handling, crane operations, and truck logistics.
- To modify the simulation parameters (e.g., number of berths, cranes, trucks, or container quantities), edit the `ContainerTerminal` class or relevant sections in the script.

## Files

- **`main.py`**: The main script to run the simulation.
- **`container_terminal.py`**: Contains the `ContainerTerminal` class.
- **`vessel.py`**: Contains the `Vessel` class.
- **`logger.py`**: Provides logging functionality for the simulation.