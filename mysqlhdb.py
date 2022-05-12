#!/usr/bin/python

import csv
import MySQLdb
import os

def sendit() :
    mydb = MySQLdb.connect(host='127.0.0.1',
        user='root',
        passwd='',
        db='maz')
    cursor = mydb.cursor()

    ##send the attendance
    path = 'Attendance'
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-1]
    filename = newest
    ## read csv
    csv_data = csv.reader(open(filename,'rU'))

    ## create insertion query
    next(csv_data)
    for row in csv_data:
        cursor.execute('INSERT INTO testcsv(Id ,Name, Date, Time)' \
                'VALUES(%s, %s, %s, %s)',  row)

    mydb.commit() ## execute insertion query
    cursor.close()
    mydb.close()
    print ("Import to MySQL is over")