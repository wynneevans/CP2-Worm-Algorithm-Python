import numpy as np
from lattice import Lattice


def main():

    the_lattice = Lattice(6, 4, 12)
    a_plaquette = the_lattice.plaquettes[0]
    print(a_plaquette.value, a_plaquette.ref0.index, a_plaquette.ref1.index, a_plaquette.ref2.index, a_plaquette.ref3.index)
    the_lattice.antiferromagnetic()
    print(a_plaquette.value, a_plaquette.ref0.index, a_plaquette.ref1.index, a_plaquette.ref2.index, a_plaquette.ref3.index)


if __name__ == "__main__":
    main()
