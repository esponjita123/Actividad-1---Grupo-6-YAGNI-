import unittest
from X import X  # Asegúrate de que el archivo X.py esté en el mismo directorio

class TestX(unittest.TestCase):

    def setUp(self):
        self.obj = X()

    def test_sumar(self):
        self.assertEqual(self.obj.sumar(3, 2), 5)
        self.assertEqual(self.obj.sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(self.obj.restar(5, 2), 3)
        self.assertEqual(self.obj.restar(0, 5), -5)

if __name__ == '__main__':
    unittest.main()
