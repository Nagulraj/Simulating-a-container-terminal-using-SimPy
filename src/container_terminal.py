import simpy
class ContainerTerminal:
    def __init__(self, env, logger):

        """
        Initializes the ContainerTerminal with resources for berths, cranes, and trucks.

        """
        self.env = env
        self.logger = logger
        self.berths = [simpy.Resource(env, capacity=1) for _ in range(2)]  # Berths with capacity 1
        self.cranes = simpy.Resource(env, capacity=2)
        self.trucks = simpy.Resource(env, capacity=3)
        self.waiting_vessels = []

    def unload_container(self, vessel_id, berth_index):
        """
        Handles the unloading of containers from a vessel at a specific berth.

        """
        with self.cranes.request() as crane_request:
            yield crane_request
            for i in range(150):
                yield self.env.timeout(3)
                self.logger.crane_unloads_container(vessel_id, i + 1, berth_index)

                with self.trucks.request() as truck_request:
                    yield truck_request
                    self.logger.truck_transports_container(vessel_id, i + 1)
                    yield self.env.timeout(6)

    def berth_vessel(self, vessel):
        """
        Manages the berthing process for a vessel, including finding an available berth and unloading containers.

        """

        berth_index = None
        berth_request = None

        for i, berth in enumerate(self.berths):
            if berth.count == 0:  
                berth_index = i
                berth_request = berth.request()
                yield berth_request  
                break

        if berth_request is None:
            berth_requests = [berth.request() for berth in self.berths]
            results = yield simpy.AnyOf(self.env, berth_requests)
            for i, req in enumerate(berth_requests):
                if req in results.keys():
                    berth_index = i
                    berth_request = req
                    break


        self.logger.vessel_berths(vessel.id, berth_index)


        yield self.env.process(self.unload_container(vessel.id, berth_index))


        self.logger.vessel_departs(vessel.id, berth_index)

        if berth_request:
            self.berths[berth_index].release(berth_request)


        if self.waiting_vessels:
            next_vessel = self.waiting_vessels.pop(0)
            self.env.process(self.berth_vessel(next_vessel))

    def handle_waiting_vessels(self):
        """
        Periodically checks for available berths and assigns waiting vessels to them.
        
        """
        while True:
            for i, berth in enumerate(self.berths):
                if berth.count == 0 and self.waiting_vessels:
                    next_vessel = self.waiting_vessels.pop(0)
                    self.env.process(self.berth_vessel(next_vessel, berth_index=i))
            yield self.env.timeout(1)