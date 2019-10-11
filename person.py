from collections import defaultdict
from random import random


class Person:
    def __init__(self, _id):
        self.id = _id
        self.vaccinated = []
        self.interact_list = []
        self.viruses = []
        self.dead = False

    # if not vaccinated and not infected, list of infectors

    def update(self):
        self.stats = {
            'id': self.id,
            'status': 'healthy',
            'infectors_dict': defaultdict(lambda: []),
            'num_interactions': 0,
            'vaccines': [],
            'died_to': []
        }
        self.dot()

        if self.dead:
            self.stats['status'] = 'dead'
            return self.pretty_stats()

        if self.vaccinated:
            self.stats['status'] = 'vaccinated'
            return self.pretty_stats()

        if self.viruses:
            self.stats['status'] = 'infected'
            return self.pretty_stats()

        self.which_infected()
        return self.pretty_stats()

    def end_step(self):
        self.interact_list = []

    def dot(self):
        for j in range(len(self.viruses)):
            if random() <= self.viruses[j][0].fatality_rate:
                self.dead = True
                self.stats['died_to'].append(self.viruses[j][0].name)

        if not self.dead:
            delete_list = []
            for i in range(len(self.viruses)):
                print(self.viruses, i)
                self.viruses[i][1] -= 1

                if self.viruses[i][1] <= 0:
                    self.vaccinated.append(self.viruses[i][0])
                    self.stats['vaccines'].append(self.viruses[i][0].name)
                    delete_list.append(i)

            for i in delete_list[::-1]:
                self.viruses.pop(i)

        else:
            self.viruses = []

    def which_infected(self):
        for virus, _id in self.interact_list:
            if random() <= virus.infect_rate:
                self.stats['infectors_dict'][virus.name].append(_id)
                self.stats['status'] = 'newly infected'
                self.viruses.append([virus, virus.lifetime])

        if not self.stats['infectors_dict']:
            self.stats['status'] = 'resisted'

    def pretty_stats(self):
        self.stats['infectors_dict'] = dict(self.stats['infectors_dict'])
        self.end_step()
        return self.stats
