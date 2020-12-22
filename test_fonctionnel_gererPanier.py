from selenium import webdriver
from time import sleep
import unittest

class testpanier(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\PINTO_ALVES_AN-ESIG\PycharmProjects\inlo-projet-testing-andre-pntlv\drivers\chromedriver.exe')

    # Connexion en tant que client au site Yatara Massages
    def loginClient(self):
        self.driver = webdriver.Chrome("drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.esig-sandbox.ch/team20_1_v2/connexion.php")
        name = self.driver.find_element_by_id("fname")
        name.send_keys("inlo")
        password = self.driver.find_element_by_id("lname")
        password.send_keys("inlo1234")
        login = self.driver.find_element_by_name("formconnexion")
        login.click()
        sleep(3)

    # Def ajout d'un article dans le panier
    def ajoutArticlePanier(self):
        self.loginClient()
        self.driver.find_element_by_xpath('//a[contains(@href,"produit.php")]').click()
        self.driver.find_element_by_xpath('//a[contains(@href,"produitEntier.php?id=3")]').click()
        self.driver.find_element_by_name("quantite").send_keys(15)
        self.driver.find_element_by_name("ajoutPanier").click()


    # Test sur l'ajout d'un produit sans être connecté
    def test_notConnected(self):
        self.driver.get("http://esig-sandbox.ch/team20_1_v2/produitEntier.php?id=3")
        self.driver.find_element_by_name("quantite").send_keys(2)
        self.driver.find_element_by_name("ajoutPanier").click()
        self.driver.implicitly_wait(5)
        erreur = self.driver.find_element_by_xpath("//font").text
        self.assertEqual(erreur,"Vous devez être connecté pour ajouter cet article à votre panier.")

    #Test sur l'ajout d'un produit sans choisir une valeur dans l'input
    def test_inputEmpty(self):
        self.loginClient()
        self.driver.find_element_by_xpath('//a[contains(@href,"produit.php")]').click()
        self.driver.find_element_by_xpath('//a[contains(@href,"produitEntier.php?id=3")]').click()
        self.driver.find_element_by_name("ajoutPanier").click()
        erreur = self.driver.find_element_by_xpath("//font").text
        self.assertEqual(erreur, "Il faut rentrer une valeur pour ajouter au panier.")

    #Test s'il n'y a pas assez de quantité en stock
    def test_quantiteStock(self):
        self.loginClient()
        self.driver.find_element_by_xpath('//a[contains(@href,"produit.php")]').click()
        self.driver.find_element_by_xpath('//a[contains(@href,"produitEntier.php?id=3")]').click()
        self.driver.find_element_by_name("quantite").send_keys(50)
        self.driver.find_element_by_name("ajoutPanier").click()
        erreur = self.driver.find_element_by_xpath("//font").text
        self.assertEqual(erreur, "Il n'y a pas assez de quantité en stock.")

    #Test de l'ajout d'un produit fonctionnel
    def test_ajoutProduit(self):
        self.loginClient()
        self.driver.find_element_by_xpath('//a[contains(@href,"produit.php")]').click()
        self.driver.find_element_by_xpath('//a[contains(@href,"produitEntier.php?id=3")]').click()
        self.driver.find_element_by_name("quantite").send_keys(15)
        self.driver.find_element_by_name("ajoutPanier").click()
        erreur = self.driver.find_element_by_xpath("//font").text
        self.assertEqual(erreur, "Vous avez bien ajouté cet article à votre panier.")

    def test_commander(self):
        self.ajoutArticlePanier()
        self.driver.find_element_by_xpath('//a[contains(@href,"panier.php")]').click()
        prix = self.driver.find_element_by_xpath("//tr[4]/td[2]").text
        self.assertEqual(prix, "315")


if __name__ == '__main__':
    unittest.main()