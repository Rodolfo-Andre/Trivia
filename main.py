# Importaciones de librerías
import random
import time
import re

# Constantes de Colores
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[39m'
BLUE = '\033[34m'

# Pantalla de Bienvenida
print(
    "Bienvenido a mi trivia, en esta ocasión tocaremos el tema de programación"
)
time.sleep(3)

print("Prepárate porque pondremos a prueba tus conocimientos\n")
time.sleep(2)

# Almacenando el nombre del usuario quitando los espacios de inicial y al final de la cadena
name = input("Ingresa tu nombre: ").strip()

# Obteniendo el objeto pattern para validar entradas de cadenas de caracteres
pattern = re.compile("^([A-Za-záéíóúÁÉÍÓÚ]+\s?)+$")

# Validando con expresiones regulares que se ingrese un nombre válido
while (pattern.match(name) == None):
    name = input("Nombre no válido. Ingresa tu nombre correctamente: ").strip()

# Variable booleana que va a decidir si se va a volve a jugar la trivia
startTrivia = True

# Nro de intentos
attempt = 0

# Puntaje
score = 0

# Lista que va a servir para almacenar el historial de putanjes
listScore = []

# Describiendo las instrucciones
print(
    f"\nHola {name} responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
)

# Lista de alternativas
listAlternatives = ["a", "b", "c", "d"]


# Función de desordenado de lista
def shuffleList(listAlternatives):
    # Desordenando lista
    random.shuffle(listAlternatives)

    # Obteniendo datos de la lista de alternativas que ha sido previamente desordenado
    alternate1, alternate2, alternate3, alternate4 = listAlternatives

    # Retornando las preguntas con sus respuestas en una lista de diccionarios
    return [{
        "question": "¿Quién fue el creador de Linux?",
        "alternatives": {
            alternate1: "Linus Torvalds",
            alternate2: "Bill Gates",
            alternate3: "Steve Jobs",
            alternate4: "Steve Wozniak"
        },
        "answers": {
            "correct": {
                "name":
                "Linus Torvalds",
                "description":
                "En 1991, Linus Torvalds diseña el sistema operativo open source llamado Linux"
            },
            "incorrect": {
                "name":
                "Bill Gates",
                "description":
                "Bill Gates con Paul Allen son los fundadores de Microsoft, empresa en la que se desarrolló el sistema operativo Windows"
            },
            "...": {
                "name":
                "Steve Wozniak",
                "description":
                "Steve Wozniak forma parte de los fundadores de Apple, empresa en la se creó el sistema operativo Mac OS"
            },
            "totallyWrong": {
                "name":
                "Steve Jobs",
                "description":
                "Steve Jobs forma parte de los fundadores de Apple, empresa en la se creó el sistema operativo Mac OS"
            }
        }
    }, {
        "question": "¿Cuál de estos lenguajes es de tipado fuerte?",
        "alternatives": {
            alternate1: "JavaScript",
            alternate2: "PERL",
            alternate3: "PHP",
            alternate4: "Haskell"
        },
        "answers": {
            "correct": {
                "name": "Haskell",
                "description": "Haskell es un lenguaje de tipado fuerte"
            },
            "incorrect": {
                "name": "PHP",
                "description": "PHP es un lenguaje de tipado débil"
            },
            "...": {
                "name": "JavaScript",
                "description": "JavaScript es un lenguaje de tipado débil"
            },
            "totallyWrong": {
                "name": "PERL",
                "description": "PERL es un lenguaje de tipado débil"
            }
        }
    }, {
        "question": "¿Qué tipo de dato almacena solo verdadero o falso?",
        "alternatives": {
            alternate1: "String",
            alternate2: "Boolean",
            alternate3: "Int",
            alternate4: "Float"
        },
        "answers": {
            "correct": {
                "name":
                "Boolean",
                "description":
                "Los tipos booleanos solo pueden almacenar True o False"
            },
            "incorrect": {
                "name": "Int",
                "description": "Los tipos int solo almacena valores enteros"
            },
            "...": {
                "name": "String",
                "description":
                "Los tipos string almacena cadenas de caracteres"
            },
            "totallyWrong": {
                "name":
                "Float",
                "description":
                "Los float son de tipo numéricos que permite representar datos positivos y negativos decimales"
            }
        }
    }]


# Pantalla de carga
for i in range(0, 5, +1):
    if (i == 0):
        print("Cargando Preguntas.", end="")
    else:
        print(".", end="")
    time.sleep(1)

print("\n")

while startTrivia:
    # Ejecutando función
    listQuestions = shuffleList(listAlternatives)
    time.sleep(2)

    #Inicializando una variable con un número aleatorio
    score = random.randint(0, 11)
    print(f"{BLUE}Comenzarás con {score} puntos{RESET}\n")
    time.sleep(2)

    # Recorriendo la lista de preguntas
    for i in range(len(listQuestions)):
        # Mostrando las preguntas
        print(f"{i+1}) {listQuestions[i]['question']}")

        # Mostrando las alternativas
        for item in sorted(listQuestions[i]["alternatives"].items()):
            print(f"{item[0]}) {item[1]}")

        # Esperando a que el usuario ingrese una respuesta
        response = input("\nTu respuesta: ")

        # Si la respuesta no es lo que esperamos, volvemos a solicitarle una correcta
        while response.casefold() not in (*listAlternatives, "p"):
            response = input(
                "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
            )

        time.sleep(2)
        # Primero validando la respuesta secreta
        if response == "p":
            print(
                f"\n{MAGENTA}------------------------------------------------------------------------"
            )
            print(
                f"FELICITACIONES {name}!!! HAZ ENCONTRADO EL CÓDIGO SECRETO, CÓMO RECOMPENSA, GANAS SASTIFACTORIAMENTE LA PARTIDA :)"
            )
            print(
                f"------------------------------------------------------------------------\n{RESET}"
            )
            # Asignamos el valor máximo
            score = 99999999
            # Detenemos el flujo de ejecución del bucle
            break

        # Validando respuesta indicada
        if (listQuestions[i]["alternatives"][response] == listQuestions[i]
            ["answers"]["correct"]["name"]):
            print(
                f"\n{GREEN}Respuesta correcta!!! {listQuestions[i]['answers']['correct'] ['description']}{RESET}"
            )
            sum = random.randint(2, 10) * 2
            score += sum
            print(f"\n{GREEN}Se te suman {sum} puntos{RESET}")

        # Validando respuesta menos indicada
        if (listQuestions[i]["alternatives"][response] == listQuestions[i]
            ["answers"]["totallyWrong"]["name"]):
            print(
                f"\n{CYAN}Respuesta menos indicada!!! {listQuestions[i]['answers']['totallyWrong'] ['description']}{RESET}"
            )
            sum = random.randint(1, 4)
            score += sum
            print(f"\n{CYAN}Se te suman {sum} puntos{RESET}")

        # Validando respuesta incorrecta
        if (listQuestions[i]["alternatives"][response] == listQuestions[i]
            ["answers"]["incorrect"]["name"]):
            print(
                f"\n{YELLOW}Respuesta incorrecta!!! {listQuestions[i]['answers']['incorrect'] ['description']}{RESET}"
            )
            score -= 5
            print(f"\n{YELLOW}Se te restan 5 puntos{RESET}")

        # Validando la respuesta más disparatada
        if (listQuestions[i]["alternatives"][response] == listQuestions[i]
            ["answers"]["..."]["name"]):
            print(
                f"\n{RED}... {listQuestions[i]['answers']['...'] ['description']}{RESET}"
            )
            division = random.randint(2, 6)
            score /= division
            print(f"\n{RED}Tu puntaje actual es dividido en {division}{RESET}")

        time.sleep(2)
        # Mostrando puntaje actual
        print(f"\n{BLUE}Puntaje Actual: {score}{RESET}\n")

    time.sleep(2)

    # Bono que puede beneficiar o perjudicar al usuario
    bonus = random.randint(1, 11)

    # Variable que se va a sumar o restar dependiendo del resultado del bonus
    num = random.randint(1, 11)

    # Evaluando el valor del bonus
    if (bonus == 5):
        score += num
        print(f"ENHORABUENA!!! HAS GANADO UN BONUS DE {num} PUNTOS")
    elif (bonus == 2):
        score -= num
        print(f"QUE MAL :c !!! SE TE RESTAN {num} PUNTOS")
    else:
        print("No has ganado ningún bono")

    time.sleep(2)
    # Mostrando puntaje final
    print(f"\n{MAGENTA}Puntaje Final: {score}{RESET}\n")

    # Agregando puntaje al historial
    listScore.append(score)

    time.sleep(2)
    print("¿Deseas intentar la trivia nuevamente?")
    repeatTrivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )
    # Validando si el usuario desea volver a jugar
    if (repeatTrivia != "si"):
        startTrivia = False
    else:
        score = 0
        attempt += 1
        print("")

print(
    f"\n{BLUE}Intentos realizados: {attempt}. Gracias por jugar {name}!!!. Estos son tus puntajes obtenidos: \n{RESET}"
)

# Imprimiendo la lista de puntajes
for i in range(len(listScore)):
    print(f"{MAGENTA}Partida nro {i+1}: {listScore[i]}{RESET}")
