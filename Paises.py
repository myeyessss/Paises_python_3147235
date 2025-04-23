paises = [
            {
                "nombre" : "Venezuela",
                "capital" : "Caracas",
                "moneda" : "Bolivar",
                "superficie" : "916,445 km²",
                "poblacion" : 
                        {
                            "censo": 26,
                            "densidad" : 31
                         },
                "ciudades": [
                                "Maracaibo",
                                "Caracas",
                                "Maracay",
                                "Barquisimeto",
                                "Valencia",
                                "Mérida",
                                "San Cristóbal",
                                "Barinas",
                                "Punto Fijo",
                                "Ciudad Bolívar",
                                "Cumaná",
                                "San Fernando de Apure",
                                "Acarigua",
                            ]
                    
                    
            },
            {
                "nombre" : "Brasil",
                "capital" : "Brasilia",
                "moneda" : "Real",
                "superficie": "8.51 millones km²",
                "poblacion":
                        {
                             "censo": 212,
                             "densidad" : 25
                         },
                
                "ciudades": [
                                "São Paulo",
                                "Rio de Janeiro",
                                "Salvador",
                                "Belo Horizonte",
                                "Porto Alegre",
                                "Curitiba",
                                "Goiânia",
                                "Recife",
                                "Guarulhos",
                                "Campinas",
                                "Fortaleza",
                            ]
            },
            {    
                "nombre" : "Paraguay",
                "capital" : "Asunción",
                "moneda" : "Guarani",
                "superficie": "406,752 km²",
                "poblacion":
                        {
                            "censo": 7,
                            "densidad" : 17
                        },
                "ciudades": [
                                "Ciudad del Este",
                                "Lambaré",
                                "San Lorenzo",
                                "Capiatá",
                                "Limpio",
                                "Cerro Corá",
                            ]
                
                    
            }
         ]
# Recorrer todos los paises:
print ("Recorriendo todos los países:")
for pais in paises:
    print("Ciudades Principales")
    for ciudad in pais["ciudades"]:
        print("-", ciudad)

    print("nombre:" , pais["nombre"])
    print("capital:" , pais["capital"])
    print("poblacion")
    print("censo" , pais["poblacion"]["censo"] ,"millones")
    print("densidad" , pais["poblacion"]["densidad"] ,"personas por km2")
    print("ciudades" , pais["ciudades"])
    print("superficie:" , pais["superficie"] ,)


    print("---------------------------------")
    # Recorrer todos los paises y mostrar su capital y población: