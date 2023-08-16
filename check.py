import sqlite3
import json
import pymysql
from datetime import datetime
#Global Var
beanArray = []

# Connect to the database
conn = sqlite3.connect('beanCounter.db')
cursor = conn.cursor()

#mysql file
mysqlConn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="coffee_fnl"
)
mysqlCursor = mysqlConn.cursor()

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
#sqlite to json format

dataDict = {
    "good": beanArray[0],
    "bad": beanArray[1],
    "kilograms": (beanArray[1] * 0.2) / 1000 
}

with open('beanData.json', 'w') as json_file:
    json.dump(dataDict, json_file)

json_data = json.dumps(dataDict)
goodBean = beanArray[0]
badBean = beanArray[1]
kiloOfBeans = (beanArray[1] * 0.2) / 1000
formattedKilo = "{:.4f}".format(kiloOfBeans)
createdAt = datetime.now()
updatedAt = createdAt
insert_query = "INSERT INTO bean_counts (good, bad, kilograms, created_at, updated_at) VALUES (%s, %s, %s, %s, %s);"
mysqlCursor.execute(insert_query, (goodBean, badBean, formattedKilo, createdAt, updatedAt))
mysqlConn.commit()
mysqlConn.close()
conn.close()
