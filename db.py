import psycopg2
from psycopg2 import sql


def connect_db():
    conn_params = {
        "dbname": "tuolaji_db",
        "user": "stevenhhb",
        "password": "727300Steven",  # Use your actual password here
        "host": "localhost"
    }
    try:
        conn = psycopg2.connect(**conn_params)
        return conn
    except Exception as e:
        print(f"Cannot connect to the database: {e}")
        return None


def get_or_create_player(player_name):
    conn = connect_db()
    with conn.cursor() as cursor:
        # Check if player exists and get ID
        cursor.execute(
            "SELECT player_id FROM players WHERE player_name = %s;", (player_name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            # Insert new player and return new ID
            cursor.execute(
                "INSERT INTO players (player_name) VALUES (%s) RETURNING player_id;", (player_name,))
            player_id = cursor.fetchone()[0]
            conn.commit()
            return player_id
    conn.close()
# Insert a new game record and return its game_id


def start_new_game():
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO games (start_time) VALUES (NOW()) RETURNING game_id;")
        game_id = cursor.fetchone()[0]
        conn.commit()
    conn.close()
    return game_id

# Record a move in the database


def record_move(game_id, player_id, move_details):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO moves (game_id, player_id, move_details, move_time) VALUES (%s, %s, %s, NOW());",
            (game_id, player_id, move_details)
        )
        conn.commit()
    conn.close()

# Update the game's outcome


def end_game(game_id, outcome):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE games SET end_time = NOW(), outcome = %s WHERE game_id = %s;",
            (outcome, game_id)
        )
        conn.commit()
    conn.close()
