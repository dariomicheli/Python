import game
import string
import random

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

clients = [
    " Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
    " Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
    "luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
    " ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
    "carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES",
    "alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
    "patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
    "MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
    "SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
    "Damián Castillo ", None, "", " "
]

rounds = [
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
        'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
        'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
        'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
        'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
    }
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
    if len(username) < 10:
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
    if 200 <= int(time) <= 1000:
        return "Normal"
    return "Lento"

# Devuelve la cantidad de menciones de la palabra "entretenimiento", "música" y "charla"


def count_mentions(lista):
    dic_keyword = {"música": 0, "entretenimiento": 0, "charla": 0}
    for elem in lista:
        words = elem.lower().split()
        dic_keyword["entretenimiento"] += words.count("entretenimiento")
        dic_keyword["música"] += words.count("música")
        dic_keyword["charla"] += words.count("charla")
    print(f"Menciones de 'música': {dic_keyword.get("música")}\nMenciones de 'charla': {dic_keyword.get("charla")}\nMenciones de 'entretenimiento': {dic_keyword.get("entretenimiento")}")

# Genera codigo de descuento


def generate_random_string(lenght):
    return "".join(random.choices(string.ascii_letters + string.digits, k=lenght))


def code_discount(username, date):
    code_length = 30

    if len(username) > 15:
        print("El usuario excede los 15 caracteres")
        return

    code = username.upper() + "-" + date.replace("-", "").upper() + "-"
    word_amount = len(code)
    if word_amount < code_length:
        random_string = generate_random_string(code_length-word_amount)
        code += random_string.upper()
    print(f"Código de descuento: {code}")

# Determina si 2 palabras son anagramas


def validar_anagrama(word1, word2):
    if len(word1) != len(word2):
        return False

    return sorted(word1.lower()) == sorted(word2.lower())

# Limpia los nombres de una lista


def clean_name(list):
    list_names = []
    set_names = set()
    for full_name in list:
        if full_name not in (None, " ", ""):
            name, surname = full_name.split()
            set_names.add(name.lower().capitalize() +
                          " " + surname.lower().capitalize())
    for full_name in set_names:
        list_names.append(full_name)
        list_names.sort()
    print(list_names)


# Ejecicio 1

imprimir_vocal(zen_text)

# Ejercicio 2
imprimir_mas_palabras(titles)

# Ejercicio 3
imprimir_regla(rules, "moderadores")

# Ejercicio 4
if validate_username(input("Ingrese un nombre de usuario:")):
    print("El nombre de usuario es valido")
else:
    print("El nombre de usuario no cumple con los requisitos")

# Ejercicio 5

print(f"Categoria: {clasification(input("Ingrese su tiempo de reacción:"))}")

# Ejercicio 6
count_mentions(descriptions)

# Ejercicio 7

code_discount(input("Usuario: "), "20210-04-10")

# Ejercicio 8

word1 = input("Ingrese la primera palabra: ")
word2 = input("Ingrese la segunda palabra: ")
if validar_anagrama(word1, word2):
    print("Son anagramas")
else:
    print("No son anagramas")

# Ejercicio 9

clean_name(clients)

# Ejercicio 10

global_table = {
    'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
    'Blaze': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
    'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
    'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
    'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0}
}

round_number = 0
for round in rounds:
    round_number += 1
    game.round_stats(round, round_number, global_table)
game.print_global_table(global_table)
