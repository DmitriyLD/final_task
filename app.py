import psycopg2
from psycopg2 import sql

def connect_db():
    connection = psycopg2.connect(
        user="postgres",
        password="my_password",
        host="db", 
        port="5432",
        database="postgres_db"
    )
    return connection

def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER,
            department VARCHAR(100)
        );
    """)

def insert_data(cursor):
    cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ("Alice", 30, "HR"))
    cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ("Bob", 25, "Engineering"))
    cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ("Charlie", 35, "Sales"))

def fetch_data(cursor):
    cursor.execute("SELECT * FROM employees;")
    records = cursor.fetchall()
    
    for record in records:
        print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Department: {record[3]}")

if __name__ == "__main__":
    conn = connect_db()
    cursor = conn.cursor()
    
    create_table(cursor)
    insert_data(cursor)
    
    conn.commit()  # Подтверждение изменений
    fetch_data(cursor)
    
    cursor.close()
    conn.close()