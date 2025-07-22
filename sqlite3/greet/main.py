"""Greetings from sqlite3"""

import sqlite3


def insert_greeting(con: sqlite3.Connection, greeting: str):
    """Insert greeting"""

    cur = con.cursor()
    print(f"Inserting greeting {greeting}...")
    cur.execute("INSERT INTO greetings (greeting) VALUES (?)", (greeting,))
    con.commit()


def list_greetings(con: sqlite3.Connection):
    """List greetings"""

    cur = con.cursor()
    print("Listing greetings...")
    for row in cur.execute("SELECT * FROM greetings"):
        print(row)


def get_id(con: sqlite3.Connection, greeting_id: int):
    """Get greeting by ID"""

    cur = con.cursor()
    print(f"Getting greeting by ID {greeting_id}...")
    res = cur.execute("SELECT * FROM greetings WHERE id = ?", (greeting_id,))
    if g := res.fetchone():
        print(g)


def get_text(con: sqlite3.Connection, text: str):
    """Get greeting by text"""

    cur = con.cursor()
    print(f"Getting greeting by text \"{text}\"...")
    res = cur.execute("SELECT * FROM greetings WHERE greeting = ?", (text,))
    if g := res.fetchone():
        print(g)


def delete_id(con: sqlite3.Connection, greeting_id: int):
    """Delete greeting by ID"""

    cur = con.cursor()
    print(f"Deleting greeting by ID {greeting_id}...")
    cur.execute("DELETE FROM greetings WHERE id = ?", (greeting_id,))
    con.commit()


def main():
    """Main entry point"""

    # create db connection and cursor
    con = sqlite3.connect(":memory:")
    cur = con.cursor()

    # create table
    create_stmt = """CREATE TABLE greetings (
        id INTEGER NOT NULL PRIMARY KEY,
        greeting TEXT NOT NULL
    );"""
    cur.execute(create_stmt)

    # insert greetings
    for greeting in ("hello", "hi", "good day", "greetings"):
        insert_greeting(con, greeting)

    # list greetings
    list_greetings(con)

    # get greeting by id
    get_id(con, 1)

    # get greeting by text
    get_text(con, "hi")

    # delete greeting by id
    delete_id(con, 1)
    list_greetings(con)


if __name__ == "__main__":
    main()
