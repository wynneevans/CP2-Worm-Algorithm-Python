from math import floor


"""Class for creating a plaquette"""


class Plaquette:
    #  2 -- 3
    #  |    |
    #  0 -- 1
    def __init__(self, ind, val):
        self.index = ind
        self.value = val
        self.ref0 = None
        self.ref1 = None
        self.ref2 = None
        self.ref3 = None


"""Class for creating a lattice structure"""


class Lattice:

    def __init__(self, Nx, Ny, Nt):

        self.Nx_ = Nx
        self.Ny_ = Ny
        self.Nt_ = Nt
        self.plaquettes = []

        for i in range(Nx*Ny*Nt/2):
            self.plaquettes.append(Plaquette(i, None))

        neighbour0_pos = -1
        neighbour1_pos = -1
        neighbour2_pos = -1
        neighbour3_pos = -1
        neighbour0 = -1
        neighbour1 = -1
        neighbour2 = -1
        neighbour3 = -1

        for k in range(Nt):

            if k % 4 == 0:

                for j in range(Ny):
                    for i in range(Nx/2):

                        plaquette_pos = i + j*Nx/2 + k*Nx*Ny/2
                        neighbour0_pos = (i*2) + (int((floor((j-1)/2))) % (Ny/2))*Nx + ((k-1+Nt) % Nt)*Nx*Ny/2
                        neighbour1_pos = (i*2+1) + (int((floor((j-1)/2))) % (Ny/2))*Nx + ((k-1+Nt) % Nt)*Nx*Ny/2
                        neighbour2_pos = (i*2) + int(floor(j/2))*Nx + ((k+1+Nt) % Nt)*Nx*Ny/2
                        neighbour3_pos = (i*2+1) + int(floor(j/2))*Nx + ((k+1+Nt) % Nt)*Nx*Ny/2

                        plaquette = self.plaquettes[plaquette_pos]
                        neighbour0 = self.plaquettes[neighbour0_pos]
                        neighbour1 = self.plaquettes[neighbour1_pos]
                        neighbour2 = self.plaquettes[neighbour2_pos]
                        neighbour3 = self.plaquettes[neighbour3_pos]

                        plaquette.ref0 = neighbour0
                        plaquette.ref1 = neighbour1
                        plaquette.ref2 = neighbour2
                        plaquette.ref3 = neighbour3

            if k % 4 == 1:

                for j in range(Ny/2):
                    for i in range(Nx):

                        plaquette_pos = i + j*Nx + k*Nx*Ny/2
                        neighbour0_pos = int(floor(i/2)) + ((j*2) % Ny)*(Nx/2) + ((k-1+Nt) % Nt)*Nx*Ny/2
                        neighbour1_pos = int(floor(i/2)) + ((j*2+1) % Ny)*(Nx/2) + ((k-1+Nt) % Nt)*Nx*Ny/2
                        neighbour2_pos = (int((floor((i-1)/2))) % (Nx/2)) + ((j*2)%Ny)*(Nx/2) + ((k+1+Nt) % Nt)*Nx*Ny/2
                        neighbour3_pos = (int((floor((i-1)/2))) % (Nx/2)) + ((j*2+1)%Ny)*(Nx/2) + ((k+1+Nt) % Nt)*Nx*Ny/2

                        plaquette = self.plaquettes[plaquette_pos]
                        neighbour0 = self.plaquettes[neighbour0_pos]
                        neighbour1 = self.plaquettes[neighbour1_pos]
                        neighbour2 = self.plaquettes[neighbour2_pos]
                        neighbour3 = self.plaquettes[neighbour3_pos]

                        plaquette.ref0 = neighbour0
                        plaquette.ref1 = neighbour1
                        plaquette.ref2 = neighbour2
                        plaquette.ref3 = neighbour3

            if k % 4 == 2:

                for j in range(Ny):
                    for i in range(Nx/2):

                        plaquette_pos = i + j*Nx/2 + k*Nx*Ny/2
                        neighbour0_pos = (i*2+1) % Nx + int(floor(j/2))*Nx + ((k-1+Nt) % Nt)*Nx*Ny/2
                        neighbour1_pos = (i*2+2) % Nx + int(floor(j/2))*Nx + ((k-1+Nt) % Nt)*Nx*Ny/2
                        neighbour2_pos = (i*2+1) % Nx + ((int(floor((j-1)/2))) % (Ny/2))*Nx + ((k+1+Nt) % Nt)*Nx*Ny/2
                        neighbour3_pos = (i*2+2) % Nx + ((int(floor((j-1)/2))) % (Ny/2))*Nx + ((k+1+Nt) % Nt)*Nx*Ny/2

                        plaquette = self.plaquettes[plaquette_pos]
                        neighbour0 = self.plaquettes[neighbour0_pos]
                        neighbour1 = self.plaquettes[neighbour1_pos]
                        neighbour2 = self.plaquettes[neighbour2_pos]
                        neighbour3 = self.plaquettes[neighbour3_pos]

                        plaquette.ref0 = neighbour0
                        plaquette.ref1 = neighbour1
                        plaquette.ref2 = neighbour2
                        plaquette.ref3 = neighbour3

            if k % 4 == 3:

                for j in range(Ny/2):
                    for i in range(Nx):

                        plaquette_pos = i + j*Nx + k*Nx*Ny/2
                        neighbour0_pos = (int((floor((i-1)/2))) % (Nx/2)) + ((j*2+1)%Ny)*(Nx/2) + ((k-1+Nt) % Nt)*Nx*Ny/2
                        neighbour1_pos = (int((floor((i-1)/2))) % (Nx/2)) + ((j*2+2)%Ny)*(Nx/2) + ((k-1+Nt) % Nt)*Nx*Ny/2
                        neighbour2_pos = int(floor(i/2)) + ((j*2+1) % Ny)*(Nx/2) + ((k+1+Nt) % Nt)*Nx*Ny/2
                        neighbour3_pos = int(floor(i/2)) + ((j*2+2) % Ny)*(Nx/2) + ((k+1+Nt) % Nt)*Nx*Ny/2

                        plaquette = self.plaquettes[plaquette_pos]
                        neighbour0 = self.plaquettes[neighbour0_pos]
                        neighbour1 = self.plaquettes[neighbour1_pos]
                        neighbour2 = self.plaquettes[neighbour2_pos]
                        neighbour3 = self.plaquettes[neighbour3_pos]

                        plaquette.ref0 = neighbour0
                        plaquette.ref1 = neighbour1
                        plaquette.ref2 = neighbour2
                        plaquette.ref3 = neighbour3

    def antiferromagnetic(self):
        Nx = self.Nx_
        Ny = self.Ny_
        Nt = self.Nt_

        for k in range(self.Nt_):

            if k % 4 == 0:
                for j in range(self.Ny_):
                    for i in range(self.Nx_/2):
                        plaquette_pos = i + j*Nx/2 + k*Nx*Ny/2
                        if j%2 == 0:
                            self.plaquettes[plaquette_pos].value = 13
                        else:
                            self.plaquettes[plaquette_pos].value = 113

            if k % 4 == 1:
                for j in range(self.Ny_/2):
                    for i in range(self.Nx_):
                        plaquette_pos = i + j*Nx + k*Nx*Ny/2
                        if i%2 == 0:
                            self.plaquettes[plaquette_pos].value = 13
                        else:
                            self.plaquettes[plaquette_pos].value = 113

            if k % 4 == 2:
                for j in range(self.Ny_):
                    for i in range(self.Nx_/2):
                        plaquette_pos = i + j*Nx/2 + k*Nx*Ny/2
                        if j%2 == 0:
                            self.plaquettes[plaquette_pos].value = 113
                        else:
                            self.plaquettes[plaquette_pos].value = 13

            if k % 4 == 3:
                for j in range(self.Ny_/2):
                    for i in range(self.Nx_):
                        plaquette_pos = i + j*Nx + k*Nx*Ny/2
                        if i%2 == 0:
                            self.plaquettes[plaquette_pos].value = 113
                        else:
                            self.plaquettes[plaquette_pos].value = 13
