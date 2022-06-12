import unittest

import CalendarioGregoriano as cg

# python -m unittest -v test_CalendarioGregoriano1a

class TestCalendarioGregoriano(unittest.TestCase):


    def test_dia_siguiente(self):
        self.assertEqual(cg.dia_siguiente((2022, 10, 12) ), (2022, 10, 13))
        self.assertEqual(cg.dia_siguiente((2022, 12, 32) ), "La fecha ingresada es invalida")
        self.assertEqual(cg.dia_siguiente((2023, 4, ) ), "La fecha ingresada es invalida")



