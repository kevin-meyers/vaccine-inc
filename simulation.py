import csv
import json

from datetime import datetime
from random import sample, random
from sys import argv

from person import Person
from virus import Virus


FIELD_NAMES = ['frame', 'id', 'status', 'infectors_dict', 'num_interactions',
               'vaccines', 'died_to']


# Like a list, but kewler
class Kewlist:

    def __init__(self, length, start_val = False):
        self.list = []
        self.bools = [start_val] * length
        self.rebuild()

    def call_for_list(self, build = True):
        if build:
            self.rebuild()
        return self.list

    def append(self, index, queue = False):
        self.bools[index] = True
        if not queue:
            self.rebuild()

    def remove(self, index, queue = False):
        self.bools[index] = False
        if not queue:
            self.rebuild()

    def set_to(self, index, value = True):
        self.bools[index] = value

    def rebuild(self):
        self.list = []
        for i in range(len(self.bools)):
            if self.bools[i]:
                self.list.append(i)

def test_kool_init():
    assert Kewlist(1).list[0] == False

def test_kool_append():
    k = Kewlist(3)
    k.append(2)
    assert k.list[2] == True

def test_kool_rebuild():
    lst = [1,4,8,3]
    kl = Kewlist(4)
    for li in lst:
        kl.append(li, True)
    kl.rebuild()

    assert kl.list == [1,3,4,8]

def test_kool_remove():
    k = Kewlist(3, True)
    k.remove(2)
    assert k.list[2] == False


class Simulation:
    '''
    Runs a single simulation till there are no more infected.

    sim_card: SimCard Object, holds all the information that a simulation needs to run.
    '''

    def __init__(self, population, viruses, pop_density=100, max_frames = 100):
        self.pop_size = population
        self.persons_list = []
        self.infected = []
        self.pop_density = pop_density  # how many people they interact with in a step
        self.max_frames = max_frames
        self.frame_num = 0
        self.file_name = None
        self.viruses = viruses

        self.nfctr_array = [[False]*population]*len(viruses)

    def next_frame(self):
        self.frame_num += 1
        self.establish_interactions()
        self.stat_stuff()

    def stat_stuff(self):
        with open(self.file_name, 'a') as f:
            writer = csv.DictWriter(f, FIELD_NAMES)
            for person in self.persons_list:
                writer.writerow(
                    {**{'frame': self.frame_num}, **person.update(self.infected)}
                )
        self.rebuild_viruses()


    def rebuild_viruses(self):
        for virus in self.infected:
            virus['persindices'].rebuild()


    def establish_interactions(self):
        # for virus, persindices in self.infected.items():
        #    for persindex in persindices:
        flattened_infected = [
            (virus_dict['virus'], persindex) for virus_dict in self.infected # YOU NEED FIX HERE
            for persindex in virus_dict['persindices'].list
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
        the_chosen = Kewlist(self.pop_size)
        for virus in self.viruses:
            for persindex in sample(range(len(self.persons_list)), k=virus.num_infected):
                the_chosen.append(persindex, True)
            the_chosen.rebuild()
            print('The Chosen: ' + str(the_chosen.list))
            self.infected.append(
                {
                    'virus': virus,
                    'persindices': the_chosen
                }
            )
            for persindex in the_chosen.list:
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






if __name__ == '__main__':
    with open('viruses.json', 'r') as f:
        viruses = [Virus(**json.loads(line)) for line in f]

    with open('simcard.json', 'r') as f:
        simcard = json.loads(f.read())

    e_sim = Simulation(**simcard, viruses=viruses)

#    pop_size = int(argv[1])
#    vac_per = float(argv[2])
#    vir_name = argv[3]
#    fatality_rate = float(argv[4])
#    repr_rate = float(argv[5])
#    init_infect = int(argv[6])

#    viruses = [Virus(vir_name, repr_rate, init_infect, fatality_rate, 4,
#                     vac_per)]

#    e_sim = Simulation(pop_size, viruses)


    e_sim.sim_start()
    endflag = False

    while not endflag:
        print(e_sim.frame_num, e_sim.max_frames)
        if e_sim.frame_num >= e_sim.max_frames:
            break
        
        e_sim.next_frame()
        
        for vir_peoples in e_sim.infected:
            print(vir_peoples['persindices'].call_for_list())
            if len(vir_peoples['persindices'].call_for_list()) > 0:
                break
        else:
            endflag = True
