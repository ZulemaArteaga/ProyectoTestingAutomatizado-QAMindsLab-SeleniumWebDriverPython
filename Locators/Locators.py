from selenium import webdriver

class MyLocators():

    driver = webdriver.Chrome()
    URL = "https://industriamaquiladora.com/"
    file_path = "/Users/zulemaarteaga/Documents/QAMindsSelenumDirectorioIndustriaMaquiladora/Data/dataBase.csv"
    evidencia = "/Users/zulemaarteaga/Documents/QAMindsSelenumDirectorioIndustriaMaquiladora/Evidence/Reporte1.html"

    # POP-UP
    closePopUp_css = "button.close"
    
    # MENU
    menu_css = "li.menumd"
    directorio_conMenuVisible_xPath = '/html/body/section[1]/nav/div[2]/div[2]/ul/li[4]/div/div[1]/a'
    directorio_xPath = '//*[@id="navbarSupportedContent"]/ul/li[5]/a'
    
    # MATERIAL, PRODUCTO O SERVICIO
    materialUnoporUno_css = "div.raya.mayusculas" # ejemplo: Abrasivos, Aceites y lubricantes

    # PROVEEDORES
    proveedores_conMenuVisible_xPath = "/html/body/section[1]/nav/div[2]/div[2]/ul/li[4]/div/div[1]/div/a[2]"
    proveedores_xPath = '//*[@id="navbarSupportedContent"]/ul/li[5]/div/a[2]'
    listaProveedoresdeMaterial_class = "col-md-10" #Frismex,Undustrial
    proveedorInfo_class = "col-md-8"
    nombreProveedor='//*[@id="nombre"]/strong'

    

