import unittest
from selenium import webdriver
from Locators.Locators import MyLocators
from TestCases.TC_1 import TC_1
import HtmlTestRunner

class DirectorioIndustriaMaquiladora(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Inicio de la prueba")
        cls.driver = webdriver.Chrome()
        cls.driver.get(MyLocators.URL)

    def test_1_Encontrar_Proveedores(self):
        driver = self.driver 
        tc_1 = TC_1(driver)
        tc_1.start()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Fin de la prueba")

if __name__ == '__main__':
        #unittest.main()
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=MyLocators.evidencia))
 
DirectorioIndustriaMaquiladora()
