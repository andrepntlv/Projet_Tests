from selenium import webdriver
import unittest

class testpanier(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'drivers\chromedriver.exe')

    # Connexion en tant que client au site Yatara Massages
    def loginClient(self):
        self.driver.maximize_window()
        self.driver.get("https://www.esig-sandbox.ch/team20_1_v2/connexion.php")
        name = self.driver.find_element_by_id("fname")
        name.send_keys("inlo")
        password = self.driver.find_element_by_id("lname")
        password.send_keys("inlo1234")
        login = self.driver.find_element_by_name("formconnexion")
        login.click()

    # Def ajout d'un article dans le panier
    def ajoutArticlePanier(self):
        self.loginClient()
        self.driver.find_element_by_xpath('//a[contains(@href,"produit.php")]').click()
        self.driver.find_element_by_xpath('//a[contains(@href,"produitEntier.php?id=3")]').click()
        self.driver.find_element_by_name("quantite").send_keys(15)
        self.driver.find_element_by_name("ajoutPanier").click()

    # Test sur l'ajout d'un produit sans être connecté
    def test_nonConnecte(self):
        self.driver.maximize_window()
        self.driver.get("http://esig-sandbox.ch/team20_1_v2/produitEntier.php?id=3")
        self.driver.find_element_by_name("quantite").send_keys(2)
        self.driver.find_element_by_name("ajoutPanier").click()
        erreur = self.driver.find_element_by_xpath("//font").text
        self.assertEqual("Vous devez être connecté pour ajouter cet article à votre panier.", erreur)

    # Test sur l'ajout d'un produit sans choisir une valeur dans l'input
    def test_champVide(self):
        self.loginClient()
        self.driver.find_element_by_xpath('//a[contains(@href,"produit.php")]').click()
        self.driver.find_element_by_xpath('//a[contains(@href,"produitEntier.php?id=3")]').click()
        self.driver.find_element_by_name("ajoutPanier").click()
        erreur = self.driver.find_element_by_xpath("//font").text
        self.assertEqual("Il faut rentrer une valeur pour ajouter au panier.", erreur)

    # Test s'il n'y a pas assez de quantité en stock
    def test_quantiteStock(self):
        self.loginClient()
        self.driver.find_element_by_xpath('//a[contains(@href,"produit.php")]').click()
        self.driver.find_element_by_xpath('//a[contains(@href,"produitEntier.php?id=3")]').click()
        self.driver.find_element_by_name("quantite").send_keys(50)
        self.driver.find_element_by_name("ajoutPanier").click()
        erreur = self.driver.find_element_by_xpath("//font").text
        self.assertEqual("Il n'y a pas assez de quantité en stock.", erreur)

    # Test du message en ajoutant un produit au panier
    def test_ajoutProduit(self):
        self.loginClient()
        self.driver.find_element_by_xpath('//a[contains(@href,"produit.php")]').click()
        self.driver.find_element_by_xpath('//a[contains(@href,"produitEntier.php?id=3")]').click()
        self.driver.find_element_by_name("quantite").send_keys(15)
        self.driver.find_element_by_name("ajoutPanier").click()
        erreur = self.driver.find_element_by_xpath("//font").text
        self.assertEqual("Vous avez bien ajouté cet article à votre panier.", erreur)

    # Test de l'ajout d'un produit fonctionnel dans le panier
    def test_ajoutProduitDansLePanier(self):
        self.ajoutArticlePanier()
        self.driver.get('http://www.esig-sandbox.ch/team20_1_v2/panier.php')
        produit = self.driver.find_element_by_xpath('//td').text
        self.assertEqual("Body oil vanilla & chocolate", produit)

    # Test le prix total du panier
    def test_prixPanier(self):
        self.ajoutArticlePanier()
        self.driver.get("https://www.esig-sandbox.ch/team20_1_v2/panier.php")
        prix = self.driver.find_element_by_xpath("//tr[3]/td[2]").text
        self.assertEqual("Prix total : 315", prix)

    # Test la modification de la quantité d'un produit depuis le panier
    def test_modifQuantite(self):
        self.ajoutArticlePanier()
        self.driver.get("https://www.esig-sandbox.ch/team20_1_v2/panier.php")
        self.driver.find_element_by_name("q[]").clear()
        self.driver.find_element_by_name("q[]").send_keys(20)
        self.driver.find_element_by_xpath("//input[@value='Actualiser']").click()
        prix = self.driver.find_element_by_xpath("//tr[3]/td[2]").text
        self.assertEqual("Prix total : 420", prix)

    # Test la modification de la quantité d'un produit en négatif
    def test_modifQuantiteNegative(self):
        self.ajoutArticlePanier()
        self.driver.get("https://www.esig-sandbox.ch/team20_1_v2/panier.php")
        self.driver.find_element_by_name("q[]").clear()
        self.driver.find_element_by_name("q[]").send_keys(-7)
        self.driver.find_element_by_xpath("//input[@value='Actualiser']").click()
        quantite = self.driver.find_element_by_xpath('//td').text
        self.assertEqual("Body oil vanilla & chocolate", quantite)

    # Test de la suppression d'un article depuis le panier, donc panier vide
    def test_panierVide(self):
        self.ajoutArticlePanier()
        self.driver.get("https://www.esig-sandbox.ch/team20_1_v2/panier.php")
        self.driver.find_element_by_link_text("Supprimer l'article").click()
        panierVide = self.driver.find_element_by_css_selector("td:nth-child(1)").text
        self.assertEqual("Votre panier est vide", panierVide)

    # Test pour passer commande d'un article
    def test_commande(self):
        self.ajoutArticlePanier()
        self.driver.get("https://www.esig-sandbox.ch/team20_1_v2/panier.php")
        self.driver.find_element_by_link_text("Commander").click()
        self.driver.find_element_by_name("paiement").click()
        self.driver.find_element_by_name("formModif").click()
        commande = self.driver.find_element_by_xpath("//font").text
        self.assertEqual("Votre commande à bien été enregistré.", commande)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()