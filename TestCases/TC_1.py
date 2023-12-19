import time
from time import perf_counter, sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
from Locators.Locators import MyLocators


class TC_1():
    def __init__(self, driver):
        self.driver = driver
        self.closePopUp_css = MyLocators.closePopUp_css
        self.menu_css = MyLocators.menu_css
        self.directorio_conMenuVisible_xPath = MyLocators.directorio_conMenuVisible_xPath
        self.directorio_xPath = MyLocators.directorio_xPath
        self.materialUnoporUno_css = MyLocators.materialUnoporUno_css
        self.proveedores_conMenuVisible_xPath = MyLocators.proveedores_conMenuVisible_xPath
        self.proveedores_xPath = MyLocators.proveedores_xPath
        self.listaProveedoresdeMaterial_class = MyLocators.listaProveedoresdeMaterial_class
        self.proveedorInfo_class = MyLocators.proveedorInfo_class
        self.nombreProveedor=MyLocators.nombreProveedor

    def start(self):
        self.driver.maximize_window()
        self.driver.get(MyLocators.URL)
        self.driver.implicitly_wait(2)
        
        driver = self.driver
        try:
            MyLocators.closePopUp_css.click() #Close PopUp
        except: 
            pass
        
        # PANTALLA CHICA: Ir a MENU --> DIRECTORIO y después hacer click en "PROVEEDORES" 
        actions = AC(driver)
        try: 
            menuVisible=driver.find_element(By.CSS_SELECTOR, MyLocators.menu_css) 
            actions.move_to_element(to_element=menuVisible).perform()                                               # Va a Menu
            directorio_conMenuVisible=driver.find_element(By.XPATH, MyLocators.directorio_conMenuVisible_xPath)
            actions.move_to_element(to_element=directorio_conMenuVisible).perform()                                 # Va a DIRECTORIO
            proveedores_conMenuVisible_xPath = driver.find_element(By.XPATH, MyLocators.proveedores_conMenuVisible_xPath)
            actions.move_to_element(to_element=proveedores_conMenuVisible_xPath).perform()                          # Va a Proveedores y luego hace click
            proveedores_conMenuVisible_xPath.click()
            
        # Entra aqui cuando es la PANTALLA GRANDE y no esta el MENU, se va directo a DIRECTORIO
        except:                                     
            directorio=driver.find_element(By.XPATH, MyLocators.directorio_xPath)               
            actions.move_to_element(to_element=directorio).perform()                        # Va directo  DIRECTORIO
            proveedores = driver.find_element(By.XPATH, MyLocators.proveedores_xPath)
            actions.move_to_element(to_element=proveedores).perform()                       # VA A PROVEEDORES y hace click
            proveedores.click()
            
            
        # Elegir al menos 20 productos. Los que tengan al menos 3 proveedores,  imprimir en un archivo la información de dichos proveedores.
        i=0
        for each in range(20):
            listaDeMateriales=driver.find_elements(By.CSS_SELECTOR, MyLocators.materialUnoporUno_css)
            #print("Vuelta " + str(i))
            #print(listaDeMateriales[i].text)
            material=listaDeMateriales[i].text
            listaDeMateriales[i].click() #Da click en cada material. Ejemplo: Abrasivos, Aceites y lubricantes
            lista_proveedores_del_material = driver.find_elements(By.CLASS_NAME, MyLocators.listaProveedoresdeMaterial_class)

            # Si el material tiene menos de 3 proveedores, salir y buscar el siguiente proveedor
            if len(lista_proveedores_del_material) <= 2:
                #print("Tiene menos de 3 proveedores" + "\n" + "No se proporcionará información de ningún proveedor"+ "\n" )
                driver.back()
                
        # Si el material tiene mas de 3 proveedores, imprimir la información de los 3 primeros proveedores
            elif len(lista_proveedores_del_material) >= 3:
                time.sleep(1)
                x=0
                for each in range(3): # Para que encuetre los primeros 3 proveedores
                    driver.find_elements(By.CLASS_NAME, MyLocators.listaProveedoresdeMaterial_class)[x].click() # Da click en el primer prooveedor de la lista de materiales
                    proveedor=driver.find_element(By.XPATH, MyLocators.nombreProveedor).text
                    lista_de_Datos=driver.find_elements(By.CLASS_NAME, MyLocators.proveedorInfo_class)
                    #print(proveedor)
                    direccion=lista_de_Datos[0].text
                    ciudad=lista_de_Datos[1].text
                    estado=lista_de_Datos[2].text
                    pais=lista_de_Datos[3].text
                    telefono=lista_de_Datos[4].text
                    variable_field=lista_de_Datos[5].text
                    if "@" in variable_field:
                        # print("@ existe")
                        correo = variable_field
                        sitioWeb=lista_de_Datos[6].text
                        contacto=lista_de_Datos[7].text
                    else:
                        # print("@ no existe")
                        correo = lista_de_Datos[6].text
                        sitioWeb=lista_de_Datos[7].text
                        contacto=lista_de_Datos[8].text
                    data = '"'+ material + '"' + ';' + '"' + proveedor + '"'  + ';' +  '"'+ direccion +'"'  + ';' +  '"'+ ciudad +'"'  + ';' +  '"'+ estado +'"'  + ';' +  '"'+ pais+'"'  + ';' +  '"' + telefono + '"'  + ';' +  '"' + correo + '"'  + ';' +  '"' + sitioWeb + '"' + ';' + '"' + contacto+'"' + "\n"
                    with open(MyLocators.file_path,'a') as fd: # Corre y va guardando la información una por una
                        fd.write(data)
                    #print("Proveedor:" + proveedor + "\n" + "Direccion:" + direccion + "\n" + "Ciudad: " + ciudad + "\n" + "Estado: " + estado + "\n" + "Pais: " + pais +"\n"+ telefono +"\n"+ correo +"\n"+ sitioWeb +"\n"+ contacto +"\n")
                    x=x+1
                    driver.back()   #Sale del proveedor 
                driver.back()
            i=i+1
     

      




       
            
        
     