import mysql.connector

print("Please enter your SQL server User Name and Password Below : \n")
user_name = input("Enter the User Name  : \n")
password = input("Enter the Password : \n")
conn = mysql.connector.connect(
    host="localhost",
    user=user_name,
    password=password
)

cursor = conn.cursor()

with open("art_collection.sql", "r") as sql_file:
    sql_script = sql_file.read()
    statements = sql_script.split(';')
    
    for statement in statements:
        if statement.strip():
            try:
                cursor.execute(statement)
                conn.commit()
            except mysql.connector.Error as err:
                print("An error occurred:", err)
                break

cursor.close()
conn.close()

print("Database setup complete.")
