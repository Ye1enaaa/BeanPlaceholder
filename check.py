import sqlite3

# Connect to the database
conn = sqlite3.connect('beanCounter.db')
cursor = conn.cursor()
beanArray = []

def allFetchData():
    # Execute a SELECT query to retrieve data
    select_query = '''
    SELECT * FROM beans;
    '''
    cursor.execute(select_query)

    # Fetch all rows returned by the query
    rows = cursor.fetchall()

    # Check if any rows are returned
    if len(rows) > 0:
        print("Data is stored in the database.")
        for row in rows:
            print(row)  # Print each row
    else:
        print("No data found in the database.")

def fetchBeanCount():
    global beanArray

    select_good_bean_query = '''
    SELECT SUM(good) FROM beans;
    '''
    cursor.execute(select_good_bean_query)
    goodBean = cursor.fetchone()[0]
    #print(sum)

    select_bad_bean_query = '''
    SELECT SUM(bad) FROM beans;
    '''
    cursor.execute(select_bad_bean_query)
    badBean = cursor.fetchone()[0]
    #print(sum)

    beanArray.append(goodBean)
    beanArray.append(badBean)
    print(beanArray)

fetchBeanCount()
conn.close()
