

class Virus:
    def __init__(self, name, infect_rate, num_infected, fatality_rate, lifetime):
        self.name = name
        self.infect_rate = infect_rate
        self.num_infected = num_infected
        self.fatality_rate = self.per_turn_fatality(fatality_rate, lifetime)
        self.lifetime = lifetime

    @staticmethod
    def per_turn_fatality(fatality_rate, lifetime):
        return 1 - (1 - fatality_rate)**(1/lifetime)
