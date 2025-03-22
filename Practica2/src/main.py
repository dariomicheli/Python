import string

zen_text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

titles = [
    "Speedrun de Super Mario en tiempo récord",
    "Charla sobre desarrollo de videojuegos",
    "Jugando al nuevo FPS del momento con amigos",
    "Música en vivo: improvisaciones al piano"
]

rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""

descriptions = [
    "Streaming de música en vivo con covers y composiciones",
    "Charla interactiva con la audiencia sobre series y películas",
    "Jugamos a juegos retro y charlamos sobre su historia",
    "Exploramos la mejor música de los 80s y 90s",
    "Programa de entretenimiento con noticias y curiosidades del mundo gamer",
    "Sesión de charla con invitados especiales del mundo del streaming",
    "Música en directo con improvisaciones y peticiones del chat",
    "Un espacio para charlar relajada sobre tecnología y cultura digital",
    "Exploramos el impacto de la música en los videojuegos clásicos"
]

# Imprime las oraciones cuya segunda palabra empieza con vocal.


def imprimir_vocal(text):
    sentences = text.split(".\n")
    for sentence in sentences:
        words = sentence.split()
        if words[1].startswith(("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")):
            print(sentence)

# Imprime la oración con más palabras de una lista


def imprimir_mas_palabras(lista):
    max = -1
    for i in range(len(lista)):
        amount = len(lista[i].split())
        if amount > max:
            max = amount
            pos = i
    print("El titulo más largo es: ", lista[pos])

# Imprime las reglas segun una palabra clave


def imprimir_regla(text, keyword):
    sentences = text.lower().split(".\n")
    for sentence in sentences:
        if keyword.lower() in sentence:
            print(sentence.capitalize())

# Validar nombre de usuario


def validate_username(username):
    if len(username) < 5:
        return False

    if not any(c.isdigit() for c in username):
        return False

    if not any(c in string.ascii_uppercase for c in username):
        return False

    if not username.isalnum():
        return False

    return True

# Devuelve la categoria segun el tiempo ingresado


def clasification(time):
    if int(time) < 200:
        return "Rápido"
    if 200 <= int(time) <= 500:
        return "Normal"
    return "Lento"

# Devuelve la cantidad de menciones de la palabra "entretenimiento", "música" y "charla"


def count_mentions(lista):
    dic_keyword = {"música": 0, "entretenimiento": 0, "charla": 0}
    for elem in lista:
        dic_keyword["entretenimiento"] += elem.lower().count("entretenimiento")
        dic_keyword["música"] += elem.lower().count("música")
        dic_keyword["charla"] += elem.lower().count("charla")
    print(f"Menciones de 'música': {dic_keyword.get("música")}\nMenciones de 'charla': {dic_keyword.get("charla")}\nMenciones de 'entretenimiento': {dic_keyword.get("entretenimiento")}")


# imprimir_vocal(zen_text)
# imprimir_mas_palabras(titles)
# imprimir_regla(rules, "moderadores")
""" if validate_username(input("Ingrese un nombre de usuario:")):
    print("El nombre de usuario es valido")
else:
    print("El nombre de usuario no cumple con los requisitos") """

# print(f"Categoria: {clasification(input("Ingrese su tiempo de reacción:"))}")
count_mentions(descriptions)
