def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

poblacion_paises = {
    'argentina': 44938712,
    'brasil': 2101471225,
    'colombia': 50372424,
}

#print(poblacion_paises['bolivia'])

#for pais in poblacion_paises.keys():
    #print(pais)

#for pais in poblacion_paises.values():
    #print(pais)

for pais, poblacion in poblacion_paises.items():
    print(pais + 'tiene ' + str(poblacion + 'habitantes'))

if __name__ == '__main__':
    run()