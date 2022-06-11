import unittest

import CalendarioGregoriano as cg

# python -m unittest -v test_CalendarioGregoriano

class TestCalendarioGregoriano(unittest.TestCase):

    def test_edad_al(self):
        self.assertEqual(cg.edad_al((1999, 7, 29), (2005, 10, 15)), (6, 2, 16))
        self.assertEqual(cg.edad_al((-19, 12, 1997), (2009, 6, 40)), "Alguna de las fechas ingresadas no es válida")
        self.assertEqual(cg.edad_al((2019, 7, 29), (2015, 2, 29)), "Alguna de las fechas ingresadas no es válida")
        self.assertEqual(cg.edad_al((2020, 7, 29), (1845, 6, 7)), "La fecha 1 debe ser menor a la fecha 2")
        self.assertEqual(cg.edad_al((1927, 7, 29), (99, 1, 26, 8)), "Debe ingresar una tupla de tres valores")
        self.assertEqual(cg.edad_al((1999), (2000, 9, 10)), "Debe ingresar una tupla de tres valores")
