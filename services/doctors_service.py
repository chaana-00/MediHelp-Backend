def create_doctor(mysql, doctor):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO doctor (name, specifications, hospital, contact) VALUES (%s, %s, %s, %s)",
                (doctor['name'], doctor['specifications'], doctor['hospital'], doctor['contact']))
    mysql.connection.commit()
    cur.close()


def get_doctors(mysql):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM doctor")
    doctors = cur.fetchall()
    cur.close()
    return doctors


def get_doctor_by_id(mysql, doctor_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM doctor WHERE id = %s", (doctor_id,))
    doctor = cur.fetchone()
    cur.close()
    return doctor


def update_doctor(mysql, doctor_id, doctor):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE doctor SET name = %s, specifications = %s, hospital = %s, contact = %s WHERE id = %s",
                (doctor['name'], doctor['specifications'], doctor['hospital'], doctor['contact'], doctor_id))
    mysql.connection.commit()
    cur.close()


def delete_doctor(mysql, doctor_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM doctor WHERE id = %s", (doctor_id,))
    mysql.connection.commit()
    cur.close()


def search_doctors_by_specifications(mysql, spec):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM doctor WHERE specifications LIKE %s", ('%' + spec + '%',))
    doctors = cur.fetchall()
    cur.close()
    return doctors



def count_doctors(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM doctor")
    user_count = cursor.fetchone()[0]
    cursor.close()
    return user_count
