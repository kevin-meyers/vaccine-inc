from simulation import Simulation
from virus import Virus


def test_simulation():
    ebola = Virus('ebola', 1, 10, .1, 4, .3)
    e_sim = Simulation(1000, [ebola])

    e_sim.sim_start()
    e_sim.next_frame()

    assert True