import dbcreds
import mariadb

try:
    conn=mariadb.connect(
                    user=dbcreds.user,
                    password=dbcreds.password,
                    host=dbcreds.host,
                    port=dbcreds.port,
                    database=dbcreds.database)
    cursor=conn.cursor()

    # conn.commit()

    cursor.close()
    conn.close()
    print('all good')
except: 
    print('Something went wrong')