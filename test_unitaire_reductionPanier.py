import unittest
from reduction_prixPanier import reduction_prixPanier

class MyTestCase(unittest.TestCase):
    # 4 tests "happy path"
    def test_montantSuperieurA1000(self):
        panier = (
            [{'quantity': 4, 'price': 200.00},
             {'quantity': 3, 'price': 100.00}]
        )
        montant = reduction_prixPanier(panier)
        self.assertEqual(880, montant)

    def test_montantSuperieurA500(self):
        panier = (
            [{'quantity': 2, 'price': 200.00},
             {'quantity': 2, 'price': 100.00}]
        )
        montant = reduction_prixPanier(panier)
        self.assertEqual(540, montant)

    def test_montantSuperieurA250(self):
        panier = (
            [{'quantity': 1, 'price': 200.00},
             {'quantity': 1, 'price': 60.00}]
        )
        montant = reduction_prixPanier(panier)
        self.assertEqual(247, montant)

    def test_montantSansReduction(self):
        panier = (
            [{'quantity': 4, 'price': 20.00},
             {'quantity': 2, 'price': 10.00}]
        )
        montant = reduction_prixPanier(panier)
        self.assertEqual(100, montant)

    # 4 tests problématiques
    def test_mauvaisTypeString(self):
        panier = (
            [{'quantity': 8, 'price': "test"},
             {'quantity': 9, 'price': 89.00}]
        )
        with self.assertRaises(TypeError):  # Dylan Monteiro aide pour la syntaxe
            reduction_prixPanier(panier)

    def test_mauvaisTypeBoolean(self):
        panier = (
            [{'quantity': 12, 'price': 50},
             {'quantity': False, 'price': 50}]
        )
        with self.assertRaises(TypeError):
            reduction_prixPanier(panier)

    def test_prixNegatif(self):
        panier = (
            [{'quantity': 4, 'price': -50.00},
             {'quantity': 1, 'price': -20.00}]
        )
        # montant = reduction_prixPanier(panier)
        with self.assertRaises(TypeError):
            reduction_prixPanier(panier)

    def test_montantValeurCharniere(self):
        panier = (
            [{'quantity': 4, 'price': 50.00},
             {'quantity': 1, 'price': 49.99}]
        )
        montant = reduction_prixPanier(panier)
        self.assertEqual(249.99, montant)

    # 2 tests cas extrêmes
    def test_montantPanierEnorme(self):
        panier = (
            [{'quantity': 100, 'price': 5000.00},
             {'quantity': 1000, 'price': 100.00}]
        )
        montant = reduction_prixPanier(panier)
        self.assertEqual(480000, montant)

    def test_montantPanierToutPetit(self):
        panier = (
            [{'quantity': 1, 'price': 0.05},
             {'quantity': 5, 'price': 0.01}]
        )
        montant = reduction_prixPanier(panier)
        self.assertEqual(0.10, montant)


if __name__ == '__main__':
    unittest.main()
