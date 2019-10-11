import csv
from datetime import datetime

from random import sample, random

from person import Person


FIELD_NAMES = ['frame', 'id', 'status', 'infectors_dict', 'num_interactions',
               'vaccines', 'died_to']


class Simulation:
    '''
    Runs a single simulation till there are no more infected.

    sim_card: SimCard Object, holds all the information that a simulation needs to run.
    '''

    def __init__(self, population, viruses, pop_density=100):
        self.pop_size = population
        self.persons_list = []
        self.infected = []
        self.pop_density = pop_density # how many people they interact with in a step
        self.frame_num = 0
        self.file_name = None
        self.viruses = viruses

    def next_frame(self):
        self.frame_num += 1
        self.establish_interactions()
        self.stat_stuff()

    def stat_stuff(self):
        with open(self.file_name, 'a') as f:
            writer = csv.DictWriter(f, FIELD_NAMES)
            for person in self.persons_list:
                writer.writerow(
                    {**{'frame': self.frame_num}, **person.update()}
                )

    def establish_interactions(self):
        # for virus, persindices in self.infected.items():
        #    for persindex in persindices:
        flattened_infected = [
            (virus_dict['virus'], persindex) for virus_dict in self.infected
            for persindex in virus_dict['persindices']
        ]

        for virus, persindex in flattened_infected:
            for person in sample(self.persons_list, k=self.pop_density):
                person.interact_list.append([virus, persindex]) # wyatt mad here


    def sim_start(self):
        self.persons_list = [Person(_id) for _id in range(self.pop_size)]
        self.infect_population()
        self.vaccinate_population()
        self.file_name = f'data/sim-log-{datetime.now().strftime("%m-%d-%Y.%H:%M:%S")}'

        with open(self.file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['frame', 'id', 'status', 'num_interactions', 'infectors'])

    def infect_population(self):
        for virus in self.viruses:
            the_chosen = sample(range(len(self.persons_list)), k=virus.num_infected)

            self.infected.append(
                {
                    'virus': virus,
                    'persindices': the_chosen
                }
            )
            for persindex in the_chosen:
                self.persons_list[persindex].viruses.append([virus,
                                                             virus.lifetime])

    def vaccinate_population(self):
        virus_persons = [
            (virus, person) for person in self.persons_list for virus in self.viruses
        ]
        for virus, person in virus_persons:
            if virus in person.viruses:
                continue

            if random() <= virus.vaccination_rate:
                person.vaccinated.append(virus)
