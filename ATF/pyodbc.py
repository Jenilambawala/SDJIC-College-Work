# Install => python -m pip install pyodbc


import pyodbc

# Create a connection to the database 
conn = pyodbc.connect('DRIVER=(IBM DB2 ODBC DRIVER); SERVER-localhost; DATABASE=my_database; UID=my_username; PhDemy_password')

# Execute a query and store the results in a cursor object

cursor = conn.cursor()
cursor.execute('SELECT FROM my_table')

#Iterate over the results and print them out for row in cursor:
for row in cursor:
    print(row)

#close the cursor and the connection
cursor.close()
conn.close()