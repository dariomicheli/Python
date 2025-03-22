import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Variable para administrar los puntos de usuario
user_points = 0

# Genero las 3 preguntas para el juego sin que se repitan
questions_to_ask = random.sample(
    list(zip(questions, answers, correct_answers_index)), 3)

# El usuario deberá contestar 3 preguntas
for x in range(3):

    question = questions_to_ask[x][0]
    answers_for_question = questions_to_ask[x][1]
    correct_answer = questions_to_ask[x][2]

    # Muestro pregunta y posibles respuestas
    print(question)
    for i, answer in enumerate(answers_for_question):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        if user_answer.isdigit():
            user_answer = int(user_answer)-1
            if user_answer >= 0 and user_answer < 4:
                # Se verifica si la respuesta es correcta
                if user_answer == correct_answer:
                    user_points += 1
                    print("¡Correcto!")
                    break
                else:
                    # Si el usuario no responde correctamente después de 2 intentos,
                    # se muestra la respuesta correcta
                    if user_points >= 0.5:
                        user_points -= 0.5
                    print("Incorrecto. La respuesta correcta es:")
                    print(answers_for_question[correct_answer])
                # Se imprime un blanco al final de la pregunta
                print()
            else:
                print("Repuesta no valida")
                exit(1)
        else:
            print("Repuesta no valida")
            exit(1)

# Imprimo puntaje total del juego
print("Puntaje total: ", user_points)
