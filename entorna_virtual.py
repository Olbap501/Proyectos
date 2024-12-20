from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Dependencias tecnologicas</h1> <a href="/rarandomndom">¡Ver un dato aleatorio!</a><h2>Te podria intersar</h2><a href="/contraseña">¡Generar contraseña!</a>'


@app.route("/random")
def factores():
    list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
            "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
            "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
            "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
            "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
            "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
            "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"
            ]

    fact = random.choice(list)

    return f"<p> {fact} </p><a href='/'>¡Volver!"


@app.route("/contraseña")
def generar_contraseña():
    caracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    n_caracter = random.randint(4, 12)
    password = ""

    for i in range(n_caracter):
        generation = random.randint(0, 71)
        password += str(caracter[generation])

    return f"<p> {password} </p><a href='/'>¡Volver!</a><h2>    </h2><a href='/contraseña'>¡Otra!"

app.run(debug=True)
