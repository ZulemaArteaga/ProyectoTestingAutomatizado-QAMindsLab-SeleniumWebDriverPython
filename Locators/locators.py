class MyLocators():
    URL = "https://industriamaquiladora.com/"
    file_path = '/Users/zulemaarteaga/Documents/GitRepos/Python-Selenium-ProjectoIndustriaMaquiladora/Data/dataBase.csv'

    # POP-UP
    closePopUp_css = "button.close"
    
    # MATERIAL, PRODUCTO O SERVICIO
    materialUnoporUno = "div.raya.mayusculas" # ejemplo: Abrasivos, Aceites y lubricantes

    # PROVEEDORES
    proveedores = '#navbarSupportedContent > div.d-none.d-md-block.navbar-buttons.mbr-section-btn > a:nth-child(2)'
    listaProveedoresdeMaterial = "//div[@class='col-md-10']" #Frismex,Undustrial
    proveedorInfo = "div.mbr-section-subtitle .row"

    direccion = ".mbr-section-subtitle .row:nth-of-type(1) .col-md-8"
    ciudad = ".mbr-section-subtitle .row:nth-of-type(2) .col-md-8"
    estado = ".mbr-section-subtitle .row:nth-of-type(3) .col-md-8"
    pais = ".mbr-section-subtitle .row:nth-of-type(4) .col-md-8"
    telefono = ".mbr-section-subtitle .row:nth-of-type(5) .col-md-8"


