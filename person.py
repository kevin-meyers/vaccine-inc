from collections import defaultdict
from random import random


class Person:
    def __init__(self, _id):
        self.id = _id
        self.vaccinated = []
        self.interact_list = []
        self.viruses = []
        self.stats = {
            'id': self._id,
            'status': '',
            'infectors_dict': defaultdict(lambda: []),
            'num_interactions': 0,
            'vaccines': [],
            'died_to': []
        }



    # if not vaccinated and not infected, list of infectors

    def update(self):
        if self.vaccinated:
            self.stats['status'] = 'vaccinated'
            return self.stats

        if self.viruses:
            self.stats['status'] = 'infected'
            return self.stats

        self.stats.update(is_infected)
        return self.stats

    def end_step(self):
        self.interact_list = []

    def dot(self):
        for virus in self.viruses:
            if random() <= virus.fatality_rate:
                self.dead = True
                self.stats['died_to'].append(virus.name)

        if not self.dead:
            for i in range(-len(self.virus)):
                self.viruses[i][1] -= 1

                if self.viruses[i][1] <= 0:
                    self.viruses.pop(i)


            

    def which_infected(self, virus):
        for interactor in self.interact_list:
            for virus, _ in interactor.viruses:
                if random() <= virus.infect_rate:
                    self.stats['infectors_dict'][virus.name].append(interactor.id)
                    self.viruses.append([virus, virus.lifetime])

        infectors = [
            interactor.id for interactor in self.interact_list
            if random() <= virus.infect_rate
        ]
        if infectors:
            return {'status': 'newly infected', 'infector_list': infectors}

        return {'status': 'resisted'}
