from logging import exception
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

currentUser = 'Hinojosa Rojas Pedro Saúl'
currentUserId = 'e1004789632'

opcionesNav = ['Inicio', 'Perfil', 'Registro Académico',
              'Notas', 'Horario', 'Sílabo', 'Pagos',
              'Evaluación', 'Matrículas', 
              'Ficha Socioeconómica', 'Becas']

linksNav = ['/', 'perfil', 'registro_academico',
              'notas', 'horario', 'silabo', 'pagos',
              'evaluacion', 'matriculas', 
              'ficha_socioeconomica', 'becas']



@app.route('/')
def index():
    opcionesMenuLat = ['Inicio', 'Perfil Estudiantil', 'Registro Académico',
              'Notas', 'Horario', 'Pagos Realizados',
              'Evaluación a Docentes', 'Matrículas', 
              'Ficha Socioeconómica', 'Formatos de Vinculación', 'Becas']

    linksMenuLat = ['/', 'perfil', 'registro_academico',
              'notas', 'horario', 'pagos',
              'evaluacion', 'matriculas', 
              'ficha_socioeconomica', 'formatos_vinculacion', 'becas']
    data = {
        'titulo': '',
        'tituloEnc': 'Portafolio Estudiantil',
        'tituloEncNav': 'Inicio',
        'usuario': currentUser,
        'UUID': currentUserId,
        'opcionesNav': opcionesNav,
        'linksNav': linksNav,
        'opcionesMenuLat': opcionesMenuLat,
        'linksMenuLat': linksMenuLat,
        'numOpcionesNav': len(linksMenuLat)
    }

    return render_template('inicio.html', data=data)

@app.route('/perfil')
def perfil():
    n = 1
    data = {
        'titulo': opcionesNav[n] + ' | ',
        'tituloEnc': 'Portafolio Estudiantil',
        'tituloEncNav': opcionesNav[n],
        'usuario': currentUser,
        'UUID': currentUserId,
        'opcionesNav': opcionesNav,
        'linksNav': linksNav,
        'numOpcionesNav': len(opcionesNav)
    }
    return render_template('perfil.html',data=data)

@app.route('/registro_academico')
def registro_academico():
    n = 2
    data = {
        'titulo': opcionesNav[n] + ' | ',
        'tituloEnc': 'Portafolio Estudiantil',
        'tituloEncNav': opcionesNav[n],
        'usuario': currentUser,
        'UUID': currentUserId,
        'opcionesNav': opcionesNav,
        'linksNav': linksNav,
        'numOpcionesNav': len(opcionesNav)
    }
    return render_template('registro_academico.html',data=data)

@app.route('/horario')
def horario():
    n = 4
    data = {
        'titulo': opcionesNav[n] + ' | ',
        'tituloEnc': 'Portafolio Estudiantil' ,
        'tituloEncNav': opcionesNav[n],
        'usuario': currentUser,
        'UUID': currentUserId,
        'opcionesNav': opcionesNav,
        'linksNav': linksNav,
        'numOpcionesNav': len(opcionesNav)
    }
    return render_template('horario.html',data=data)

if __name__ == '__main__':
	app.run(debug=True, port=5000)


