from flask import Flask, render_template
app =  Flask(__name__)

@app.route('/prueba')
def prueba():
    paises = [
        {
            'nombre':'Argentina',
            'Moneda':'Pesos Argentinos',
            'Capital':' Rio de Janeiro',
            'Poblacion':' 654327',
            'Superficie':' 76374 km2',
            'CiudadesPrincipales':'a',
        },
        {
            'nombre':'Brasil',
            'Moneda':'Reales',
            'Capital':'Brasilia',
            'Poblacion':' 12243',
            'Superficie':' 6734726 km',
            'CiudadesPrincipales':'Rio de Janeiro',
        },
        {
            'nombre':'Francia',
            'Moneda':'Euros Franceses',
            'Capital':' Paris',
            'Poblacion':' 123342',
            'Superficie':' 83748 km',
            'CiudadesPrincipales':'a',
        },
        {
            'nombre':'Colombia',
            'Moneda':'Pesos',
            'Capital':' Bogota',
            'Poblacion':' 6565627',
            'Superficie':' 764372 km',
            'CiudadesPrincipales':'a',
        },
        {
            'nombre':'España',
            'Moneda':'Euros',
            'Capital':' Madrid',
            'Poblacion':' 526452',
            'Superficie':' 76378 km ',
            'CiudadesPrincipales':'a',
        }
    ]
    return render_template('paises.html',
                            paises=paises,
                            usuario="Cristian",)