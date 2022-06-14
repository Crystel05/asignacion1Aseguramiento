import unittest

import CalendarioGregoriano as cg

# python -m unittest -v test_CalendarioGregoriano1a

class TestCalendarioGregoriano(unittest.TestCase):
    
    def test_fecha_es_valida(self):
        self.assertTrue(cg.fecha_es_valida((1582, 11, 20)))
        self.assertTrue(cg.fecha_es_valida((1900, 7, 14)))
        self.assertTrue(cg.fecha_es_valida((1672, 4, 5)))
        self.assertTrue(cg.fecha_es_valida((2022, 2, 26)))
        self.assertTrue(cg.fecha_es_valida((1856, 2, 29)))
        self.assertFalse(cg.fecha_es_valida((1317, 10, 7)))


    def test_dia_siguiente(self):
        self.assertEqual(cg.dia_siguiente((2022, 10, 12) ), (2022, 10, 13))
        self.assertEqual(cg.dia_siguiente((2022, 12, 32) ), "La fecha ingresada es invalida")
        self.assertEqual(cg.dia_siguiente((2023, 4, ) ), "La fecha ingresada es invalida")



