import unittest

import CalendarioGregoriano as cg

# python -m unittest -v test_CalendarioGregoriano1a

class TestCalendarioGregoriano(unittest.TestCase):
    '''
    def test_fecha_es_valida(self):
        self.assertTrue(cg.fecha_es_valida((1582, 11, 20)))
        self.assertTrue(cg.fecha_es_valida((1900, 7, 14)))
        self.assertTrue(cg.fecha_es_valida((1672, 4, 5)))
        self.assertTrue(cg.fecha_es_valida((2022, 2, 26)))
        self.assertTrue(cg.fecha_es_valida((1856, 2, 29)))
        self.assertFalse(cg.fecha_es_valida((1317, 10, 7)))
  '''
    def test_fecha_futura(self):

        self.assertEqual(cg.fecha_futura((2022, 10, 31), 25), (2022, 11, 25))
        self.assertEqual(cg.fecha_futura((2022, -10, 5), 4), "La fecha ingresada no es válida")
        self.assertEqual(cg.fecha_futura((2150, 5), 10), "La fecha ingresada no es válida")
        self.assertEqual(cg.fecha_futura((2500, -1), -10.5), "La fecha ingresada no es válida")
        self.assertEqual(cg.fecha_futura((2022, 5, 15), 10.5), "El número de días tiene que ser mayor o igual a 0")
