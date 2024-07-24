

class Log:
    def __init__(self, env):
        self.env = env

    def vessel_arrives(self, vessel_id):
        print(f"Time {self.env.now}: Vessel {vessel_id} arrives")

    def vessel_berths(self, vessel_id, berth_index):
        print(f"Time {self.env.now}: Vessel {vessel_id} berths at berth {berth_index + 1}")

    def vessel_departs(self, vessel_id, berth_index):
        print(f"Time {self.env.now}: Vessel {vessel_id} departs from berth {berth_index + 1}")

    def crane_unloads_container(self, vessel_id, container_number, berth_index):
        print(f"Time {self.env.now}: Crane unloads container {container_number} from vessel {vessel_id} at berth {berth_index + 1}")

    def truck_transports_container(self, vessel_id, container_number):
        print(f"Time {self.env.now}: Truck transports container {container_number} from vessel {vessel_id}")

    def vessel_waiting_for_berth(self, vessel_id):
        print(f"Time {self.env.now}: Vessel {vessel_id} waiting for berth")