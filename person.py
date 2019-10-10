from collections import defaultdict
from random import random


class Person:
    def __init__(self, _id):
        self.id = _id
        self.vaccinated = []
        self.interact_list = []
        self.viruses = []
        self.stats = {
            'id': _id,
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

        self.stats.update(self.which_infected())
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
                    self.vaccinated.append(virus)
                    self.stats['vaccines'].append(virus.name)
                    self.viruses.pop(i)


    def which_infected(self):
        for virus, _id in self.interact_list:
            if random() <= virus.infect_rate:
                self.stats['infectors_dict'][virus.name].append(_id)
                self.stats['status'] = 'newly infected'
                self.viruses.append([virus, virus.lifetime])


        return {'status': 'resisted'}
