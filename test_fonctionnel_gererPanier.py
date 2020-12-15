from selenium import webdriver
from time import sleep

# Connexion en tant que client au site Yatara Massages
def loginClient():
    driver = webdriver.Chrome("drivers\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.esig-sandbox.ch/team20_1_v2/connexion.php")
    name = driver.find_element_by_id("fname")
    name.send_keys("inlo")
    password = driver.find_element_by_id("lname")
    password.send_keys("inlo1234")
    login = driver.find_element_by_name("formconnexion")
    login.click()
    sleep(100000)



if __name__ == '__main__':
    loginClient()
