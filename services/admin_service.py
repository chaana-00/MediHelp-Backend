def get_admin_by_email(mysql, email):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admins WHERE email = %s", (email,))
    admin = cur.fetchone()
    cur.close()
    if admin:
        return {
            'id': admin[0],
            'email': admin[1],
            'password': admin[2]
        }
    return None
