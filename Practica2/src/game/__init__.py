# Puntaje definido para cada una de las acciones
POINTS = {"kills": 3, "assists": 1, "deaths": -1}

# Imprime el encabezado de la tabla de clasificación


def print_header(round_number):
    print(f"\nRanking ronda {round_number}")
    print(f"\n{"Jugador":^10} {"Kills":^10} {"Asistencias":^10} {"Muertes":^10} {"MVPs":^10} {"Puntos":^10}")
    print("-"*70)

# Calcula los puntos de cada jugador en la ronda


def calculate_points(round_table):
    for player in round_table:
        round_table[player]["points"] = round_table[player].get("kills") * POINTS.get("kills") + \
            round_table[player].get("assists") * POINTS.get("assists") + \
            round_table[player].get("deaths") * POINTS.get("deaths")

# Determina el mejor jugador de la ronda


def determine_mvp(round_table):
    mvp = max(round_table, key=lambda x: round_table[x]["points"])
    round_table[mvp]["mvps"] = 1

# Resume en una tabla los datos de la ronda


def round_resume(round):
    round_table = {}
    for player in round:
        round_table[player] = {
            "kills": round[player].get("kills"),
            "assists": round[player].get("assists"),
            "deaths": 1 if round[player].get("deaths") == True else 0,
            "mvps": 0,
            "points": 0
        }
    calculate_points(round_table)
    determine_mvp(round_table)
    return round_table

# Actualiza la tabla global con los datos de la ronda


def update_global_table(global_table, round_table):
    for player in global_table:
        global_table[player]["kills"] += round_table[player]["kills"]
        global_table[player]["assists"] += round_table[player]["assists"]
        global_table[player]["deaths"] += round_table[player]["deaths"]
        global_table[player]["mvps"] += round_table[player]["mvps"]
        global_table[player]["points"] += round_table[player]["points"]

# Imprime la tabla de la ronda


def print_round_table(round_table):
    round_table_sorted = sorted(
        round_table.items(), key=lambda x: x[1]["points"], reverse=True)
    for player, stats in round_table_sorted:
        print(f"{player:^10} {stats.get('kills'):^10} {stats.get('assists'):^10} {stats.get('deaths'):^10} {stats.get('mvps'):^10} {stats.get('points'):^10}")
    print("-"*70)

# Genera las estadísticas de la ronda y la imprime


def round_stats(round, round_number, global_table):

    print_header(round_number)
    round_table = round_resume(round)
    update_global_table(global_table, round_table)
    print_round_table(round_table)

# Imprime la tabla global


def print_global_table(global_table):

    print_header("Final")
    print_round_table(global_table)
