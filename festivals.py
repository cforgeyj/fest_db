import sqlite3
from sqlite3 import Error

def __init__(self, name, schema):
    # error handling
    if not name:
        raise RuntimeError("invalid table name")
    if not schema:
        raise RuntimeError("invalid database schema")

    # init fields and initiate database connection
    self.name = name
    self.schema = schema
    self.db_conn = sqlite3.connect(self.DB_NAME)

    # ensure the table is created
    self.create_table()


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_show(conn, shows):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO shows(name,location,month)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, shows)
    return cur.lastrowid


def select_show_by_location(conn, location):
    cur = conn.cursor()

    cur.execute("SELECT * FROM shows WHERE location=?", (location, ))

    rows = cur.fetchall()

    for rows in rows:
        print(rows)


def select_show_by_month(conn, month):
    cur = conn.cursor()

    cur.execute("SELECT * FROM shows where month=?", (month, ))

    rows = cur.fetchall()

    for rows in rows:
        print(rows)


def main():
    database = "fests.db"

    #workbook = xlrd.open_workbook('fests.xls')
    #ws = workbook.sheet_by_name('fests')
    sql_create_shows_table = """ CREATE TABLE IF NOT EXISTS shows (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        location text,
                                        month text
                                    ); """

    # create a database connection
    conn = create_connection(database)
    with conn:
        #for row in range(ws.nrows):
            #create_show({"name": ws.cell(row, 0).value, "location": ws.cell(row, 1).value,
            #             "month": ws.cell(row, 2).value})

        show_1 = ('Countdown', 'San Bernadino', 'January')
        show_2 = ('Snowglobe', 'Tahoe', 'January')
        show_3 = ('OMFG', 'San Diego', 'January')
        show_4 = ('LED Anniversary', 'San Diego', 'February')
        show_5 = ('CRSSD', 'San Diego', 'March')
        show_6 = ('Coachella', 'Indio', 'April')
        show_7 = ('StageCoach', 'Indio', 'April')
        show_8 = ('LED USA', 'San Diego', 'May')
        show_9 = ('EDC', 'Las Vegas', 'May')
        show_10 = ('Lightning in a Bottle', 'SLO', 'May')
        show_11 = ('Splash House', 'Palm Springs', 'June')
        show_12 = ('Audiotistic', 'San Francisco', 'July')
        show_13 = ('Outside Lands', 'San Francisco', 'August')
        show_14 = ('Splash House', 'Palm Springs', 'August')
        show_15 = ('Life is Beautiful', 'Las Vegas', 'September')
        show_16 = ('Kaaboo', 'San Diego', 'September')
        show_17 = ('CRSSD', 'San Diego', 'October')
        show_18 = ('Escape', 'San Bernadino', 'October')

        show_id1 = create_show(conn, show_1)
        show_id2 = create_show(conn, show_2)
        show_id3 = create_show(conn, show_3)
        show_id4 = create_show(conn, show_4)
        show_id5 = create_show(conn, show_5)
        show_id6 = create_show(conn, show_6)
        show_id7 = create_show(conn, show_7)
        show_id8 = create_show(conn, show_8)
        show_id9 = create_show(conn, show_9)
        show_id10 = create_show(conn, show_10)
        show_id11 = create_show(conn, show_11)
        show_id12 = create_show(conn, show_12)
        show_id13 = create_show(conn, show_13)
        show_id14 = create_show(conn, show_14)
        show_id15 = create_show(conn, show_15)
        show_id16 = create_show(conn, show_16)
        show_id17 = create_show(conn, show_17)
        show_id18 = create_show(conn, show_18)

        select_show_by_month(conn, "April")



if __name__ == '__main__':
    main()
