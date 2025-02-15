
from flask import Flask, render_template, request
import mysql.connector
import settings

app = Flask(__name__)

# DB Create
def create_database():
    connection = mysql.connector.connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.DB_NAME}")
    cursor.close()
    connection.close()

# DB Connection
def get_db_connection():
    return mysql.connector.connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME
    )

# Table Create
def create_books_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            pages INT NOT NULL,
            published_year INT NOT NULL
        )
    """)
    cursor.close()
    connection.close()

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Add Book Page
@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Formdan ma'lumotlarni olish va db ga yozish
        pass
    return render_template('add_book.html')

if __name__ == '__main__':
    # Dastur ishga tushishidan oldin database va table yaratish
    create_database()
    create_books_table()

    # Flask serverni ishga tushirish
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG
    )

