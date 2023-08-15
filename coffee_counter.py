import sqlite3
from tkinter import *
from tkinter import ttk

def printS():
    print("hi")

def addBadBeanData():
    # Example: Insert data into the table
    insert_data_query = '''
    INSERT INTO beans (good,bad) VALUES (?,?);
    '''
    bean_data = (0,1)
    cursor.execute(insert_data_query, bean_data)
    conn.commit()
def addGoodBeanData():
    insert_data_query = '''
    INSERT INTO beans (good,bad) VALUES (?,?);
    '''
    bean_data = (1,0)
    cursor.execute(insert_data_query, bean_data)
    conn.commit()
 
# Step 1: Connect to the database (creates a new file if it doesn't exist)
conn = sqlite3.connect('beanCounter.db')

cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS beans (
    id INTEGER PRIMARY KEY,
    good FLOAT,
    bad FLOAT
);
'''
cursor.execute(create_table_query)

#Window
root = Tk()
wndow =  ttk.Frame(root, padding= 10)
wndow.grid()
ttk.Button(wndow, text= "Good", command=addGoodBeanData).grid(column=1, row=0)
ttk.Button(wndow, text= "Bad", command=addBadBeanData).grid(column=2, row=0) 

#Commit changes and close the connection
root.mainloop()
conn.close()

