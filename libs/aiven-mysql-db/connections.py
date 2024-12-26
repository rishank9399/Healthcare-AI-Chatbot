
import pymysql


user="avnadmin"
password=""




def test(user,password):
        
    timeout = 10
    connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="",
    password=password,
    read_timeout=timeout,
    port=15701,
    user=user,
    write_timeout=timeout,)

    try:    

        cursor = connection.cursor()

    except:
        print("Some Error occured. Could not connect to database ")
        return False

        
    else:
        print("Connected to Database")
        try:
            cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")

        except:{}
        
        cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
        cursor.execute("SELECT * FROM mytest")
        print(cursor.fetchall())
        return True 

test(user,password)



