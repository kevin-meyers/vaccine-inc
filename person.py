from random import random


class Person:
    def __init__(self, _id):
        self.id = _id
        self.vaccinated = False
        self.infected = False
        self.interact_list = []

    # if not vaccinated and not infected, list of infectors


    def update(self, virus):
        if self.vaccinated:
            # log not because of vaccine
            return self.id, 'vaccinated'

        if self.infected:
            # log not because already infected
            return self.id, 'infected'

    
    def end_step(self):
        self.interact_list = []

    def is_infected(self):
        which_infected = [
            interactor.id for interactor in self.interact_list 
            if random() <= virus.infect_rate
        ]
                # log infected by interaction with which_infected


        self.infected = True


