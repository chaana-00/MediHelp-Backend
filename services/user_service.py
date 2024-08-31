def create_user(mysql, user):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name, email, nic, age, gender, address, mobile, img, password) VALUES (%s, %s, %s,  %s, %s, %s, %s, %s, %s)",
                (user['name'], user['email'], user['nic'], user['age'], user['gender'],  user['address'], user['mobile'], user['img'], user['password']))
    mysql.connection.commit()
    cur.close()


def get_users(mysql):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return users


def get_user_by_id(mysql, user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    return user


def update_user(mysql, user_id, user):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET name = %s, email = %s, nic = %s, age = %s, gender = %s, address = %s, mobile = %s, img = %s, password = %s WHERE id = %s",
                (user['name'], user['email'], user['nic'], user['age'],  user['gender'], user['address'], user['mobile'], user['img'], user['password'], user_id))
    mysql.connection.commit()
    cur.close()


def delete_user(mysql, user_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mysql.connection.commit()
    cur.close()


def get_user_by_email_from_db(mysql, email):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()
    if user:
        return {
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'nic': user[3],
            'age': user[4],
            'gender': user[5],
            'address': user[6],
            'mobile': user[7],
            'img': user[8],
            'password': user[9]
        }
    return None



def count_users(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    cursor.close()
    return user_count
