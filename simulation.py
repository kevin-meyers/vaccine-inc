from random import sample, random

from person import Person


class simulation:
    ''' 
    Runs a single simulation till there are no more infected.
        
    sim_card: SimCard Object, holds all the information that a simulation needs to run.
    '''

    def __init__(self, population, viruses, pop_density=100):
        self.pop_size = population
        self.persons_list = []
        self.num_init_infect = num_initial_infect
        self.infected = []
        self.pop_density = pop_density # how many people they interact with in a step

    def next_frame(self):
        establish_interactions()

    def stat_stuff(self):
        

    def establish_interactions(self):
        for virus, persindices in self.infected.items():
            for persindex in persindices:
                for person in sample(self.persons_list, k=self.pop_density):
                    person.interact_list.append([virus, persindex]) # wyatt mad here


    def sim_start(self):
        self.persons_list = [Person(_id) for _id in range(self.pop_size)]
        self.infect_population()
        self.vaccinate_population()
    
    def infect_population(self):
        for virus in self.viruses:
            self.infected.append(
                {
                    'virus': virus, 
                    'persindices': sample(range(len(self.persons_list)), k=virus.num_infected
                }
            )

    def vaccinate_poulation(self):
        for virus in self.viruses:
            for person in persons:
                if virus in person.viruses:
                    continue

                if random() <= virus.vaccination_rate:
                    person.vaccinated.append(virus)
