import sqlite3

CREATE_RESTAURANT_TABLE = "CREATE TABLE IF NOT EXISTS restaurant(R_name TEXT, R_id INTEGER PRIMARY KEY, R_cuisine TEXT, no_of_emp INTEGER);"


INSERT_RESTAURANT = "INSERT INTO restaurant(R_name, R_id, R_cuisine, no_of_emp) VALUES(?,?,?,?);"

GET_ALL_RESTAURANTS = "SELECT * FROM restaurant;"

GET_RESTAURANTS_BY_NAME =  "SELECT * FROM restaurant WHERE R_name = ?;"

GET_RESTAURANTS_BY_EMP = "SELECT * FROM restaurant WHERE no_of_emp > ?;"


def connect():
    return sqlite3.connect('data.db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_RESTAURANT_TABLE)


def add_restaurant(connection, R_name, R_id, R_cuisine, no_of_emp):
    with connection:
        connection.execute(INSERT_RESTAURANT, (R_name, R_id, R_cuisine, no_of_emp))

def get_all_restaurants(connection):
    with connection:
        return connection.execute(GET_ALL_RESTAURANTS).fetchall()

def get_restaurant_by_name(connection, R_name):
    with connection:
        return connection.execute(GET_RESTAURANTS_BY_NAME, (R_name,)).fetchall()

def get_restaurant_by_employeecount(connection, no_of_emp):
    with connection:
        return connection.execute(GET_RESTAURANTS_BY_EMP, (no_of_emp,)).fetchall()


    
