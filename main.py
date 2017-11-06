import sqlite3

def Main():

    try:
        con=sqlite3.connect('void_db.db')
        cur=con.cursor()
        cur.execute('select * from wm;')

        con.commit()

        data=cur.fetchall()
        for row in data:
            print(data)

    except sqlite3.Error:
        if con:
            con.rollback()
            print("problem whis sqlconnect")
    finally:
        if con:
            con.close()



if __name__ == '__main__':
    Main()
