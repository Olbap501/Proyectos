# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
import os

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)



@bot.command()
async def tip(ctx):
    tips = [" Reducir los envases o productos de usar y tirar. El catálogo de acciones que se pueden realizar es infinito: desde optar con el consumo de productos a granel, hasta optar por productos envasados en materiales que después se pueden reciclar con mayor facilidad: papel o cartón o vidrio.",
    "Reducir el despilfarro de alimentos.  Comprando sólo lo que necesitamos, cuidando la conservación y preparación de alimentos, aprovechando las sobras para hacer nuevas recetas y optando por el compostaje orgánico en alguna de sus múltiples opciones: 4º contenedor, compostaje doméstico, compostaje comunitario, etc. ",
    "Decantarnos preferiblemente por productos de origen reciclado. De esta forma reducimos la necesidad de extraer materiales nuevos de la naturaleza y/o destinar recursos energéticos para procesarlos. ",
    "Seleccionar materiales más respetuosos con el medioambiente y con mayor vida útil. Evita los productos lowcost. Por ejemplo, si optamos por materiales textiles con más durabilidad y mejor rendimiento, reducimos la producción de textiles y, sobretodo, la cantidad de ropa que tiramos a la basura por ser ya inservible.",
    "Busca formas de reutilizar los recursos textiles antes de desecharlos. Conviértelos en trapos, utilízalos para hacer manualidades, como envoltorio de regalos, etc. Si necesitas ideas, aquí te damos alguna. ",
    "Opta por la reparación de objetos. Siempre que sea posible, y económicamente viable, es preferible optar por alargar la vida útil de los objetos. ",
    "Copia buenas prácticas para reutilizar residuos. Ahora que todo se ha hecho virtual, la red nos proporciona estupendos recursos para tener ideas. Pinterest, páginas como el-recetario.net o personas como 2ndfunniestthing son referentes para esta tarea. ",
    "Al depositar los residuos, debemos asegurarnos de hacerlo en el contenedor adecuado.",
    "Ante las dudas, acudir a herramientas que facilitan la resolución de las mismas como el buscador AIRE  o el propio de la Mancomunidad de la Comarca de Pamplona.",
    "Visitar plantas de separación y reciclaje. Acercarnos a estas instalaciones no solo nos acerca a los procesos de tratamiento de residuos, sino que nos acerca a los beneficios socioeconómicos y medioambientales de su reciclaje. "]

    await ctx.send( random.choice(tips) )

@bot.command()
async def meme(ctx):
    imagen = random.choice( os.listdir("images") )
    with open(f'images/{imagen}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

recipientes = {
"naranja" : ["sobras", 
              "huesos",
              "espinas",
              "comida podrida",
              "cascaras",
              "cajas de pizza",
              "platos de carton usados"
    ],

"verde" : ["botes de cristal",
            "copas",
            "vasos",
            "botellas de cristal",
            "botes de colonia",
            "tarros de cristal",
            "frascos de cristal"
    ],

"amarillo" : ["botellas de plastico",
                "envases",
                "bricks",
                "botes de plastico",
                "garrafas",
                "latas",
                "madera"
    ]  ,                 

"azul" : ["papel",
            "carton",
            "cajas de carton",
            "papel de regalo",
            "rollos de papel"
    ],

"rojo" : ["aparatos elctonicos",
            "ordenadores",
            "moviles",
            "tablets",
            "productos quimicos",
            "lejia",
            "medicina",
            "productos hospitalario"
    ]}

@bot.command()
async def cubos_reciclaje(ctx, objeto: str):
    
    if objeto.lower() in recipientes["naranja"]:
        await ctx.send( objeto +" debe ir en el recipiente Naranja" )
    elif objeto.lower() in recipientes["verde"]:
        await ctx.send( objeto +" debe ir en el recipiente Verde" )
    elif objeto.lower() in recipientes["amarillo"]:
        await ctx.send( objeto +" debe ir en el recipiente Amarillo" )
    elif objeto.lower() in recipientes["azul"]:
        await ctx.send( objeto +" debe ir en el recipiente Azul" )
    elif objeto.lower() in recipientes["rojo"]:
        await ctx.send( objeto +" debe ir en el recipiente Rojo" )
    else:
        await ctx.send( objeto +" debe ir en el recipiente Gris" )

@bot.command()
async def juego2(ctx):
    reci = random.choice( list(recipientes.keys()) )

    await ctx.send( random.choice( recipientes[reci]) )

@bot.command()
async def juego(ctx):
    reci = random.choice( list(recipientes.keys()) )

    await ctx.send( random.choice( recipientes[reci]) )

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        
        respuesta = await bot.wait_for('message', timeout=30.0, check=check)

        if respuesta.content == reci:
            await ctx.send("Correcto")
        else:
            await ctx.send("Sigue intentado, era: "+reci)
    except:
        await ctx.send("El tiempo se agotó, vuelve a intentarlo")


bot.run('Token')
