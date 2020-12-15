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
        sleep(10)

    # Test sur l'ajout d'un produit sans être connecté
    def test_notConnected(self):
        self.driver.get("http://esig-sandbox.ch/team20_1_v2/produitEntier.php?id=3")
        self.driver.find_element_by_name("quantite").send_keys(2)
        self.driver.find_element_by_name("ajoutPanier").click()
        self.driver.implicitly_wait(5)
        error = self.driver.find_element_by_class_name(".card .card-cascade .wider .reverse")
        #error = self.driver.find_element_by_class_name("card card-cascade wider reverse")
        assert "Vous devez être connecté pour ajouter cet article à votre panier." in error
        sleep(15000)

if __name__ == '__main__':
    unittest.main()