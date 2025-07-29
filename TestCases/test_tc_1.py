from seleniumbase import BaseCase
from Locators.locators import MyLocators

class test_tc_1(BaseCase):
    def test_tc_1_collect_provider_data(self):
        self.maximize_window()
        self.open(MyLocators.URL)
        self.sleep(2)

        self.click(MyLocators.closePopUp_css)
        self.wait_for_element_visible(MyLocators.proveedores)
        self.click(MyLocators.proveedores)

        # Elegir al menos 20 productos. Los que tengan al menos 3 proveedores,
        # Imprimir en un archivo la información de dichos proveedores.
        i = 0
        for i in range(3):
            listaDeMateriales = self.find_elements(MyLocators.materialUnoporUno)
            material = listaDeMateriales[i]
            # print(f'Vuelta: {i}, {material.text}')
            material.click()

            listaDeProveedores = self.find_elements(MyLocators.listaProveedoresdeMaterial)

            # Si el material tiene menos de 2 o menos proveedores, salir y buscar el siguiente proveedor
            if len(listaDeProveedores) <= 2:
                self.go_back()

            # Si el material tiene mas de 3 proveedores, imprimir la información de los 3 primeros proveedores
            elif len(listaDeProveedores) >= 3:
                self.wait(1)
                x = 0
                for x in range(3):
                    listaDeProveedores = self.find_elements(MyLocators.listaProveedoresdeMaterial)
                    proveedor = listaDeProveedores[x]
                    nombre_proveedor = proveedor.text.split('\n')[0].strip()
                    proveedor.click()

                    direccion = self.find_element(MyLocators.direccion).text.strip()
                    ciudad = self.find_element(MyLocators.ciudad).text.strip()
                    estado = self.find_element(MyLocators.estado).text.strip()
                    pais = self.find_element(MyLocators.pais).text.strip()
                    telefono = self.find_element(MyLocators.telefono).text.strip()

                    lista_de_Datos = self.find_elements(MyLocators.proveedorInfo)
                    variable_field = lista_de_Datos[6].text.strip()

                    if "@" in variable_field:
                        correo = variable_field
                        sitioWeb = lista_de_Datos[7].text.strip()
                        contacto = lista_de_Datos[8].text.strip()
                    else:
                        correo = "N/A"
                        sitioWeb = lista_de_Datos[6].text.strip()
                        contacto = lista_de_Datos[7].text.strip()

                    #Writte data to CSV file
                    expected_headers = '"Proveedor","Dirección","Ciudad","Estado","País","Teléfono","Correo","Sitio Web","Contacto"'
                    with open(MyLocators.file_path, 'r+') as fd:
                        first_line = fd.readline().strip()
                        if first_line != expected_headers:
                            fd.write(expected_headers + '\n')

                        data_row = (
                            f'"{nombre_proveedor}","{direccion}","{ciudad}","{estado}","{pais}","{telefono}","{correo}","{sitioWeb}","{contacto}"\n'
                        )
                        fd.write(data_row)

                    x = x + 1
                    self.go_back() # Sale del proveedor
                self.go_back()
            i = i + 1
