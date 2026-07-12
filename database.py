import sqlite3
from datetime import datetime

DATABASE = "movieai.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie TEXT NOT NULL,
        search_time TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS favorites(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie TEXT UNIQUE NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def save_history(movie):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history(movie, search_time) VALUES(?, ?)",
        (movie, datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    )

    conn.commit()
    conn.close()


def get_history():
    conn = get_connection()

    rows = conn.execute(
        "SELECT * FROM history ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return rows


def add_favorite(movie):
    conn = get_connection()

    try:
        conn.execute(
            "INSERT INTO favorites(movie) VALUES(?)",
            (movie,)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        pass

    conn.close()


def remove_favorite(movie):
    conn = get_connection()

    conn.execute(
        "DELETE FROM favorites WHERE movie=?",
        (movie,)
    )

    conn.commit()
    conn.close()


def get_favorites():
    conn = get_connection()

    rows = conn.execute(
        "SELECT * FROM favorites ORDER BY movie"
    ).fetchall()

    conn.close()

    return rows


if __name__ == "__main__":
    create_tables()
    print("Database created successfully.")