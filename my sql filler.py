import mysql.connector
from mysql.connector import Error
print("plese enter you sql information")
host_db=input(("enter your hostname: "))
user_db=input(("enter your username: "))
password_db=input(("enter your password: "))
while True:
   print("\n===============") 
   print("what to do")
   print("1. for database , 2. create a table , 3. insert data in a table , 4. exit / quit")
   print("=================")
   try:
       chooise= float(input("choose (1, 2, 3, or 4): "))
   except valueError:
       print("invalid input! please enter a number.")
       continue
   if chooise==1:
  
  

  
      try:
          print("test1")
          connection = mysql.connector.connect(
             host= host_db,
             user= user_db,
             password= password_db
             
            )
          print("test2")
          if connection.is_connected():
              cursor = connection.cursor()

              db_name = input(("enter a name for the database: "))
              cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
              print(f"database '{db_name}' created successfully (or already exists).")

              cursor.execute(f"use {db_name}")
              print("test3")      
                 
      except Error as e:
                       print(f"error while connecting to mysql: {e}")
      
      finally:

            if 'connection' in locals() and connection.is_connected():
             cursor.close()
             connection.close()
             print("mysql connection closed.")

  
   elif chooise==2:
    import mysql.connector
    from mysql.connector import Error
    try:
        connection = mysql.connector.connect(
            host= host_db,
            user= user_db,
            password= password_db
              )
        if connection.is_connected():
                 cursor = connection.cursor()
    
        db_name = input("enter the name of the database you want to create the table in: ")

        cursor.execute(f"use {db_name}")

        tb_name = input(("plese enter a name for the table: "))
        columns = []
        print("\nDefin your columns (type 'done' when you are finished):")
        while True:
            col_def = input("Enter column definition (or type 'done'): ").strip()
            if col_def.lower() == 'done':
                break
            if col_def:
                columns.append(col_def)

        if not columns:
                 print("you didn't enter any columns! table creatoin cancelled.")
        else:
                columns_str = ", ".join(columns)

                table_query = f"CREATE TABLE IF NOT EXISTS {tb_name} ({columns_str});"
                  
        
        cursor.execute(table_query)
        print("table created successfully")

    except Error as e:
        print(f"error while connecting to mysql: {e}")

    finally:

            if 'connection' in locals() and connection.is_connected():
             cursor.close()
             connection.close()
             print("mysql connection closed.")

   elif chooise == 3:
    import mysql.connector
    from mysql.connector import Error
    try:
        connection = mysql.connector.connect(
            host= host_db,
            user= user_db,
            password= password_db
              )
        if connection.is_connected():
                 cursor = connection.cursor()

        db_name = input("enter the name of the dadabase: ").strip()
        cursor.execute(f"USE {db_name}")

        tb_name = input("enter the table name to insert data into: ").strip()
        while True:
             columns = []
             values = []
             col_count = 1
             print("\n--- insert a new row into '{tb_name}' ---")
             print("type 'done' as the column name when you are finished entering data.") 

             while True:
               col_name = input(f"column {col_count} name (or type 'done'): ").strip()
               if col_name.lower() == 'done':
                   break
               if col_name:
                   col_value = input(f"enter value for '{col_name}': ").strip()
                   columns.append(col_name)
                   values.append(col_value)
                   col_count += 1

             if not columns:
                    print("no data entered! insertion cancelled.")
             else:
                 cols_str = ", ".join(columns)
                 placeholders = ", ".join(["%s"] * len(columns))

                 insert_query = f"insert into {tb_name} ({cols_str}) values ({placeholders})"

                 cursor.execute(insert_query, tuple(values))
                 connection.commit()

                 print(f"data inserted successfully into '{tb_name}'! (Row id: {cursor.lastrowid})")
             another = input("\nDO you want to add another row? (y/n: ").strip().lower()
             if another != 'y':
                 print("Returing to main menu...")
                 break
 
    except Error as e:
           print(f"error while connecting to mysql: {e}")

    finally:

            if 'connection' in locals() and connection.is_connected():
             cursor.close()
             connection.close()
             print("mysql connection closed.")

   elif chooise == 4:

        print("exiring program")
        break
           
            
      


    
