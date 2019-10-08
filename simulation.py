from random import sample

from person import Person


class simulation:
    ''' 
    Runs a single simulation till there are no more infected.
        
    sim_card: SimCard Object, holds all the information that a simulation needs to run.
    '''

    def __init__(self, population, viruses, pop_density=100):
        self.population = [Person(_id) for _id in range(population)]
        self.num_init_infect = num_initial_infect
        self.infected = []

    def sim_stat(self):
        


    def infect_population(self, viruses):
        for virus in viruses:
            self.infected.append(
                {
                    'virus': virus, 
                    'persindices': sample(range(len(self.population)), k=virus.num_infected
                }
            )
