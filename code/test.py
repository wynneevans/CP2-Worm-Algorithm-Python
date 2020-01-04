import unittest
from lattice import Lattice


class LatticeTests(unittest.TestCase):
    """Tests for the Lattice class"""

    def test_lattice_indices(self):

        test_lattice = Lattice(6, 4, 12)

        self.assertEqual(test_lattice.plaquettes[0].index, 0)
        self.assertEqual(test_lattice.plaquettes[15].index, 15)

    def test_lattice_plaquette_ind(self):

        nx = 6
        ny = 4
        nt = 4

        test_lattice = Lattice(nx, ny, nt)

        #  2 -- 3
        #  |    |
        #  0 -- 1

        #  0, 1, 2, 3

        CORNERS = {
            0: (42, 43, 12, 13),
            1: (44, 45, 14, 15),
            2: (46, 47, 16, 17),
            3: (36, 37, 12, 13),
            4: (38, 39, 14, 15),
            5: (40, 41, 16, 17),
            6: (36, 37, 18, 19),
            7: (38, 39, 20, 21),
            8: (40, 41, 22, 23),
            9: (42, 43, 18, 19),
            10: (44, 45, 20, 21),
            11: (46, 47, 22, 23),
            #
            12: (0, 3, 26, 29),
            13: (0, 3, 24, 27),
            14: (1, 4, 24, 27),
            15: (1, 4, 25, 28),
            16: (2, 5, 25, 28),
            17: (2, 5, 26, 29),
            18: (6, 9, 32, 35),
            19: (6, 9, 30, 33),
            20: (7, 10, 30, 33),
            21: (7, 10, 31, 34),
            22: (8, 11, 31, 34),
            23: (8, 11, 32, 35),
            #
            24: (13, 14, 43, 44),
            25: (15, 16, 45, 46),
            26: (17, 12, 47, 42),
            27: (13, 14, 37, 38),
            28: (15, 16, 39, 40),
            29: (17, 12, 41, 36),
            30: (19, 20, 37, 38),
            31: (21, 22, 39, 40),
            32: (23, 18, 41, 36),
            33: (19, 20, 43, 44),
            34: (21, 22, 45, 46),
            35: (23, 18, 47, 42),
            #
            36: (29, 32, 3, 6),
            37: (27, 30, 3, 6),
            38: (27, 30, 4, 7),
            39: (28, 31, 4, 7),
            40: (28, 31, 5, 8),
            41: (29, 32, 5, 8),
            42: (35, 26, 9, 0),
            43: (33, 24, 9, 0),
            44: (33, 24, 10, 1),
            45: (34, 25, 10, 1),
            46: (34, 25, 11, 2),
            47: (35, 26, 11, 2)
        }

        for i in range(nx*ny*nt/2):
            #print("Plaquette: ", i)
            self.assertEqual(test_lattice.plaquettes[i].ref0.index, CORNERS[i][0])
            self.assertEqual(test_lattice.plaquettes[i].ref1.index, CORNERS[i][1])
            self.assertEqual(test_lattice.plaquettes[i].ref2.index, CORNERS[i][2])
            self.assertEqual(test_lattice.plaquettes[i].ref3.index, CORNERS[i][3])

    def test_lattice_plaquette2_ind(self):

        nx = 8
        ny = 6
        nt = 4

        test_lattice = Lattice(nx, ny, nt)
 
        CORNERS = {
            0: (88, 89, 24, 25),
            1: (90, 91, 26, 27),
            2: (92, 93, 28, 29),
            3: (94, 95, 30, 31),
            4: (72, 73, 24, 25),
            5: (74, 75, 26, 27),
            6: (76, 77, 28, 29),
            7: (78, 79, 30, 31),
            8: (72, 73, 32, 33),
            9: (74, 75, 34, 35),
            10: (76, 77, 36, 37),
            11: (78, 79, 38, 39),
            12: (80, 81, 32, 33),
            13: (82, 83, 34, 35),
            14: (84, 85, 36, 37),
            15: (86, 87, 38, 39),
            16: (80, 81, 40, 41),
            17: (82, 83, 42, 43),
            18: (84, 85, 44, 45),
            19: (86, 87, 46, 47),
            20: (88, 89, 40, 41),
            21: (90, 91, 42, 43),
            22: (92, 93, 44, 45),
            23: (94, 95, 46, 47),
            #
            24: (0, 4, 51, 55),
            25: (0, 4, 48, 52),
            26: (1, 5, 48, 52),
            27: (1, 5, 49, 53),
            28: (2, 6, 49, 53),
            29: (2, 6, 50, 54),
            30: (3, 7, 50, 54),
            31: (3, 7, 51, 55),
            32: (8, 12, 59, 63),
            33: (8, 12, 56, 60),
            34: (9, 13, 56, 60),
            35: (9, 13, 57, 61),
            36: (10, 14, 57, 61),
            37: (10, 14, 58, 62),
            38: (11, 15, 58, 62),
            39: (11, 15, 59, 63),
            40: (16, 20, 67, 71),
            41: (16, 20, 64, 68),
            42: (17, 21, 64, 68),
            43: (17, 21, 65, 69),
            44: (18, 22, 65, 69),
            45: (18, 22, 66, 70),
            46: (19, 23, 66, 70),
            47: (19, 23, 67, 71),
            #
            48: (25, 26, 89, 90),
            49: (27, 28, 91, 92),
            50: (29, 30, 93, 94),
            51: (31, 24, 95, 88),
            52: (25, 26, 73, 74),
            53: (27, 28, 75, 76),
            54: (29, 30, 77, 78),
            55: (31, 24, 79, 72),
            56: (33, 34, 73, 74),
            57: (35, 36, 75, 76),
            58: (37, 38, 77, 78),
            59: (39, 32, 79, 72),
            60: (33, 34, 81, 82),
            61: (35, 36, 83, 84),
            62: (37, 38, 85, 86),
            63: (39, 32, 87, 80),
            64: (41, 42, 81, 82),
            65: (43, 44, 83, 84),
            66: (45, 46, 85, 86),
            67: (47, 40, 87, 80),
            68: (41, 42, 89, 90),
            69: (43, 44, 91, 92),
            70: (45, 46, 93, 94),
            71: (47, 40, 95, 88),
            #
            72: (55, 59, 4, 8),
            73: (52, 56, 4, 8),
            74: (52, 56, 5, 9),
            75: (53, 57, 5, 9),
            76: (53, 57, 6, 10),
            77: (54, 58, 6, 10),
            78: (54, 58, 7, 11),
            79: (55, 59, 7, 11),
            80: (63, 67, 12, 16),
            81: (60, 64, 12, 16),
            82: (60, 64, 13, 17),
            83: (61, 65, 13, 17),
            84: (61, 65, 14, 18),
            85: (62, 66, 14, 18),
            86: (62, 66, 15, 19),
            87: (63, 67, 15, 19),
            88: (71, 51, 20, 0),
            89: (68, 48, 20, 0),
            90: (68, 48, 21, 1),
            91: (69, 49, 21, 1),
            92: (69, 49, 22, 2),
            93: (70, 50, 22, 2),
            94: (70, 50, 23, 3),
            95: (71, 51, 23, 3)

        }

        for i in range(nx*ny*nt/2):
            self.assertEqual(test_lattice.plaquettes[i].ref0.index, CORNERS[i][0])
            self.assertEqual(test_lattice.plaquettes[i].ref1.index, CORNERS[i][1])
            self.assertEqual(test_lattice.plaquettes[i].ref2.index, CORNERS[i][2])
            self.assertEqual(test_lattice.plaquettes[i].ref3.index, CORNERS[i][3])


if __name__ == '__main__':
    unittest.main()