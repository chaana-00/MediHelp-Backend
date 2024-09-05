def create_prediction(mysql, userId, prediction, datetime, age):
    cursor = mysql.connection.cursor()
    cursor.execute(
        'INSERT INTO prediction (userId, prediction, datetime, age) VALUES (%s, %s, %s, %s)',
        (userId, prediction, datetime, age)
    )
    mysql.connection.commit()
    cursor.close()


def get_all_predictions(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM prediction')
    predictions = cursor.fetchall()
    cursor.close()
    return predictions


def get_predictions_under_20(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM prediction WHERE age < 18')
    predictions = cursor.fetchall()
    cursor.close()
    return predictions


def count_predictions_under_20(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM prediction WHERE age < 18')
    count = cursor.fetchone()[0]
    cursor.close()
    return count


def get_predictions_by_user(mysql, userId):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM prediction WHERE userId = %s', (userId,))
    predictions = cursor.fetchall()
    cursor.close()
    return predictions

