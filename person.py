from random import random


class Person:
    def __init__(self, _id):
        self.id = _id
        self.vaccinated = []
        self.interact_list = []
        self.viruses = []

    # if not vaccinated and not infected, list of infectors

    def update(self):
        if self.vaccinated:
            # log not because of vaccine
            return make_stat('vaccinated')

        if self.viruses:
            # log not because already infected
            return make_stat('infected')

        return make_stat(**is_infected)

    
    def end_step(self):
        self.interact_list = []

    def which_infected(self, virus):
        num_infectors = len(self.interact_list)

        infectors = [
            interactor.id for interactor in self.interact_list 
            if random() <= virus.infect_rate
        ]
        if infectors:
            return {'status': 'newly infected', 'infector_list': infectors}

        return {'status': 'resisted'}

    def make_stat(self, status, infector_list = []):
        
        return [self.id, status, infector_list, len(self.interact_list)]
