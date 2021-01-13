import unittest

from reduction_prixPanier import reduction_prixPanier
__import__(reduction_prixPanier())

from reductio_prixPanier import reduction_prixPanier


class MyTestCase(unittest.TestCase):
    def test_montantSuperieurAMille(self):
        panier = (
            [{'quantity': 4, 'price': 200.00},
             {'quantity': 3, 'price': 100.00}]
        )
        montant = reduction_prixPanier(panier)
        self.assertEqual(1100, montant)


if __name__ == '__main__':
    unittest.main()
