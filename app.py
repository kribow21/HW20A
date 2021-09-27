import dbcreds
import mariadb

conn= None
cursor=None

def create_post():
        print("Create your post:")
        user_content = input()
        cursor.execute("INSERT INTO blog_post(username, content) VALUES (?, ?)", [name, user_content,])
        conn.commit()
        print('Post created')
def view_posts():
        cursor.execute("SELECT * FROM blog_post")
        post_list = cursor.fetchall()
        for post in post_list:
            print(post)

try:
    conn=mariadb.connect(
                    user=dbcreds.user,
                    password=dbcreds.password,
                    host=dbcreds.host,
                    port=dbcreds.port,
                    database=dbcreds.database)
    cursor=conn.cursor()

    print("Username:")
    name = input()
    print("Select an option:")
    print("For writting a new post enter '1' , For seeing all post enter '2'")
    choice = input()
    # inserts new blog post into the database
    if(choice == '1'):
        create_post()
    #user can see all blog posts
    elif(choice == '2'):
        view_posts()

except mariadb.DataError: 
    print('Something went wrong with your data')
except mariadb.OperationalError:
    print('Something wrong with the connection')
except mariadb.ProgrammingError:
    print('Your query was wrong')
except mariadb.IntegrityError:
    print('Your query would have broken the database and we stopped it')
except mariadb.InterfaceError:
    print('Something wrong with database interface')
except:
    print('Something went wrong')
finally:
    if(cursor != None):
        cursor.close()
        print('cursor closed')
    else:
        print('no cursor to begin with')
    if(conn != None):   
        conn.rollback()
        conn.close()
        print('connection closed')
    else:
        print('the connection never opened, nothing to close')
