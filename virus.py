

class Virus:
    def __init__(self, name, infect_rate, num_infected, fatality_rate,
                 lifetime, vaccination_rate):
        fatality_rate = fatality_rate if fatality_rate < 1 else .99
        self.name = name
        self.infect_rate = infect_rate
        self.num_infected = num_infected
        self.fatality_rate = self.per_turn_fatality(fatality_rate, lifetime)
        self.lifetime = lifetime
        self.vaccination_rate = vaccination_rate

    @staticmethod
    def per_turn_fatality(fatality_rate, lifetime):
        return 1 - (1 - fatality_rate)**(1/lifetime)
