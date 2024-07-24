import simpy

class Vessel:
    def __init__(self, env, terminal, logger, id, num_containers=150):
        self.env = env
        self.terminal = terminal
        self.logger = logger
        self.id = id
        self.num_containers = num_containers
        self.env.process(self.arrive())

    def arrive(self):
        self.logger.vessel_arrives(self.id)
        berth_available = any(berth.count == 0 for berth in self.terminal.berths)

        if berth_available:
            yield self.env.process(self.terminal.berth_vessel(self))
        else:
            self.logger.vessel_waiting_for_berth(self.id)
            self.terminal.waiting_vessels.append(self)